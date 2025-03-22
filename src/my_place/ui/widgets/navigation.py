from kivy.uix.button import Button
from kivy.app import App

class BackButton(Button):

    def __init__(self, screen_name, **kw):
        # Handle defaults
        default = {
            "text" : "Back", 
            "background_color" : (54/255, 109/255, 59/255, 1), 
            "background_normal" : "",
            "pos_hint" : {"y": 0.95, "x": 0.0}, 
            "size_hint" : (0.1, 0.05)
        }
        for k, v in default.items():
            if k not in kw:
                kw[k] = v

        super().__init__(**kw)
        self.screen_name = screen_name
        self.bind(on_press=self.on_btn_pressed)
        
    def on_btn_pressed(self, instance):
        app = App.get_running_app()
        app.root.current = self.screen_name
        self.parent.manager.transition.direction = "right"
        
    