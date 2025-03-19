from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App

from my_place.core.networking.interface import NetworkInterface

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = GridLayout(
            rows=2,
            cols=1,
        )
        
        # Host Server btn
        self.host_server_btn = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            size_hint=(.8, .5),
            text = "Host Server",
            font_size=24,
        )
        self.host_server_btn.bind(on_press=self.go_to_server_login_screen)
        layout.add_widget(self.host_server_btn)
        
        # Connect to Server
        self.connect_to_server_btn = Button(
            background_color=(54/255, 109/255, 150/255, 1),
            background_normal="",
            size_hint=(.8, .5),
            text = "Connect to Server",
            font_size=24,
        )
        self.connect_to_server_btn.bind(on_press=self.go_to_client_login_screen)
        layout.add_widget(self.connect_to_server_btn)
        
        self.add_widget(layout)
        
    def go_to_server_login_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "server-login"
        
    def go_to_client_login_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "client-login"