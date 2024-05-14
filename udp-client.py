import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
# SOCK_DGRAM specific for UDP connections
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
# Because UDP is a connectionless protocol, there is no call to "connect()" beforehand
client.sendto(b"AAABBBCCC", (target_host, target_port))


data, addr = client.recvfrom(4096)

# it returns both the data and the details of the remote host and port.
# recvfrom() is used to receive UDP data back
client.close()

print(data)
