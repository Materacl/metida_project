from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window

from random import randint

from ega_mode import tests

Builder.load_string('paronim2.kv')


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class FirstPageScreen(Screen):
    pass


class SecondPageScreen(Screen):
    pass


class ThirdPageScreen(Screen):
    pass


class Paronim2App(App):
    def build(self):
        # Creating the Screen Manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(FirstPageScreen(name='page_1'))
        sm.add_widget(SecondPageScreen(text='page_2'))
        sm.add_widget(ThirdPageScreen(name='page_3'))

        return sm


if __name__ == '__main__':
    ParonimApp().run()
