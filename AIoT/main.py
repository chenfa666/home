import sys
import time
import random
from uart import *
from Adafruit_IO import MQTTClient


AIO_FEED_ID = [ "device_light", "remote", "door_switch"]
AIO_USERNAME = "chenfa666"
AIO_KEY = "aio_aSDr22YOQ0IUEms6qH3pCfYAarQC"


def connected(client):
    for topic in AIO_FEED_ID:
        client.subscribe(topic)
    print("Connected successfully...")


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed successfully...")


def disconnected(client):
    print("disconnected...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Data received: " + payload + ", feed id:" + feed_id)
    if feed_id == 'device_light':
        writeData(payload)
    elif feed_id == 'remote':
        writeData(payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    readSerial(client)
    pass
