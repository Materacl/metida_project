from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

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
    tasks = tests.keys()
    task_shower = Label(text=tasks[randint(0, len(tests.values()))])
    answer_input = TextInput(multiline=False,
                             background_color=[.19, .26, .35, 1])
    pass


class Pages(PageLayout):
    def page_1_btn(self):
        ega_tests_show()


class ParonimApp(App):
    def build(self):
        return Pages()


if __name__ == '__main__':
    ParonimApp().run()
