"""Handle the MySql Database Connection"""
import pymysql
from flask import current_app

__all__ = ['MysqlDatabaseHandler']


def connect():
    conn = pymysql.connect(user=current_app.config['MYSQL_DATABASE_USER'],
                           password=current_app.config['MYSQL_DATABASE_PASSWORD'],
                           host=current_app.config['MYSQL_DATABASE_HOST'],
                           database=current_app.config['MYSQL_CORE_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor,
                           charset='utf8mb4')
    return conn


def close(conn):
    if conn is not None and conn.open:
        conn.close()


class MysqlDatabaseHandler(object):
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        close(self.conn)
