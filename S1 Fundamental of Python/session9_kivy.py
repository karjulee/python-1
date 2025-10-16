from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


# Custom widget for the window
class Task01(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add a label
        self.label = Label(text="Hello Umair!", pos=(150, 300), font_size=24)
        self.add_widget(self.label)

        # Add a button
        btn = Button(text="Click Me", pos=(150, 200), size_hint=(0.3, 0.1))
        btn.bind(on_press=self.on_button_click)
        self.add_widget(btn)

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"


# Main app class
class MyApp(App):
    def build(self):
        # Disable KV file auto-loading
        self.load_kv = False
        return Task01()


if __name__=="__main__":
    MyApp().run()