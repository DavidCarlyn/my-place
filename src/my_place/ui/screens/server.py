from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App

from my_place.core.networking.interface import NetworkInterface

class ServerLoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(
            orientation="vertical",
            size_hint=[0.7, 0.5],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding=5,
            spacing=10,
        )
        
        ## SERVER PART
        
        # Username input
        server_username_input_layout = BoxLayout(orientation="horizontal")
        server_username_input_lbl = Label(text="Username:")
        self.server_username_text_input = TextInput(multiline=False)
        server_username_input_layout.add_widget(server_username_input_lbl)
        server_username_input_layout.add_widget(self.server_username_text_input)
        
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
            text = "Host Server",
            font_size=24,
        )
        self.host_server_btn.bind(on_press=self.host_server)
        
        layout.add_widget(server_username_input_layout)
        layout.add_widget(server_port_input_layout)
        layout.add_widget(self.host_server_btn)
        
        self.add_widget(layout)
        
    def host_server(self, instance):
        try:
            port = int(self.server_port_text_input.text)
            username = self.server_username_text_input.text
            username = "UNKNOWN" if username == "" else username
        except Exception as e:
            print(e)
            return
        
        network : NetworkInterface = App.get_running_app().network
        network.setup_server(username=username, port=port, num_connections=10)
        self.go_to_chat_screen()
        
    def go_to_chat_screen(self):
        app = App.get_running_app()
        app.network.subscribe_to_messages(app.screen_manager.chat_screen.add_chat_item)
        
        app.root.current = "chat"