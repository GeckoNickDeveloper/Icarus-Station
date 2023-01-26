import paho.mqtt.client as mqtt
from datetime import datetime
import time
import struct
import pygame

# Command
class Command:
	def __init__(self):
		self.__pitch = 0
		self.__roll = 0
		self.__yaw = 0
		self.__throttle = 0
		self.__aux = 0
	
	def set_pitch(self, val):
		"""
			Val: float number between -1 and 1
		"""
		self.__pitch = int(((val + 1.0) / 2) * 255)
	
	def set_roll(self, val):
		"""
			Val: float number between -1 and 1
		"""
		self.__roll = int(((val + 1.0) / 2) * 255)
	
	def set_yaw(self, val):
		"""
			Val: float number between -1 and 1
		"""
		self.__yaw = int(((val + 1.0) / 2) * 255)
	
	def set_throttle(self, val):
		"""
			Val: float number between -1 and 1
		"""
		self.__throttle = int(((val - 1.0) / 2) * -255)

	def toggle_aux_flag_light(self):
		if self.__aux & 0x80 == 0:
			self.__aux = self.__aux | 0x80
		else:
			self.__aux = self.__aux & 0x7F
		


	def to_binary(self):
		data = []
		data.append(int(self.__pitch))
		data.append(int(self.__roll))
		data.append(int(self.__yaw))
		data.append(int(self.__throttle))
		data.append(int(self.__aux))

		return bytes(data)




# Init Pygame
pygame.display.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
id = joystick.get_instance_id()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	client.subscribe("/icarus/telemetry", qos=0)
	client.subscribe("/icarus/luminosity", qos=0)
	client.subscribe("/icarus/terrain", qos=0)

	print("Connected with result code " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
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

#client.connect("mqtt.eclipseprojects.io", 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()



# Station code
try:
	cmd = Command() # Create command object

	while True:
		if client.is_connected() == False:
			client.connect("mqtt.eclipseprojects.io", 1883)

		pub = False
		ev = pygame.event.wait()
		if ev.type == pygame.JOYAXISMOTION:
			cmd.set_pitch(joystick.get_axis(1))
			cmd.set_roll(joystick.get_axis(0))
			cmd.set_yaw(joystick.get_axis(2))
			cmd.set_throttle(joystick.get_axis(3))
			pub = True
			
		elif ev.type == pygame.JOYBUTTONDOWN:
			if joystick.get_button(1): # 1 >> Numero 2 sul joystick
				cmd.toggle_aux_flag_light()
				pub = True

		
		if pub:
			client.publish("/icarus/command", cmd.to_binary())
	
		print(cmd.to_binary())
		pygame.event.clear()
except KeyboardInterrupt as e1:
	print("Terminato dall'utente")
except Exception as e:
	print("Unexpected Exception")