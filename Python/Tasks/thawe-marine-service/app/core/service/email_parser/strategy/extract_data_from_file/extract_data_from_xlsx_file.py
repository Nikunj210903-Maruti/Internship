import xlrd

from app.common import FILE_PATH, KEYS, xlrd_date_to_date_type
from .inerface_extract_data_from_file import ExtractDataFromFileService
from ......common import today_date


class ExtractDataFromXlsxFileService(ExtractDataFromFileService):
    "It will extract data from xlsx file as a dictionary and store it into a list."

    def __init__(self, message):
        self.message = message
        self.message.data = []

    def extract_data_from_file(self):
        for attachment in self.message.attachments:
            self.get_data_from_xlsx_file(attachment)

    def get_data_from_xlsx_file(self, attachment):
        filepath = FILE_PATH + str(today_date()) + "/" + attachment
        wb = xlrd.open_workbook(filepath)
        sheet = wb.sheet_by_index(0)
        data = {}
        data["ship_name"] = sheet.cell(1, 1).value
        data["date"] = sheet.cell(2, 1).value
        data['date'] = xlrd_date_to_date_type(wb, data['date'])

        data["row"] = {}
        data_row = data["row"]
        for row in range(4, sheet.nrows):
            cell_data = sheet.cell(row, 1).value
            if len(cell_data) == 0:
                continue
            if cell_data in KEYS:
                data_row[cell_data] = {}
                temp = data_row[cell_data]
            else:
                if 'temp' in locals():
                    temp[sheet.cell(row, 1).value] = sheet.cell(row, 2).value
        self.message.data.append(data)
