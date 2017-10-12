#!flask/bin/python
import os
import logging
from flask import request
from flask import Flask
import paho.mqtt.client as paho

MQTT_HOST = os.environ.get("MQTT_HOST", '')
MQTT_USER = os.environ.get("MQTT_USER", '')
MQTT_PWD = os.environ.get("MQTT_PWD", '')
MQTT_PORT = int(os.environ.get("MQTT_PORT", 5001))

client = paho.Client()
client.username_pw_set(MQTT_USER, MQTT_PWD)
client.connect(MQTT_HOST, MQTT_PORT)
client.publish("topic/test", "My message")
client.disconnect()

app = Flask(__name__)


#Get request
@app.route('/', methods=['GET'])
def helloWorld():
    return "Hello, World!"

#Post request
@app.route('/', methods=['POST'])
def facebookWebHook():
    jsonDictionary = request.get_json()
    logging.warning(jsonDictionary["name"])
    return "Post!"

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))