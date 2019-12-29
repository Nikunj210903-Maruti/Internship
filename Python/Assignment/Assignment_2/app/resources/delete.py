from flask_restful import Resource
from ..common.utils import output_html ,get_logger
from flask import render_template , request ,json
from ..database.connection import con
from ..database.querie import delete
import os

class Delete(Resource):
    def get(self):
        pass

    def delete(self):
        logger=get_logger()
        items =[]
        for i in json.loads(request.form["total"]):
            if request.form.get(str(i)):
                items.append(i)
        connection = con()
        print(items)
        try:
            if connection:
                delete(connection, items)
                logger.debug("Inventories deleted successfully")
                for i in items:
                    image_name = "../static/images/image" + str(i) +".png"
                    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),  image_name)
                    print(dir_path)
                    os.remove(dir_path)
                    logger.debug("Images deleted successfully from local directory")
                data = {"message": "You deleted Inventories successfully", "error": None}
                return data
            else:
                raise Exception("Did not connected to database")

        except Exception as e:
            # logger.error("Error : ", str(e))
            data = {"message": None, "error": str(e)}
            return data



