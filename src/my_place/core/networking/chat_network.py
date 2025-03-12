class ChatNetwork:
    def __init__(self):
        self.socket = None
        self.on_message_recieve_subscribers = []
    
    def subscribe_to_on_message_recieve(self, func):
        self.on_message_recieve_subscribers.append(func)
            
    def send(self, message):
        if self.socket:
            self.socket.send(message.encode())