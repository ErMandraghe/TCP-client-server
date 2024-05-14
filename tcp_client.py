import socket

HOST = '127.0.0.1'
PORT = 9998

#creates a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((HOST, PORT))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receinve data back
response = client.recv(4096)

print(response.decode())
client.close()


'''
AF_INET parameter specifies IPv4 addr/host.
SOCK_STREAM is TCP specific, not UDP.
'''
