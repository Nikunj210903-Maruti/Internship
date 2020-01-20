import email
import imaplib
import json

from flask import current_app
from imapclient import IMAPClient

from ...models import MysqlDatabaseHandler, get_all_eid, insert_many_eid, get_vessel_id, insert_into_vessel_noon_report, \
    get_noon_report_base_parameter
from ....common import FOLDER_SELECT, get_utc_timestamp, InvalidEmailData


class EmailParserService:
    "It is a service that will set configurations like email-id ane password. It will also store vessel_noon_report data to database"

    def __init__(self, message, FilterEmail, ExtractDataFromFile):
        self.message = message
        self.ExtractDataFromFile = ExtractDataFromFile
        self.FilterEmail = FilterEmail
        self.initialize()

    def read_emails(self):
        if self.message.mail:
            self.search_emails(None, "ALL")
            self.get_unread_eids()
            self.fetch_emails()
            filter_email = self.FilterEmail(self.message)
            filter_email.filter_email()
            extract_data_from_file = self.ExtractDataFromFile(self.message)
            extract_data_from_file.extract_data_from_file()
            self.inset_noon_report()

    def get_initial_data(self):
        with MysqlDatabaseHandler() as conn:
            get_all_eid(conn, self.message)
            self.message.already_read_ids = []
            if self.message.rows_eid:
                for row in self.message.rows_eid:
                    self.message.already_read_ids.append(row['e_id'])

            get_noon_report_base_parameter(conn, self.message)
            self.message.parameter_dict = {}
            for parameter in self.message.rows_noon_report_base_parameters:
                self.message.parameter_dict[parameter['type']] = json.loads(parameter["params"])
            self.message.keys = self.message.parameter_dict.keys()

    def initialize(self):
        try:
            self.message.mail = imaplib.IMAP4_SSL(current_app.config['GOOGLE_IMAP_SERVER'])
            self.message.mail.login(current_app.config['USER'], current_app.config['PASSWORD'])
            self.message.mail.select(FOLDER_SELECT)
            self.get_initial_data()
        except IMAPClient.Error:
            self.message.mail = None
            raise InvalidEmailData

    def search_emails(self, key, value):
        result, result_bytes = self.message.mail.search(None, key, "{}".format(value))
        self.message.eids = result_bytes[0].split()

    def get_unread_eids(self):
        self.message.unread_eids = []
        for id in self.message.eids:
            if int(id.decode("utf-8")) not in self.message.already_read_ids:
                self.message.unread_eids.append(id)

    def insert_eids(self):
        with MysqlDatabaseHandler() as conn:
            insert_many_eid(conn, self.message)
            conn.commit()

    def fetch_emails(self):
        self.message.emails = []
        for num in self.message.unread_eids:
            typ, data = self.message.mail.fetch(num, '(RFC822)')
            data = email.message_from_bytes(data[0][1])
            self.message.emails.append(data)
        self.insert_eids()

    def create_noon_report_data(self, data):
        report_date = data["date"]
        vessel_id = self.message.row_vessel_id['id']
        data_row = data['row']

        for row in data_row.keys():
            if row in self.message.keys:
                report_type = row
                params = self.message.parameter_dict[row]
                data_params = data_row[row].keys()
                temp = data_row[row]
                value = {}
                for param in params:
                    if param in data_params:
                        value[param] = temp[param]
                    else:
                        value[param] = ""
                self.message.new_data.append(
                    {"vessel_id": vessel_id, 'type': report_type, "value": str(value), "report_date": report_date,
                     "created_at": get_utc_timestamp(), "created_by": 1, "modified_at": get_utc_timestamp(),
                     "modified_by": 1})

    def inset_noon_report(self):
        self.message.new_data = []
        with MysqlDatabaseHandler() as conn:
            for data in self.message.data:
                get_vessel_id(conn, data["ship_name"], self.message)
                if self.message.row_vessel_id:
                    self.create_noon_report_data(data)
            insert_into_vessel_noon_report(conn, self.message.new_data)
            conn.commit()
