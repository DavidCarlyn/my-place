import socket

class Server:
    def __init__(self, port=40674):
        self.port = port
        self.socket = socket.socket()
        
        self.socket.bind(('', self.port))
        
    def listen(self):
        self.socket.listen(5)
        
        while True:
            # Establish connection with client.
            c, addr = self.socket.accept()
            print ('Got connection from', addr )

            # send a thank you message to the client.
            c.send(b'Thank you for connecting')

            # Close the connection with the client
            c.close()
