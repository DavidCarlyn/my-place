import socket
from threading import Thread

from my_place.core.networking.chat_network import ChatNetwork

class Server(ChatNetwork):
    def __init__(self, port=40674, num_connections=5):
        super().__init__()
        self.port = port
        self.num_connections = num_connections
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.socket.bind(('', self.port))
        self.list_of_clients = set()
        self.socket.listen(self.num_connections)
        
    def remove(self, connection): 
        if connection in self.list_of_clients: 
            self.list_of_clients.remove(connection) 
    
    def send(self, message):
        self.broadcast(message.encode(), self.socket)
    
    def broadcast(self, message, connection):
        for client in list(self.list_of_clients): 
            if client != connection: 
                try: 
                    client.send(message) 
                except: 
                    client.close() 
                    # if the link is broken, we remove the client 
                    self.remove(client) 
                    
    def _handle_message(self, message, connection, address):
        print(message)
        for func in self.on_message_recieve_subscribers:
            func(message)
        
        self.broadcast(message.encode(), connection) 
    
    def on_client_connect(self, connection, address): 
 
        # sends a message to the client whose user object is conn 
        connection.send("Welcome to this chatroom!".encode()) 
    
        while True: 
            try: 
                message = connection.recv(2048).decode()
                if message:
                    self._handle_message(message, connection, address)
                else: 
                    """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                    self.remove(connection) 

            except Exception as e: 
                print(e)
            
    def listen_for_client_connections(self):
        while True: 
 
            """Accepts a connection request and stores two parameters, 
            conn which is a socket object for that user, and addr 
            which contains the IP address of the client that just 
            connected"""
            connection, address = self.socket.accept() 
        
            """Maintains a list of clients for ease of broadcasting 
            a message to all available people in the chatroom"""
            self.list_of_clients.add(connection) 
        
            # prints the address of the user that just connected 
            print (address[0] + " connected")
        
            # creates and individual thread for every user 
            # that connects
            thread_process = Thread(target=self.on_client_connect, args=(connection, address))
            thread_process.daemon = True
            thread_process.start()
     
    def start(self):
        server_client_process = Thread(target=self.listen_for_client_connections)
        server_client_process.daemon = True
        server_client_process.start()
        
        
    def close(self):
        for client_connection in list(self.list_of_clients):
            self.remove(client_connection)
            
        self.socket.close() 
        
