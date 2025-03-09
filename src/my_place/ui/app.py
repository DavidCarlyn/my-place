from kivy.app import App
from kivy.core.window import Window

from my_place.ui.screens.home import HomeScreen
 
class MyPlaceApp(App):
    def build(self):
        Window.clearcolor = "#134921"
        return HomeScreen()