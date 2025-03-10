import socket
from datetime import datetime

from threading import Thread

from my_place.core.networking.chat_network import ChatNetwork

class Client(ChatNetwork):
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def listen_for_messages(self):
        while True:
            message = self.socket.recv(1024).decode()
            print(message)
            for func in self.on_message_recieve_subscribers:
                func(message)
        
    def connect(self, address='127.0.0.1', port=40674):
        print(f"Connecting to: {address}:{port}")
        self.socket.connect((address, port))
        
        thread_process = Thread(target=self.listen_for_messages)
        thread_process.daemon = True
        thread_process.start()
        
    def close(self):
        self.socket.close()
        