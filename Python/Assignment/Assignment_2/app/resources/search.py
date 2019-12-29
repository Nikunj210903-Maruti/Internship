from flask_restful import Resource , fields , marshal_with
from ..common.utils import get_logger ,output_html,check_expire_time,toLocal
from flask import render_template,request , current_app
from ..database.connection import con
from ..database.querie import select

data={
        "name": fields.String,
        "category": fields.String,
        "quantity": fields.Integer,
        "expiry_time": fields.String,
        "id": fields.Integer,
        "is_expired": fields.Boolean,
        "image": fields.String
        }

model =  {
    "items" :fields.List(fields.Nested(data)),
    "error":fields.String
}

class Search(Resource):
    def get(self):
        pass

    @marshal_with(model)
    def post(self):
        logger = get_logger()
        search_by = request.form['search_by']
        timezone = request.form['timezone']
        credential = request.form['credential']
        print(search_by,credential)
        try:
            connection = con()
            if connection:
                result = select(connection,search_by,credential)
                logger.debug("searched inventory by" +  search_by)
                print("result",result)
                logger.info("Inventory : ",result)
                if len(result) > 0:
                    for inventory in result:
                        if check_expire_time(timezone, inventory["expiry_time"]):
                            inventory["is_expired"] = 1
                        inventory["expiry_time"] = toLocal(inventory["expiry_time"], timezone)
                        inventory["expiry_time"] = str(inventory["expiry_time"])
                        inventory["manufacturing_time"] = str(inventory["manufacturing_time"])
                    data = {"items": result}
                    print(data)
                    return data
                else:
                    raise Exception("Inventory does not found")
            else:
                raise Exception("Did not connected to database")

        except Exception as e:
            #logger.error("Error : ", str(e))
            data = {"items": [],"error":str(e)}
            return data

