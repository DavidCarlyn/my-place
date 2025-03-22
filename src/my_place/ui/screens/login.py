from kivy.uix.anchorlayout import AnchorLayout
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
        button_layout = BoxLayout(
            orientation="vertical",
            size_hint=[0.5, 0.5],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding=5,
            spacing=10,
        )
        
        # Host Server btn
        self.host_server_btn = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            text = "Host Server",
            font_size=24,
        )
        self.host_server_btn.bind(on_press=self.go_to_server_login_screen)
        button_layout.add_widget(self.host_server_btn)
        
        # Connect to Server
        self.connect_to_server_btn = Button(
            background_color=(54/255, 109/255, 150/255, 1),
            background_normal="",
            text = "Connect to Server",
            font_size=24,
        )
        self.connect_to_server_btn.bind(on_press=self.go_to_client_login_screen)
        button_layout.add_widget(self.connect_to_server_btn)

        self.add_widget(button_layout)
        
    def go_to_server_login_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "server-login"
        
    def go_to_client_login_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "client-login"