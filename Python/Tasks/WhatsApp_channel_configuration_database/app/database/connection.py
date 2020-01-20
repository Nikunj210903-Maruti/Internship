def con():
    import pymysql.cursors
    from flask import current_app

    connection = pymysql.connect(host=current_app.config["DATABASE_HOST"],
                                         user=current_app.config["DATABASE_USERNAME"],
                                         password=current_app.config["DATABASE_PASSWORD"],
                                         db="Wotnot",
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
    return connection
