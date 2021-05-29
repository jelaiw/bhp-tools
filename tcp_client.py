import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object.
# See https://docs.python.org/3/library/socket.html#creating-sockets.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client.
# See https://docs.python.org/3/library/socket.html#socket.socket.connect.
client.connect((target_host, target_port))

# Send some data.
# See https://docs.python.org/3/library/socket.html#socket.socket.send.
# See https://docs.python.org/3/reference/lexical_analysis.html#strings.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data.
# See https://docs.python.org/3/library/socket.html#socket.socket.recv.
response = client.recv(4096)

# See https://docs.python.org/3/library/stdtypes.html#bytes.decode.
print(response.decode())
client.close()
