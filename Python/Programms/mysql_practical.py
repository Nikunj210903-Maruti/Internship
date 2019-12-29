import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             db='db',
                             password='Nikunj210903',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    
    connection.commit()

    with connection.cursor() as cursor:
        
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
except:
    print("error")
finally:
    connection.close()
