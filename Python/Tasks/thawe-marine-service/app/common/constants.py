""" API List """
EMAIL_PARSER_API = "/email-parser"

APP_READINESS_API = '/k8/readiness'
APP_LIVENESS_API = '/k8/liveness'
APP_TERMINATION_API = '/k8/termination'

"""email_parser"""
FOLDER_SELECT = 'INBOX'
FILE_PATH = "data/noon_report/xlsx_file/"
KEYS = ['Speed & Fuel consumption data', "Navigation parameters", "ME parameters", "ROBs"]

""" Date Format """
DT_FMT_dmy = '%d/%m/%y'  # 31/12/17
DT_FMT_bdYIMp = '%b %d %Y %I:%M %p'  # Jul 16 2017 08:46 PM
DT_FMT_ymdHMSf = '%Y-%m-%d %H:%M:%S.%f'  # 2017-07-19 06:58:20.370
DT_FMT_ymdHMSfz = '%Y-%m-%d %H:%M:%S.%f%z'  # 2017-07-19 06:58:20.370+00:00
DT_FMT_ymdHMS = '%Y-%m-%d %H:%M:%S'  # 2017-07-19 06:58:20
DT_FMT_Ymd = '%Y-%m-%d'  # 2017-09-11
DT_FMT_YMD = '%Y/%m/%d'
DT_FMT_ymdHM = '%Y-%m-%d %H:%M'
DT_FMT_dbYHMS = '%d-%b-%Y %H:%M:%S'
DT_FMT_dbYHMSf = '%d-%b-%Y %H:%M:%S.%f'
DT_FMT_HM = '%H:%M'

ERROR_MSG_TEMPLATE = 'File: {file_name} : {file_line_no} \n Error: {err} \n Error Description: {err_info} \n Traceback: {traceback} \n API: {path} \n Info: {info}'

PRODUCT_NAME = 'Thawe-Marine-Service'
APP_NAME = 'Thawe-Marine-Service'
