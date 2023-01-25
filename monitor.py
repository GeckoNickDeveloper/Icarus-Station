import paho.mqtt.client as mqtt
import time
import struct
import binascii
import array
from datetime import datetime


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	
	#client.subscribe("/icarus/monitoring/mpu6050")
	#client.subscribe("/icarus/monitoring/bh1750")
	client.subscribe("/icarus/telemetry", qos=0)
	client.subscribe("/icarus/luminosity", qos=0)
	client.subscribe("/icarus/terrain", qos=0)
	print("Connected...\n")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	#print("\n")
	#if msg.topic == "/icarus/telemetry":
	#a,b,c,d,e,f,g,h,i = struct.unpack("!9f", msg.payload)
	#floats = [a,b,c,d,e,f,g,h,i]
	#bytes = binascii.hexlify(msg.payload)
	#a,b,c,d,e,f,g,h,i = struct.unpack("!9f", bytes)
	#floats = [a,b,c,d,e,f,g,h,i]

	#binary_data = array.array('i', [1, 2, 3, 4, 5]).tobytes()

	# Crea un array di interi a partire dalla stringa binaria
	#int_array = array.array('i')
	#int_array.frombytes(binary_data)
#	floats = struct.unpack('<9f', msg.payload)
	#print(msg.payload)
	#print(binascii.hexlify(msg.payload))
#	print(floats)
#	print("Pos " + str(floats[0:2]) + ", Vel " + str(floats[3:5]) + ", Orientation " + str(floats[6:8]))
	if msg.topic == "/icarus/telemetry":
		tlm = struct.unpack('<fffffffff', msg.payload)
		print(f"Position [{tlm[0]}, {tlm[1]}, {tlm[2]}]")
		print(f"Velocity [{tlm[3]}, {tlm[4]}, {tlm[5]}]")
		print(f"Orientation [{tlm[6]}, {tlm[7]}, {tlm[8]}]\n")
	elif msg.topic == "/icarus/luminosity":
		#print(len(msg.payload))
		lux = struct.unpack('<f', msg.payload)
		print(f"Luminosity [{lux[0]}]\n")
	elif msg.topic == "/icarus/terrain":
		trn = struct.unpack('<f', msg.payload)
		print(f"Terrain [{trn[0]}]\n")




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
