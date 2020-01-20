import json
import logging
import os
import re
import sys
import traceback
from base64 import b64encode
from configparser import ConfigParser
from datetime import datetime
from datetime import timedelta
from io import StringIO
from urllib.parse import urlparse
from uuid import uuid4,uuid1

import pytz
import requests
import xlrd
from dateutil import tz
from flask import current_app, request, has_request_context
from flask_log_request_id import current_request_id
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .constants import (DT_FMT_ymdHMSf, ERROR_MSG_TEMPLATE, DT_FMT_HM)
from .enums import HttpMethodEnum


def make_dir(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_current_timestamp(timezone=pytz.utc):
    return datetime.now(tz=timezone)


def datetime_to_str(date_time, str_format=DT_FMT_ymdHMSf):
    return date_time.strftime(str_format)


def str_to_datetime(date_time, str_format=DT_FMT_ymdHMSf):
    return datetime.strptime(date_time, str_format)


def get_utc_timestamp():
    return datetime_to_str(get_current_timestamp())


def get_utc_datetime():
    return datetime.now(tz=pytz.utc)

def today_date():
    return datetime.now(tz=pytz.utc).date()



def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)
        cp = ConfigParser()
        cp.read_file(config)
        return dict(cp.items('dummy_section'))


class HttpErrorHandler:
    @staticmethod
    def make_error_response(http_status=500, error_code='', error_message='', ok=False):
        return {
                   'ok': ok,
                   'error': error_code,
                   'message': error_message
               }, http_status

    @staticmethod
    def unauthorized_error():
        return HttpErrorHandler.make_error_response(401, "UNAUTHORIZED",
                                                    "Unauthorized: Access is denied due to invalid credentials.")


def error_traceback(error, info_msg=''):
    from app import app
    with app.app_context():
        exc_type, exc_value, exc_traceback = sys.exc_info()
        path = ''
        if request and hasattr(request, 'path'):
            path = request.path
        text = ERROR_MSG_TEMPLATE.format(file_name=exc_traceback.tb_frame.f_code.co_filename,
                                         file_line_no=str(exc_traceback.tb_lineno),
                                         err_info=error.__doc__,
                                         err=str(error),
                                         traceback=str(repr(traceback.format_tb(exc_traceback))),
                                         path=path,
                                         info=str(info_msg))

        slack_post({"text": text})
        return text


def get_ip_address(_request):
    if has_request_context():
        proxy_ip_key = 'HTTP_X_FORWARDED_FOR'
        ip_address = request.environ[proxy_ip_key] if proxy_ip_key in _request.environ else _request.remote_addr
        if isinstance(ip_address, str):
            # return last access IP address
            return ip_address.split(',')[-1]


def get_request_correlation_id():
    if has_request_context():
        if request.headers.get('WT_CORRELATION_ID', None) is None:
            return current_request_id()
        return request.headers.get('WT_CORRELATION_ID', '-')
    return uuid4().__str__()


def get_request_header_value(field_name):
    if has_request_context():
        return request.headers.environ.get(field_name, '-')
    return '-'


def get_request_user_id():
    if has_request_context():
        return request.headers.get('WT_USER_ID', '-')
    return '-'


def get_http_request_fields(record):
    record.correlation_id = get_request_correlation_id()
    record.user_id = get_request_user_id()
    record.path_info = get_request_header_value('PATH_INFO')
    record.query_string = get_request_header_value('QUERY_STRING')
    record.method = get_request_header_value('REQUEST_METHOD')
    record.http_origin = get_request_header_value('HTTP_ORIGIN')
    record.ip_address = get_ip_address(request)
    record.user_agent = get_request_header_value('HTTP_USER_AGENT')
    record.file_path = record.pathname
    return record


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record = get_http_request_fields(record)
        return super().format(record)


class GrayLogContextFilter(logging.Filter):

    def filter(self, record):
        get_http_request_fields(record)
        return True


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.exception('Got exception during processing: %s', exception)
    error_traceback(exception)


