import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(1)
print("start accept")
clt, adr = s.accept()
print("Connection to {0}established".format(adr))
clt.send(bytes("Socket Programming in Python", "utf-8 "))
print("message sent")
msg = clt.recv(1024)
print(msg.decode("utf-8"))