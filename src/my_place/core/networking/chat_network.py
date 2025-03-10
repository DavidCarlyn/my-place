from datetime import datetime

class ChatNetwork:
    def __init__(self):
        self.socket = None
        self.on_message_recieve_subscribers = []
    
    def subscribe_to_on_message_recieve(self, func):
        self.on_message_recieve_subscribers.append(func)
            
    def send(self, message):
        if self.socket:
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"[{date_now}] {message}"
            self.socket.send(to_send.encode())