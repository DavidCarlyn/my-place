from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App

from my_place.core.networking.interface import NetworkInterface
from my_place.ui.widgets.custom import ColoredBoxLayout
from my_place.ui.widgets.navigation import BackButton

class ClientLoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = ColoredBoxLayout(
            orientation="vertical",
            size_hint=[0.7, 0.5],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding=5,
            spacing=10,
        )
        
        ## CLIENT PART
        
        # Username input
        client_username_input_layout = BoxLayout(orientation="horizontal")
        client_username_input_lbl = Label(text="Username:", color="black")
        self.client_username_text_input = TextInput(multiline=False, halign="center")
        client_username_input_layout.add_widget(client_username_input_lbl)
        client_username_input_layout.add_widget(self.client_username_text_input)
        layout.add_widget(client_username_input_layout)
        
        # Address input
        client_address_input_layout = BoxLayout(orientation="horizontal")
        client_address_input_lbl = Label(text="Network Address (IP):", color="black")
        self.client_address_text_input = TextInput(multiline=False, halign="center")
        client_address_input_layout.add_widget(client_address_input_lbl)
        client_address_input_layout.add_widget(self.client_address_text_input)
        layout.add_widget(client_address_input_layout)
        
        # Port input
        client_port_input_layout = BoxLayout(orientation="horizontal")
        client_port_input_lbl = Label(text="Port:", color="black")
        self.client_port_text_input = TextInput(text="40674", multiline=False, halign="center")
        client_port_input_layout.add_widget(client_port_input_lbl)
        client_port_input_layout.add_widget(self.client_port_text_input)
        layout.add_widget(client_port_input_layout)
        
        # Connect to Server
        self.connect_to_server_btn = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            text = "Connect to Server",
            font_size=24,
        )
        self.connect_to_server_btn.bind(on_press=self.connect_to_server)
        layout.add_widget(self.connect_to_server_btn)
        
        # Add layout to screen
        self.add_widget(layout)
        
        # Back Button
        bbtn = BackButton(screen_name="login")
        self.add_widget(bbtn)
    
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