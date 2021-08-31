from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase

from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from random import choice
import json

from packages.ega_mode import make_tests

# Keyboard above text input
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'

user_file = 'packages/data/user.json'


class MenuScreen(Screen):
    Builder.load_file('kv_files/MenuScreenV2.kv')

    def on_pre_enter(self):
        app = MDApp.get_running_app()
        self.ids.scores.text = str(app.scores)
        self.ids.ega_percentage.text = app.get_percentage_text(app.ega_right_answers, app.ega_wrong_answers)

        ega_percentage = app.get_percentage(app.ega_right_answers, app.ega_wrong_answers)
        try:
            if ega_percentage >= 50:
                self.ids.ega_percentage.theme_text_color = "Custom"
                self.ids.ega_percentage.text_color = (.33, .65, .1, 1)
            elif ega_percentage < 50:
                self.ids.ega_percentage.theme_text_color = "Custom"
                self.ids.ega_percentage.text_color = (.96, .24, .20, 1)
        except TypeError:
            pass


class ArchiveScreen(Screen):
    Builder.load_file('kv_files/ArchiveScreen.kv')


class SettingsScreen(Screen):
    Builder.load_file('kv_files/SettingsScreen.kv')


class EgaTestsScreen(Screen):
    """Main screen for "ЕГЭ" tests"""

    Builder.load_file("kv_files/EgaTestsScreenV2.kv")

    def __init__(self, **kwargs):
        super(EgaTestsScreen, self).__init__(**kwargs)

        self.layout = self.ids.layout

        self.carousel = None

    def on_enter(self):
        if self.carousel is not None:
            self.layout.remove_widget(self.carousel)
            self.carousel = EndlessEgaCarousel(direction='right')
            self.layout.add_widget(self.carousel)

        else:
            self.carousel = EndlessEgaCarousel(direction='right')
            self.layout.add_widget(self.carousel)

        self.carousel.create_test()
        self.carousel.create_test()

    def nav_drawer_logic(self, instance):

        if instance.icon == 'menu':
            MDApp.get_running_app().root.transition.direction = 'up'
            MDApp.get_running_app().root.current = 'menu'

            MDApp.get_running_app().refresh()

        elif instance.icon == 'cog-outline':
            MDApp.get_running_app().root.transition.direction = 'up'
            MDApp.get_running_app().root.current = 'settings'


class EndlessEgaCarousel(MDCarousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tests = make_tests()

    def on_slide_complete(self, *args):
        self.create_test()

    def create_test(self):
        task = self.tests.pop(choice(list(self.tests.keys())))

        task_text = ".\n \n".join(task[0]) + '.'

        answer = task[1]

        test = EgaTestLayout()
        test.create_task(task_text, answer)

        self.add_widget(test)


class EgaTestLayout(BoxLayout):
    Builder.load_file('kv_files/EgaTestLayoutV2.kv')

    def __init__(self, **kwargs):
        super(EgaTestLayout, self).__init__(**kwargs)

        self.answer = ''
        self.answer_is_right = False

    def create_task(self, task_text, task_answer):
        self.ids.task.text = task_text
        self.answer = task_answer

    def submit_answer(self):

        # Checking if answer is right
        if self.ids.answer_field.text.lower() == self.answer:
            self.answer_is_right = True
            MDApp.get_running_app().scores += 10
            MDApp.get_running_app().ega_right_answers += 1
            self.parent.parent.parent.parent.parent.parent.parent.ids.scores.text = f'{MDApp.get_running_app().scores}'
        else:
            MDApp.get_running_app().ega_wrong_answers += 1
            self.answer_is_right = False

        self.show_answer()

    def show_answer(self):
        self.ids.answer_field_layout.remove_widget(self.ids.answer_field)
        self.ids.answer_field_layout.remove_widget(self.ids.submit_btn)
        if self.answer_is_right:
            self.ids.answer_field_layout.add_widget(MDLabel(text=self.answer,
                                                            halign="center",
                                                            size_hint=(1, 1),
                                                            font_style="JetBrainsMono-Label",
                                                            theme_text_color="Custom",
                                                            text_color=(.33, .65, .1, 1)))

        else:
            self.ids.answer_field_layout.add_widget(MDLabel(text=self.answer,
                                                            halign="center",
                                                            size_hint=(1, 1),
                                                            font_style="JetBrainsMono-Label",
                                                            theme_text_color="Custom",
                                                            text_color=(.96, .24, .20, 1)))


class ParonimApp(MDApp):
    """Main App class"""

    def __init__(self, **kwargs):
        super(ParonimApp, self).__init__(**kwargs)

        # Creating Screen Manager
        self.sm = ScreenManager()

        self.user_data = self.get_user_data()

        self.scores = self.user_data["scores"]
        self.ega_right_answers = self.user_data["ega_right_answers"]
        self.ega_wrong_answers = self.user_data["ega_wrong_answers"]

    def build(self):
        # Creating main theme style
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.accent_palette = "Red"

        # Creating fonts
        self.create_fonts()

        # Adding all screens
        self.add_screens()

        return self.sm

    def add_screens(self):
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.add_widget(EgaTestsScreen(name='ega'))

    def create_fonts(self):
        """Class that`s create custom fonts"""

        LabelBase.register(
            name="JetBrainsMono",
            fn_regular="fonts/JetBrainsMono-Regular.ttf")

        LabelBase.register(
            name="JetBrainsMono-Italic",
            fn_regular="fonts/JetBrainsMono-Italic.ttf")

        # Font for Labels
        self.theme_cls.font_styles["JetBrainsMono-Label"] = [
            "fonts/JetBrainsMono-Regular",
            50,
            True,
            0.15,
        ]

        # Font for Buttons
        self.theme_cls.font_styles["JetBrainsMono-Buttons"] = [
            "fonts/JetBrainsMono-Regular",
            20,
            True,
            0.15,
        ]

        # Font for text
        self.theme_cls.font_styles["JetBrainsMono-Text"] = [
            "fonts/JetBrainsMono-Italic",
            20,
            False,
            0.15,
        ]

    def get_user_data(self):
        with open(user_file) as user_data_file:
            user_data = json.load(user_data_file)
            return user_data

    def get_percentage(self, right_answers, wrong_answers):
        all_answers = right_answers + wrong_answers

        try:
            percentage = right_answers / all_answers * 100
        except ZeroDivisionError:
            percentage = None
        return percentage

    def get_percentage_text(self, right_answers, wrong_answers):

        all_answers = right_answers + wrong_answers

        try:
            percentage = right_answers / all_answers * 100
            percentage_text = f"Процент правильности: {'%.0f' % percentage}%"
        except ZeroDivisionError:
            percentage_text = f"Вы еще не проходили эти тесты."
        return percentage_text

    def on_stop(self):
        new_user_data = {
            "scores": self.scores,
            "ega_right_answers": self.ega_right_answers,
            "ega_wrong_answers": self.ega_wrong_answers,
        }
        with open(user_file, 'w') as user_data_file:
            json.dump(new_user_data, user_data_file)


if __name__ == '__main__':
    ParonimApp().run()
