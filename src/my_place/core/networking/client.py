import socket

class Client:
    def __init__(self, address='127.0.0.1', port=40674):
        self.port = port
        self.address = address
        self.socket = socket.socket()
        
        
    def connect(self):
        self.socket.connect((self.address, self.port))
        # receive data from the server
        print(self.socket.recv(1024))

        # close the connection
        self.socket.close()