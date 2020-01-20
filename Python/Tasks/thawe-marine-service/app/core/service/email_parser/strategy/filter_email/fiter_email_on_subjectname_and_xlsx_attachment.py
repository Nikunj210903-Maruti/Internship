import os
import re

from app.common import FILE_PATH
from .interface_filter_email import FilterEmailService
from ......common import create_downloaded_attachment_file_name, make_dir, today_date


class FilterEmailOnSubjectNameandAttachmentTypeService(FilterEmailService):
    "It will filter emails based on subject name and attachment type. It will filter emails with xlsx file attachment"

    def __init__(self, message):
        self.message = message
        self.message.attachments = []
        self.create_folder()

    def create_folder(self):
        xlsx_folder_location = os.path.abspath(
            os.path.join(__file__, '..', '..', '..', '..', '..', '..', '..', 'data', 'noon_report', 'xlsx_file',
                         str(today_date())))
        make_dir(xlsx_folder_location)

    def filter_email(self):
        self.filter_emails_on_subject()
        self.filter_emails_on_attachment_type()

    def filter_emails_on_subject(self):
        filtered_emails = []
        for e_mail in self.message.emails:
            if re.match("(\w)+(_Noon_Report_)([0-2][0-9]|(3)[0-1])(-)(((0)[0-9])|((1)[0-2]))(-)\d{4}",
                        e_mail['Subject']):
                filtered_emails.append(e_mail)
        self.message.emails = filtered_emails

    def filter_emails_on_attachment_type(self):
        filtered_emails = []
        for e_mail in self.message.emails:
            if self.check_and_download_attachment_with_xlsx_file(e_mail):
                filtered_emails.append(e_mail)
        self.message.emails = filtered_emails

    def check_and_download_attachment_with_xlsx_file(self, e_mail):
        for part in e_mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('content-Disposition') is None:
                continue
            file = part.get_filename()
            if bool(file):
                extension = file.split('.')[1]
                if extension == "xlsx":
                    self.download_attachment(e_mail, part, file, "xlsx")
                    return True
        return False

    def download_attachment(self, e_mail, part, file, extension):
        shipname = e_mail["Subject"].split("_", 1)[0]
        filename = create_downloaded_attachment_file_name(shipname, extension)
        filepath = FILE_PATH + str(today_date()) + "/" + filename
        with open(file, 'wb') as f:
            f.write(part.get_payload(decode=True))
        os.rename(file, filepath)
        self.message.attachments.append(filename)
