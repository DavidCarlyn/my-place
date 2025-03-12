from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App

from my_place.core.networking.interface import NetworkInterface

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(
            orientation="vertical"
        )
        
        ## SERVER PART
        
        # Port input
        server_port_input_layout = BoxLayout(orientation="horizontal")
        server_port_input_lbl = Label(text="Port:")
        self.server_port_text_input = TextInput(text="40674", multiline=False)
        server_port_input_layout.add_widget(server_port_input_lbl)
        server_port_input_layout.add_widget(self.server_port_text_input)
        
        # Host Server btn
        self.host_server_btn = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            size_hint=(.3, .3),
            text = "Host Server",
            font_size=24,
        )
        self.host_server_btn.bind(on_press=self.host_server)
        
        layout.add_widget(server_port_input_layout)
        layout.add_widget(self.host_server_btn)
        
        
        ## CLIENT PART
        
        # Address input
        client_address_input_layout = BoxLayout(orientation="horizontal")
        client_address_input_lbl = Label(text="Network Address (IP):")
        self.client_address_text_input = TextInput(multiline=False)
        client_address_input_layout.add_widget(client_address_input_lbl)
        client_address_input_layout.add_widget(self.client_address_text_input)
        layout.add_widget(client_address_input_layout)
        
        # Port input
        client_port_input_layout = BoxLayout(orientation="horizontal")
        client_port_input_lbl = Label(text="Port:")
        self.client_port_text_input = TextInput(text="40674", multiline=False)
        client_port_input_layout.add_widget(client_port_input_lbl)
        client_port_input_layout.add_widget(self.client_port_text_input)
        layout.add_widget(client_port_input_layout)
        
        # Connect to Server
        self.connect_to_server_btn = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            size_hint=(.3, .3),
            text = "Connect to Server",
            font_size=24,
        )
        self.connect_to_server_btn.bind(on_press=self.connect_to_server)
        layout.add_widget(self.connect_to_server_btn)
        
        self.add_widget(layout)
        
    def host_server(self, instance):
        try:
            port = int(self.server_port_text_input.text)
        except Exception as e:
            print(e)
            return
        
        network : NetworkInterface = App.get_running_app().network
        network.setup_server(port=port, num_connections=10)
        self.go_to_chat_screen()
    
    def connect_to_server(self, instance):
        try:
            port = int(self.client_port_text_input.text)
            address = self.client_address_text_input.text
        except Exception as e:
            print(e)
            return
        
        network : NetworkInterface = App.get_running_app().network
        network.setup_client(address=address, port=port)
        self.go_to_chat_screen()
        
    def go_to_chat_screen(self):
        app = App.get_running_app()
        app.network.subscribe_to_messages(app.screen_manager.chat_screen.add_chat_item)
        
        app.root.current = "chat"