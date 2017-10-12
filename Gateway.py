#!flask/bin/python
import os
import logging
from flask import request
from flask import Flask
import paho.mqtt.client as mqtt

client = paho.Client()
client.username_pw_set(Config.MQTT_USER, Config.MQTT_PWD)
client.connect(Config.MQTT_HOST, Config.MQTT_PORT)
client.publish("topic/test", "Hello world!");
client.disconnect();

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
