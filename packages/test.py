from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window

from random import randint


class Pages(PageLayout):
    pass


class ParonimApp(App):
    def build(self):
        return Pages()


if __name__ == '__main__':
    ParomnimApp().run()
