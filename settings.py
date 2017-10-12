import os

MQTT_HOST = os.environ.get("MQTT_HOST", '')
MQTT_USER = os.environ.get("MQTT_USER", '')
MQTT_PWD = os.environ.get("MQTT_PWD", '')
MQTT_PORT = int(os.environ.get("MQTT_PORT", 5001))
#MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
#WEB_PORT = int(os.environ.get("PORT", 5000))