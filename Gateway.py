#!flask/bin/python
import logging
from flask import request
from flask import Flask
import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="", clean_session=True, userdata=None, transport="tcp")
client.connect()
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

if __name__ == '__main__':
    app.run(debug=True)
