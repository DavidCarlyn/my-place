from my_place.core.networking.client import Client
from my_place.core.networking.server import Server

class NetworkInterface:
    def __init__(self):
        self.network = None
        self.username = "UNKNOWN"
            
    def setup_client(self, username: str, address: str, port: int):
        self.username = username
        if not self.network:
            self.network = Client()
            self.network.connect(address=address, port=port)
        
    def setup_server(self, username: str, port: int = None, num_connections=10):
        self.username = username
        if not self.network:
            self.network = Server(port=port, num_connections=num_connections)
            self.network.start()
            
    def subscribe_to_messages(self, func):
        self.network.subscribe_to_on_message_recieve(func)
        
    def send(self, message):
        if not self.network:
            return
        message = f"[{self.username}]: {message}"
        
        self.network.send(message)
        
    def close(self):
        self.network.close()