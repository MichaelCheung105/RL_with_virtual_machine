import socket


class SocketCommunicator:
    def __init__(self, socket_type: str, host: str, port: int):
        self.socket_type = socket_type
        self.server_socket, self.client_socket = None, None

        if self.socket_type == 'server':
            self.initiate_server(host, port)
        elif self.socket_type == 'client':
            self.initiate_client(host, port)
        else:
            raise Exception("Incorrect socket type!")

    def initiate_server(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        self.await_client()

    def await_client(self):
        # Wait for client to connect and confirm the connection
        print("Waiting for client to connect")
        self.client_socket, address = self.server_socket.accept()
        print("Connection to client {0} established".format(address))

        # Greetings to client
        self.client_socket.send(bytes("Hi Client! I'm your server :)", "utf-8 "))

        # Check response from client
        message_from_client = self.client_socket.recv(1024).decode("utf-8")
        print("Message received from client: {0}".format(message_from_client))

    def initiate_client(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server(host, port, retry_count=10)

    def connect_to_server(self, host, port, retry_count=10):
        # Try to connect to server
        while retry_count > 0:
            try:
                print("Connecting to server {0}".format(host))
                self.client_socket.connect((host, port))
                print("Connection to server {0} established".format(host))
                break
            except Exception as e:
                print("Fail to connect to server {0}".format(host))
                print(e)
                retry_count -= 1
                print("Retry connection. Retry count remained: {0}".format(retry_count))

        # Check response from server
        message_from_server = self.client_socket.recv(1024).decode("utf-8")
        print("Message received from server: {0}".format(message_from_server))

        # Greetings to server
        self.client_socket.send(bytes("Hi Server! I'm your client :)", "utf-8 "))

    def send_message(self, message):
        self.client_socket.send(message)

    def receive_message(self):
        message = self.client_socket.recv(1024)
        return message
