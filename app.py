from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item

app = Flask(__name__)
api = Api(app)

api.add_resource(Item, '/item/<string:name>')

if __name__ =='__main__':
    app.run(port=5000, debug=True)