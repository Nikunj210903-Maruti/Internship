def insert(connection, name, category, e_time, m_time, quantity, image_path):
    with connection.cursor() as cursor:
        sql = "INSERT INTO item (name,category,image,quantity,expiry_time,manufacturing_time) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(sql, (name, category, image_path, quantity, e_time, m_time))
    connection.commit()
    connection.close()

def update(connection, inventory_id , quantity):
    with connection.cursor() as cursor:
        sql = "UPDATE item SET quantity =" + quantity + " WHERE id =" + inventory_id
        cursor.execute(sql, ())
        count = cursor.rowcount
    connection.commit()
    connection.close()
    return count

def select(connection,key,value):
    print(key,value)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM item where " + key +"=%s"
        cursor.execute(sql, (value))
        print(sql)
        result = cursor.fetchall()
        connection.close()
        print(result)
        return result

def delete(connection,id):
    print(type(id))
    with connection.cursor() as cursor:
        sql = "DELETE FROM item where id=%s"
        cursor.executemany(sql,id)
        connection.commit()
    connection.close()





