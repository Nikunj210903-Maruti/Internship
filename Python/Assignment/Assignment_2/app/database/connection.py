def con():
    import pymysql.cursors
    from flask import current_app
    from ..common.utils import get_logger
    logger=get_logger()
    connection = pymysql.connect(host=current_app.config["HOST"],
                                         user=current_app.config["USER"],
                                         password=current_app.config["PASSWORD"],
                                         db=current_app.config["DATABASE_NAME"],
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
    logger.debug("Connected to database successfully")
    return connection
