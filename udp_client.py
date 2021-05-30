import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object.
# See https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data.
# See https://docs.python.org/3/library/socket.html#socket.socket.sendto.
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Receive some data.
# See https://docs.python.org/3/library/socket.html#socket.socket.recvfrom.
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
