from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'crack'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # JWT creates a new end-point /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
