from flask_restful import Resource
from ..common.utils import output_html ,get_logger
from flask import request ,render_template
from ..database.connection import con
from ..database.querie import update

class Update(Resource):
    def get(self):
       pass

    def put(self):
        logger=get_logger()
        inventory_id = request.form['inventory_id']
        quantity = request.form['quantity']
        connection=con()
        try:
            if connection:
                count = update(connection, inventory_id , quantity)
                if count==0:
                    raise Exception("Inventory_id does not exists")
                logger.debug("updated inventory quantity")
                data = {"message": "You Updated data successfully", "error": None}
                return data
            else:
                raise Exception("Did not connected to database")

        except Exception as e:
            # logger.error("Error : ", str(e))
            data = {"message": None, "error": str(e)}
            return data



