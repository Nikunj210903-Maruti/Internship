from .connection import con
from properties.p import Property
import json
prop = Property()
sql = prop.load_property_files('app/database/sql.properties')

def select_whatsapp_channel_configuration(query , bot_id):
    connection = con()
    with connection.cursor() as cursor:
        sql_stmt = sql[query]
        params={
            "bot_id": bot_id,
        }
        cursor.execute(sql_stmt, params)
        result= cursor.fetchone()
        if result:
            result['created_at'] = str(result['created_at'])
            result['modified_at'] = str(result['modified_at'])
            result['auth_details'] = json.loads(result['auth_details'])
    connection.commit()
    connection.close()
    return result

def insert_whatsapp_channel_configuration_on_duplicate_update(query ,*data):
    connection = con()
    with connection.cursor() as cursor:
        sql_stmt = sql[query]
        params={
            "channel_vendor_id": data[0],
            "bot_id": data[1],
            "bot_phone_number": data[2],
            "webhook_url": data[3],
            "auth_details": data[4],
            "created_at": data[5],
            "created_by": data[6],
            "modified_at": data[7],
            "modified_by": data[8]
        }
        cursor.execute(sql_stmt, params)
    connection.commit()
    connection.close()

def insert_channel_configuration(query ,*data):
    connection = con()
    with connection.cursor() as cursor:
        print(sql[query])
        sql_stmt = sql[query]
        params={
            "bot_lead_id": data[0],
            "channel_id": data[1],
            "status": data[2],
            "created_at": data[3],
            "created_by": data[4],
            "modified_at": data[5],
            "modified_by": data[6]
        }
        cursor.execute(sql_stmt, params)
    connection.commit()
    connection.close()

