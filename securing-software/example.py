import socket


address = "127.0.0.1"
port = 12321

s = socket.socket()
s.connect((address, port))
data = s.recv(1024)