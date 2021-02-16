from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import requests
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'nostradamus'

jwt = JWT(app, authenticate, identity) # /auth

device1 ={
            "name": "ESP1",
            "type": "ESP32",
            "address": "192.168.1.6",
            "state": "ON"}
device2 = {
            "name": "ESP2",
            "type": "ESP32",
            "address": "192.168.1.7",
            "state": "ON"}
items = [device1, device2]

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'type': data['type'], 'address' : data['address'], 'state' : data['state']}
        items.append(item)
        return item, 201

    @jwt_required()
    def put(self, name):
        data = request.get_json()
        device_data = {}

        if not next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' does not exists".format(name)}, 400

        for item in items:
            if item['name'] == name:
                url = 'http://' + item['address']
                d = 'relayon'
                if(data['state'] == 'OFF'):
                    d = 'relayoff'

                param = d
                r = requests.get(url, params=param)
                device_data = item
                device_data['state'] = data['state']
                item['state'] = data['state']

        return data, 201

    @jwt_required()
    def delete(self, name):
        data = request.get_json()
        device_data = {}

        if not next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' does not exists".format(name)}, 400

        for item in items:
            if item['name'] == name:
                items.remove(item)

        return {'message' : "{} was successfully removed".format(name)}, 201



class ItemList(Resource):
    def get(self):
        return {'items': items}

class Home(Resource):
    ## IDEA: Responsive web designe for n-number of devices. 
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Home, '/')

app.run(port=5000, debug=True)
