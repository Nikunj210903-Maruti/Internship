import pymysql.cursors
from flask import current_app
import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log/logfile.log")
formatter =logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def con():
    try:
        connection = pymysql.connect(host=current_app.config["HOST"],
                                         user=current_app.config["USER"],
                                         password=current_app.config["PASSWORD"],
                                         db=current_app.config["DATABASE_NAME"],
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        logger.debug("Connected to database successfullly")
        return connection
    except Exception as e:
        print(e)
        logger.error("Did not connected to database.")
        return None