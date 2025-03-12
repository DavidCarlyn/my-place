from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import mainthread

from my_place.ui.widgets.custom import CustomBackgroundColor, CustomBorder
from my_place.core.networking.interface import NetworkInterface


class CustomBoxLayout(BoxLayout, CustomBackgroundColor, CustomBorder):
    def __init__(self, **kw):
        self.background_color = kw.get("background_color", (0, 0, 1, 1))
        super().__init__(**kw)
            

class ChatScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        # Main Layout
        screen_layout = BoxLayout(
            orientation = "vertical"
        )
        
        # a list of chat items to be displayed
        self.chat_items = []
        self.chat_item_layout = CustomBoxLayout(
            orientation = "vertical",
            size_hint = (1, 0.95),
            padding=10,
            spacing=6,
        )
        
        # Where the user will enter text and send messages
        input_box = BoxLayout(
            orientation = "horizontal",
            size_hint = (1, 0.05),
        )
        
        # Text box for input
        self.input_text_box = TextInput(
            size_hint = (0.8, 1),
            multiline=False,
        )
        self.input_text_box.bind(on_text_validate=self.send_message)
        
        # Send Button
        send_button = Button(
            background_color = (37/255, 142/255, 146/255, 1),
            background_normal = "",
            text="Send",
            size_hint=(0.2, 1),
        )
        send_button.bind(on_release=self.send_message)
        
        # Add to input box
        input_box.add_widget(self.input_text_box)
        input_box.add_widget(send_button)
        
        # Set main layout
        self.add_widget(screen_layout)
        
        # Add to main layout
        screen_layout.add_widget(self.chat_item_layout)
        screen_layout.add_widget(input_box)
        
    def send_message(self, instance):
        message = self.input_text_box.text
        if message == "":
            # TODO give  the user some type of feedback
            return 
        
        network : NetworkInterface = App.get_running_app().network
        if network:
            network.send(message)
        self.input_text_box.text = ""
        self.add_chat_item(message)
        
    @mainthread
    def add_chat_item(self, message):
        chat_item = CustomBoxLayout(orientation="horizontal", size_hint_max_y=30, background_color=(1, 0, 0, 1))
        message_label = Label(text=message, halign="left", valign="center", padding=4)
        message_label.bind(size=message_label.setter('text_size'))
        chat_item.add_widget(message_label)
        self.chat_items.append(chat_item)
        self.chat_item_layout.add_widget(chat_item)
        