import socket

from cv2 import IMWRITE_WEBP_QUALITY

# take the server name and port name

host = 'local host'
port = 8000
ip = input("what is the remote server's IP? \n")

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect((ip, port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message
# string are not empty
while msg:
	print('Received:' + msg.decode())
	msg = s.recv(1024)

# disconnect the client
s.close()
