from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.app import App


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = AnchorLayout(
            anchor_x = 'center',
            anchor_y = 'center',
        )
        self.login_button = Button(
            background_color=(54/255, 109/255, 59/255, 1),
            background_normal="",
            size_hint=(.3, .3),
            text = "Login",
            font_size=24,
        )
        self.login_button.bind(on_press=self.go_to_chat_screen)
        layout.add_widget(self.login_button)
        self.add_widget(layout)
        
    def go_to_chat_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "chat"