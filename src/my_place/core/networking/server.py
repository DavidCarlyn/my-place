import socket
from threading import Thread
from datetime import datetime

class Server:
    def __init__(self, port=40674, num_connections=5):
        self.port = port
        self.num_connections = num_connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.server_socket.bind(('', self.port))
        self.list_of_clients = set()
        self.server_socket.listen(self.num_connections)
        
    def remove(self, connection): 
        if connection in self.list_of_clients: 
            self.list_of_clients.remove(connection) 
    
    def broadcast(self, message, connection):
        for client in self.list_of_clients: 
            if client != connection: 
                try: 
                    client.send(message) 
                except: 
                    client.close() 
                    # if the link is broken, we remove the client 
                    self.remove(client) 
    
    def on_client_connect(self, connection, address): 
 
        # sends a message to the client whose user object is conn 
        connection.send("Welcome to this chatroom!".encode()) 
    
        while True: 
            try: 
                message = connection.recv(2048).decode()
                if message: 
                    """prints the message and address of the 
                    user who just sent the message on the server 
                    terminal"""
                    print("<" + address[0] + "> " + message) 

                    # Calls broadcast function to send message to all 
                    message_to_send = "<" + address[0] + "> " + message 
                    self.broadcast(message_to_send.encode(), connection) 

                else: 
                    """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                    self.remove(connection) 

            except Exception as e: 
                print(e)
            
    def start_client_process(self):
        while True: 
 
            # input message we want to send to the server
            to_send =  input()
            # a way to exit the program
            #if to_send.lower() == 'q':
            #    break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"[{date_now}] {to_send}"
            # finally, send the message
            self.broadcast(to_send.encode(), self.server_socket)
     
    def start(self):
        server_client_process = Thread(target=self.start_client_process)
        server_client_process.daemon = True
        server_client_process.start()
        
        while True: 
 
            """Accepts a connection request and stores two parameters, 
            conn which is a socket object for that user, and addr 
            which contains the IP address of the client that just 
            connected"""
            connection, address = self.server_socket.accept() 
        
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
        
        for client_connection in list(self.list_of_clients):
            self.remove(client_connection)
            
        self.server_socket.close() 
        
