import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log/logfile.log")
formatter =logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def insert(table,connection,*data):
    try:
        with connection.cursor() as cursor:
            if table=="user":
                sql = "INSERT INTO user (Username,Email,Password,Photo) VALUES (%s, %s, %s,%s)"
            if table == "user_order":
                sql = "INSERT INTO user_order (Username,Cake,Chocolate) VALUES (%s, %s, %s)"
            cursor.execute(sql,tuple(data))
        connection.commit()
        connection.close()
        logger.debug("data inserted successfully to table : " + table)
    except Exception as e:
        logger.error("There is an error while inserting into table : " + table)

def select(table,connection,*data):
    try:
        with connection.cursor() as cursor:
            if table=="user":
                sql = "SELECT `Username`, `Password` FROM "+table+" WHERE `Username`=%s and `Password`=%s"
            elif table=="items":
                sql = "SELECT * FROM " + table
            cursor.execute(sql, tuple(data))
            result = cursor.fetchall()
            logger.debug("data fetched successfully from table : " + table)
        return result
    except Exception as e:
        logger.error("There is an error while fetching data from table : " + table)
        return None
