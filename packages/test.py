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


def generate_ega_tasks():
    tasks = list(tests.keys())
    task = str(tasks[randint(0, len(tests.keys()) - 1)])
    return task


def ega_tests_show():
    ega_tests = EgaTest(task = generate_ega_tasks())

    tests_window = Popup(title='ЕГЭ тесты', content=ega_tests)

    tests_window.open()


class EgaTest(BoxLayout):

    def __init__(self, task):
        self.task = task

    submit_btn = Button(text='Submit',
                        font_size=20,
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
