from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# Declare both screens
class MenuScreen(Screen):
    pass


class FirstPage(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Paronim2App(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FirstPage(name='page_1'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


if __name__ == '__main__':
    Paronim2App().run()