def is_success_request(status_code):
    return 200 <= status_code <= 299


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def invoke_http_request(endpoint, method, headers, payload=None, timeout=61):
    _request = requests_retry_session()
    _request.headers.update({
        **headers
    })
    try:
        response = None
        if method == HttpMethodEnum.GET.value:
            response = _request.get(url=endpoint, data=payload, timeout=timeout)
        if method == HttpMethodEnum.POST.value:
            response = _request.post(url=endpoint, data=payload, timeout=timeout)
        if method == HttpMethodEnum.PUT.value:
            response = _request.put(url=endpoint, data=payload, timeout=timeout)
        if method == HttpMethodEnum.DELETE.value:
            response = _request.delete(url=endpoint, data=payload, timeout=timeout)
        log_failed_http_request(endpoint, response.text, response.status_code)
        return response.json(), response.status_code
    except requests.exceptions.RequestException:
        from app import app
        app.logger.exception('Error raised while invoking %s', endpoint)
        raise


def log_failed_http_request(endpoint, response, status_code):
    if not is_success_request(status_code):
        msg = 'Http {} | Error-{} : {}'.format(endpoint, status_code, response)
        from app import app
        app.logger.error(msg)
        slack_post({"text": msg})


def slack_post(payload, webhook=None):
    headers = {'content-type': 'application/json'}
    if not webhook:
        webhook = current_app.config['ERROR_WEBHOOK_URL']
    try:
        pass
        # response, status_code = invoke_http_request(webhook, HttpMethodEnum.POST.value, headers, json.dumps(payload))
        # return response
    except (requests.exceptions.RequestException, Exception):
        from app import app
        app.logger.exception('An error occurred while invoking the Slack webhook')


def get_search_string(str_value, replace_with=',', replace_to=' ', to_lower_case=True):
    if isinstance(str_value, str):
        return str_value.replace(replace_with, replace_to).strip().lower()[:2000]


def notify_es_pagination_limit(endpoint, response):
    if response and isinstance(response, dict):
        total_count = int(response.get('hits', {}).get('total', {}).get('value', 0))
        result_count = len(response.get('hits', {}).get('hits', []))
        if result_count < total_count:
            msg = "-------------------{linesep}" \
                  "`Alert{linesep}`" \
                  "*Elasticsearch Pagination Required*{linesep}" \
                  "- API: {endpoint}{linesep}" \
                  "- Results: {result}/{total}{linesep}" \
                  "-------------------"
            slack_post(
                {"text": msg.format(result=result_count,
                                    total=total_count,
                                    endpoint=endpoint,
                                    linesep=os.linesep)})


def timezone_converter(datetime_str, datetime_format=DT_FMT_HM, from_zone='', to_zone='UTC',
                       is_string_input=True):
    from_timezone = tz.gettz(from_zone)
    to_timezone = tz.gettz(to_zone)
    if is_string_input:
        utc = str_to_datetime(datetime_str, datetime_format)
    else:
        utc = datetime_str
    utc = utc.replace(tzinfo=from_timezone)
    return utc.astimezone(to_timezone)


def get_next_day_date(date):
    return date + timedelta(days=1)


def is_pattern_matched(str_val, pattern):
    result = re.match(pattern, str_val)
    return True if result else False


def str_format_datetime(date_time, str_format='%Y-%m-%d %H:%M:%S.%f'):
    return date_time.strftime(str_format)


def get_domain_from_url(url):
    domain_name = '{uri.netloc}'.format(uri=urlparse(url))
    return domain_name if domain_name else url


def is_json(question_string):
    try:
        json.loads(question_string)
        return True
    except ValueError:
        return False


def generate_basic_token(username, password):
    return 'Basic %s' % b64encode(
        str.encode('{username}:{password}'.format(username=username, password=password))).decode("ascii")


def xlrd_date_to_date_type(wb, xlrd_date):
    date_type = str(datetime(*xlrd.xldate_as_tuple(xlrd_date, wb.datemode)).date())
    return date_type


def create_downloaded_attachment_file_name(shipname,extension):
    filename = shipname + "_" + str(today_date()) + "_" + str(uuid1()) + "." + extension
    return filename
