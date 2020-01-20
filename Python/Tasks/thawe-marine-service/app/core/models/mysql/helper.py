__all__ = ['fetch_rows', 'insert_rows', 'fetch_row', ]


def fetch_rows(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        return cursor.fetchall()


def fetch_row(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        return cursor.fetchone()


def insert_rows(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.executemany(sql_stmt, params)
