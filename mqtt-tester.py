import paho.mqtt.client as mqtt
import time
from datetime import datetime


def get_time():
	#t = time.time()
	#t_ms = int(t * 1000)
	##print(f"The current time in milliseconds: {t_ms}")
	#datetime.fromtimestamp(t_ms/1000.0)
	#return t_ms
	now = datetime.now()
	return now



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	t = get_time()
	payload = "abced"
	print("[" + str(t) + "] " + str(payload))
	
	client.publish("/icarus/command", str(payload))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	t = get_time()
	print("[" + str(t) + "] " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()