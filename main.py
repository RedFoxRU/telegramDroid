from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3


class MainApp(App):
    def build(self):
        self.connect = sqlite3.connect('accounts.db')
        self.cursor = self.connect.cursor()
        self.last_was_operator = None
        self.last_button = None
        self.main_layout = BoxLayout(orientation="vertical")


if __name__ == "__main__":
    app = MainApp()
    app.run()
