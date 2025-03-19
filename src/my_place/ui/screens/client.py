from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App

from my_place.core.networking.interface import NetworkInterface

class ClientLoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(
            orientation="vertical"
        )
        
        ## CLIENT PART
        
        # Username input
        client_username_input_layout = BoxLayout(orientation="horizontal")
        client_username_input_lbl = Label(text="Username:")
        self.client_username_text_input = TextInput(multiline=False)
        client_username_input_layout.add_widget(client_username_input_lbl)
        client_username_input_layout.add_widget(self.client_username_text_input)
        layout.add_widget(client_username_input_layout)
        
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
    
    def connect_to_server(self, instance):
        try:
            port = int(self.client_port_text_input.text)
            address = self.client_address_text_input.text
            username = self.client_username_text_input.text
            username = "UNKNOWN" if username == "" else username
        except Exception as e:
            print(e)
            return
        
        network : NetworkInterface = App.get_running_app().network
        network.setup_client(username=username, address=address, port=port)
        self.go_to_chat_screen()
        
    def go_to_chat_screen(self):
        app = App.get_running_app()
        app.network.subscribe_to_messages(app.screen_manager.chat_screen.add_chat_item)
        
        app.root.current = "chat"