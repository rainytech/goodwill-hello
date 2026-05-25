"""
Goodwill - Hello App (build test only)
Smallest possible Kivy app: one label, one button.
Purpose: prove the Buildozer APK pipeline works before building anything real.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloRoot(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation="vertical", padding=40, spacing=20, **kw)
        self.count = 0

        self.msg = Label(
            text="Hello, Goodwill Tuition Centre!",
            font_size="22sp",
        )
        self.add_widget(self.msg)

        btn = Button(
            text="Tap me",
            font_size="20sp",
            size_hint_y=None,
            height=70,
        )
        btn.bind(on_release=self.tapped)
        self.add_widget(btn)

    def tapped(self, *_):
        self.count += 1
        self.msg.text = f"Tapped {self.count} time(s)!"


class HelloApp(App):
    def build(self):
        self.title = "Goodwill Hello"
        return HelloRoot()


if __name__ == "__main__":
    HelloApp().run()
