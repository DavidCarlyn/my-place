import socket
from datetime import datetime

from threading import Thread

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def listen_for_messages(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            print(message)
        
    def connect(self, address='127.0.0.1', port=40674):
        self.client_socket.connect((address, port))
        # receive data from the server
        print(self.client_socket.recv(1024))
        
        thread_process = Thread(target=self.listen_for_messages)
        thread_process.daemon = True
        thread_process.start()
        
        while True: 
 
            # input message we want to send to the server
            to_send =  input()
            # a way to exit the program
            if to_send.lower() == 'q':
                break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"[{date_now}] {to_send}"
            # finally, send the message
            self.client_socket.send(to_send.encode())

        # close the connection
        self.client_socket.close()
        