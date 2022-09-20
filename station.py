import math
import socket
from numpy import integer
import pygame

# ax 0 -> dx/sx
# ax 1 -> up/dw
# ax 2 -> rot_dx/rot_sx
# ax 3 -> throttle [red = -1 (max), white = 1 (min)]

hst = "Host: " + socket.gethostname() + "\t\t(" + socket.gethostbyname(socket.gethostname()) + ")"
print(hst)

# Init
pygame.display.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
id = joystick.get_instance_id()

#
# create an INET, STREAMing socket
#
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 42069))
# become a server socket
serversocket.listen(1)

client, address = serversocket.accept()
try:
	while True:
		ev = pygame.event.wait()
		if ev.type == pygame.JOYAXISMOTION:
			data = []
			#data.append(hex((joystick.get_axis(0) + 1.0) * 127.5))
			#a = (joystick.get_axis(0) + 1.0) * 127.5
			#print("A: {0}".format(integer(a)))
			
			#print('type:', type(a).__name__)  
			#print(hex(math.floor(a)))

			data.append(int(((joystick.get_axis(0) + 1.0) * 127.5)))
			data.append(int(((joystick.get_axis(1) + 1.0) * 127.5)))
			data.append(int(((joystick.get_axis(2) + 1.0) * 127.5)))
			data.append(int(((joystick.get_axis(3) - 1.0) * -127.5)))
			
			data.append(0)
			#print([0xc4, 0xf3, 0x45, 0x7a, 0xde].encode())

			#data.append(0x00)
			#data.append(0x00)
			#data.append(0x00)
			#data.append(0x00)
			#data.append(0x00)
			print(bytes(data))
			client.send(bytes(data))
except Exception as e:
	print(e)