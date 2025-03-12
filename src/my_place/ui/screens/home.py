from kivy.uix.screenmanager import ScreenManager

from my_place.ui.screens.login import LoginScreen
from my_place.ui.screens.chat import ChatScreen

class HomeScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login_screen = LoginScreen(name="login")
        self.chat_screen = ChatScreen(name="chat")
        self.add_widget(self.login_screen)
        self.add_widget(self.chat_screen)
