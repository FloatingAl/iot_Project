import paho.mqtt.client as mqtt
from flask import Flask, request, json
from flask_restful import Resource, Api

broker_address="192.168.1.0" # needs to be changed per usage

app = Flask(__name__)
api = Api(app)

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.connect(broker_address)

user_info = { username : "Username",
              password : "password" }

orders = { location     : "123 Everyday Dr.", 
           resturant    : "Burger King",
           orders       : "1",
           delivery     : "Delivery" }

class User_Inputs(Resource):

    def get(self):
        pass

    def post(self):
        pass

class Food_Inputs(Resource):

    def get(self):
        pass
    
    def post(self):
        pass

client.loop_start()

if __name__ == "__main__"
    app.run(debug=True)

client.loop_start()