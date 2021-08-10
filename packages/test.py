from kivy.app import App

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


def ega_tests_show():
    ega_tests = EgaTest()

    tests_window = Popup(title='ЕГЭ тесты', content=ega_tests)

    tests_window.open()


class EgaTest(BoxLayout):
    pass


class Pages(PageLayout):
    def page_1_btn(self):
        tasks = list(tests.keys())
        task = str(tasks[randint(0, len(tests.keys()) - 1)])
        ega_tests_show()


class ParonimApp(App):
    def build(self):
        return Pages()


if __name__ == '__main__':
    ParonimApp().run()
