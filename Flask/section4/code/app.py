from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required


from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'crack'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # JWT creates a new end-point /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @jwt_required()
    def get(self, name):
        # next will return the first item found by the lambda function. Also, it can break our program if there are no items left.
        # added None to avoid that
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = Item.parser.parse_args()

        # if an item exists and the item is not None
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # To get the json payload with a body attached to it
        # request.get_json (Force = True) means we do not need content type header
        # request.get_json (silent = True) doesn't give an error. Returns null in case of an error
        # data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)
