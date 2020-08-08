import socket

# Configure Socket and Establish Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# Receive message from Server
msg = s.recv(1024)
print(msg.decode("utf-8"))

# Send message to Server
s.send(bytes("Hi Server! I'm your client", "utf-8 "))
