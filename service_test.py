import socket

port = 22
service = socket.getservbyport(port)
print(service)
