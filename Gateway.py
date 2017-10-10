#!flask/bin/python
import os
import logging
from flask import request
from flask import Flask
import paho.mqtt.client as mqtt

#client = mqtt.Client(client_id="", clean_session=True, userdata=None, transport="tcp")
#client.connect("m11.cloudmqtt.com", 13487, 60, )

app = Flask(__name__)

#Get request
@app.route('/', methods=['GET'])
def helloWorld():
    return "Hello, World!"

#Post request
@app.route('/', methods=['POST'])
def facebookWebHook():
    jasonDictionary = request.get_json()
    logging.warning(jasonDictionary["name"])
    return "Post!"

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
