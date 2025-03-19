from kivy.uix.screenmanager import ScreenManager

from my_place.ui.screens.login import LoginScreen
from my_place.ui.screens.chat import ChatScreen
from my_place.ui.screens.client import ClientLoginScreen
from my_place.ui.screens.server import ServerLoginScreen

class HomeScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login_screen = LoginScreen(name="login")
        self.client_login_screen = ClientLoginScreen(name="client-login")
        self.server_login_screen = ServerLoginScreen(name="server-login")
        self.chat_screen = ChatScreen(name="chat")
        self.add_widget(self.login_screen)
        self.add_widget(self.client_login_screen)
        self.add_widget(self.server_login_screen)
        self.add_widget(self.chat_screen)
