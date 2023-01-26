import paho.mqtt.client as mqtt
from datetime import datetime
import time
import hashlib
import random
import logging

# Config
log_name = "NET_DELAY_TEST_1s"
logging.basicConfig(filename=log_name, level=logging.INFO, format='%(asctime)s %(message)s')

#event_delay = 0.1 # seconds

def hash_string(string):
	# Crea l'oggetto hash utilizzando l'algoritmo SHA-256
	h = hashlib.sha256()
	# Aggiorna l'oggetto hash con la stringa da criptare
	h.update(string.encode('utf-8'))
	# Restituisci il risultato dell'hashing in forma di stringa esadecimale
	return h.hexdigest()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	#client.publish("/icarus/command", "ciao!")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	t = datetime.now()
	print("[" + str(t) + "] " + str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


cmds = [[0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]
, [0, 0, 0, 0, 0]
, [0, 0, 255, 0, 0]]


i = 0
# [Testing] Station code
try:
	while True:
		if client.is_connected() == False:
			client.connect("mqtt.eclipseprojects.io", 1883)

		if i == 100:
			break
		
		client.publish("/icarus/command", bytes(cmds[i]))

		# Delay readings
		delay = 2 # Seconds
		time.sleep(delay)
		print("OK ", i)
		i += 1
except KeyboardInterrupt as e1:
	print("Terminato dall'utente")
except Exception as e:
	print("Unexpected Exception")
 