from kivy.uix.screenmanager import ScreenManager

from my_place.ui.screens.login import LoginScreen
from my_place.ui.screens.chat import ChatScreen

class HomeScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LoginScreen(name="login"))
        self.add_widget(ChatScreen(name="chat"))
