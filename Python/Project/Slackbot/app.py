from flask import *
from flask_restful import *
from resources.index import Index
from resources.msgslack import Send_Message
app = Flask(__name__)
api = Api(app)



@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")

api.add_resource(Index , '/')
api.add_resource(Send_Message , '/msg')

if __name__ == '__main__':
    app.run(debug=True)