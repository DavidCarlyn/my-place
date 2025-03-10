from kivy.app import App
from kivy.core.window import Window

from my_place.ui.screens.home import HomeScreen
from my_place.core.networking.interface import NetworkInterface
 
class MyPlaceApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.network = NetworkInterface()
        self.screen_manager = None
            
    def build(self):
        Window.clearcolor = "#134921"
        self.screen_manager = HomeScreen()
        return self.screen_manager