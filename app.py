from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'
items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'type': data['type'], 'address' : data['address'], 'state' : data['state']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Home, '/')

app.run(port=5000, debug=True)
