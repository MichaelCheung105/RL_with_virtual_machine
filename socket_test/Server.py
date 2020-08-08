import socket

# Configure Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(1)

# Establish Connection
clt, adr = s.accept()
print("Connection to {0} established".format(adr))

# Send message to Client
clt.send(bytes("Hi Client! I'm your server", "utf-8 "))

# Receive message from Client
msg = clt.recv(1024)
print(msg.decode("utf-8"))
