from .helper import fetch_rows, insert_rows, fetch_row
from ...models import sql_scripts
from ....common import get_utc_timestamp

__all__ = ['get_all_eid', 'insert_many_eid', 'insert_into_vessel_noon_report', 'get_vessel_id',
           'get_noon_report_base_parameter']


def get_all_eid(conn, message):
    message.rows_eid = fetch_rows(conn, params={
    }, sql_stmt=sql_scripts['get_all_eid'])


def get_noon_report_base_parameter(conn, message):
    message.rows_noon_report_base_parameters = fetch_rows(conn, params={
    }, sql_stmt=sql_scripts['get_noon_report_base_parameters'])


def insert_many_eid(conn, message):
    params = []
    for eid in message.unread_eids:
        params.append({'e_id': eid, 'inserted_at': str(get_utc_timestamp())})
    insert_rows(conn, params=params, sql_stmt=sql_scripts['insert_into_eid'])


def insert_into_vessel_noon_report(conn, data):
    insert_rows(conn, params=data, sql_stmt=sql_scripts['insert_vessel_noon_report'])


def get_vessel_id(conn, vessel_name, message):
    message.row_vessel_id = fetch_row(conn, params={
        'vessel_name': vessel_name
    }, sql_stmt=sql_scripts['get_vessel_id'])
