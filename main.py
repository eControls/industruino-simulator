import properties from properties
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connection succeeded !")
    client.subscribe("update/{}".format(properties.app_id), 1)

def on_message(client, userdata, msg):
    print("Received message : {}".format(msg))

if __name__ : "__main__" :
    print("Bonjour.")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(properties.broker_url, properties.broker_port, 60)

