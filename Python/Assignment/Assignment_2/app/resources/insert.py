from flask_restful import Resource
from ..common.utils import get_logger ,validation ,read_id ,write_id,toCst,output_html
from flask import render_template,request
import os
from ..database.connection import con
from ..database.querie import insert

class Insert(Resource):
    def get(self):
       pass

    def post(self):
        logger=get_logger()
        validated = validation(request.files,request.form)
        print(validated)
        try:
            if not validated:
                raise Exception("Please enter all data and upload image in PNG form only")
            id = read_id()
            name = request.form['name']
            category = request.form["category"]
            e_time = request.form['e_time']
            m_time = request.form['m_time']
            quantity = request.form['quantity']
            photo = request.files['photo']

            m_time = toCst(m_time)
            e_time = toCst(e_time)

            path = os.path.dirname(os.path.abspath(__file__))
            filename = "image" + str(id) + '.' + photo.filename.rsplit('.', 1)[1].lower()
            image_path = os.path.join(os.path.join(path, '..\static\images'), filename)
            image_path = image_path.replace("resources\..\\", "")
            photo.save(image_path)

            connection = con()
            if connection:
                insert(connection, name, category, e_time, m_time, quantity, image_path)
                logger.debug("Inventory added successfully")
                write_id(int(id) + 1)
                data = {"message": "You Entered data successfully and image_path is : " + image_path, "error": None}
                return data
            else:
                raise Exception("Did not connected to database")

        except Exception as e:
            # logger.error("Error : ", str(e))
            data = {"message": None, "error": str(e)}
            return data





