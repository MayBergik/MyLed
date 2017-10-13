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
"""
client = paho.Client()
client.username_pw_set(MQTT_USER, MQTT_PWD)
client.connect(MQTT_HOST, MQTT_PORT)
client.publish("topic/test", "My message")
client.disconnect()
"""
app = Flask(__name__)

#Default
@app.route('/')
def helloWorld():
    logging.warning("helloWorld()")
    return "Hello, World!"

#Get request
@app.route('/webhook', methods=['GET'])
def verify():
    """webhook api"""
    logging.warning("verify()")
    return request.args.get('hub.challenge')

#Post request
@app.route('/', methods=['POST'])
def postman():
    jsonDictionary = request.get_json()
    logging.warning(jsonDictionary["name"])
    return "post"

#Post request
@app.route('/webhook', methods=['POST'])
def facebookWebHook():
    jsonDictionary = request.get_json()
    logging.warning("facebookWebHook()" + str(jsonDictionary))

    if jsonDictionary['entry'][0]['changes'][0]['value']['item'] == 'like':
        client = paho.Client()
        client.username_pw_set(MQTT_USER, MQTT_PWD)
        client.connect(MQTT_HOST, MQTT_PORT)
        client.publish("topic/test", "LIKE by (user ID:) " + jsonDictionary['user_id'])
        client.disconnect()
    return ""

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))