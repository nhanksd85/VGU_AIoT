print("Hello AIoT")
import sys
from Adafruit_IO import MQTTClient
from simple_ai import *
import time

AIO_FEED_ID = ["actuator1","actuator2"]
AIO_USERNAME = "BBC_IoT"
AIO_KEY = "aio_QYth850SuWaXh20PWdD20n0W5XSN"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Payload: " + payload)


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    image_capture()
    ai_result = image_detector()
    client.publish("visiondetection", ai_result)