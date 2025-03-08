from kivy.app import App

from my_place.ui.home import HomeScreen
 
class MyApp(App):
    def build(self):
        return HomeScreen()

def main() -> None:
    MyApp().run()
    