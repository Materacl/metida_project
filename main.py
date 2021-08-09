from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window

from random import randint
Window.title = 'Metida'


class ParonimApp(App):
    """Main ParomnimApp class"""

    def __init__(self):
        super().__init__()

    def btn_pressed(self, instance):
        instance.text = 'Touched'

    def build(self):
        main_layout = PageLayout()
        page_layout = AnchorLayout()
        menu_layout = BoxLayout(orientation='vertical', size_hint=[0.5, 0.5])

        page_layout.add_widget(menu_layout)

        page_1 = Button(text='Page 1',
                        font_size=30,
                        background_normal='',
                        background_color=[.15, .55, .4, 1],
                        on_press=self.btn_pressed)

        page_2 = Button(text='Page 2',
                        font_size=30,
                        background_color=[.29, .53, .55, 1])
        page_2.bind(on_press=self.btn_pressed)

        page_3 = Button(text='Page 3',
                        font_size=30,
                        background_color=[.19, .26, .35, 1])
        page_3.bind(on_press=self.btn_pressed)

        main_layout.add_widget(page_1)
        main_layout.add_widget(page_2)
        main_layout.add_widget(page_3)

        return main_layout


if __name__ == '__main__':
    ParonimApp().run()
