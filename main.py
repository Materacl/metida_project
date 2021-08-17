from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from random import choice
from packages.ega_mode import make_tests


# Keyboard above text input
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = 'below_target'


class MenuScreen(Screen):
    Builder.load_file('kv_files/MenuScreen.kv')
    pass


class PracticeChooseScreen(Screen):
    Builder.load_file('kv_files/PracticeChooseScreen.kv')
    pass


class EgaTestsScreen(Screen):
    """Main screen for "ЕГЭ" tests"""

    Builder.load_file("kv_files/EgaTestsScreen.kv")

    def __init__(self, **kwargs):
        super(EgaTestsScreen, self).__init__(**kwargs)

        self.layout = self.ids.layout
        self.carousel = MDCarousel(direction='right')
        self.carousel_slides = self.carousel.slides

        self.progress = 0
        self.max_progress = 0

        self.right_answers = 0

    def on_enter(self):
        self.create_slides()

    def create_slides(self):
        # Creating tests data from imported func
        tests = make_tests()

        # Creating slides with different tests
        for i in range(len(make_tests())):
            task = tests.pop(choice(list(tests.keys())))
            task_text = "\n".join(task[0])

            answer = task[1]

            test = EgaTestLayout()
            test.create_task(task_text, answer)

            self.max_progress += 1

            self.carousel.add_widget(test)

        # Creating end screen
        self.carousel.add_widget(TestEndLayout())

        # Adding widgets to the main layout
        self.carousel_slides = self.carousel.slides
        self.layout.add_widget(self.carousel)

    # Switches slides
    def next_slide(self):
        self.carousel.load_next(mode='next')

        progress_bar = self.ids.progress_bar
        progress_bar.value = self.progress / self.max_progress * 100

    # Button that leads to settings and menu
    def action_button(self, btn):
        if btn.icon == 'menu':
            MDApp.get_running_app().root.transition.direction = 'up'
            MDApp.get_running_app().root.current = 'menu'
            self.layout.remove_widget(self.carousel)

        elif btn.icon == 'cog-outline':
            MDApp.get_running_app().root.transition.direction = 'up'
            MDApp.get_running_app().root.current = 'settings'
            self.layout.remove_widget(self.carousel)


class EgaTestLayout(BoxLayout):
    Builder.load_file('kv_files/EgaTestLayout.kv')

    def __init__(self, **kwargs):
        super(EgaTestLayout, self).__init__(**kwargs)

        self.answer = ''
        self.answer_is_right = False

        self.first_submit = False

    def create_task(self, task_text, task_answer):
        self.ids.task.text = task_text
        self.answer = task_answer
        print(self.answer)

    def submit_answer(self):

        # Checking if the submit button was pressed first time
        if not self.first_submit:
            self.parent.parent.parent.parent.progress += 1
            self.first_submit = True

        # Checking if answer is right
        if self.ids.answer_field.text.lower() == self.answer:
            self.answer_is_right = True

            if self.first_submit:
                self.parent.parent.parent.parent.right_answers += 1
        else:
            self.answer_is_right = False

        # Мне стыдно...
        self.parent.parent.parent.parent.next_slide()

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
        print('Nu da')


class TestEndLayout(AnchorLayout):
    Builder.load_file('kv_files/TestEndLayout.kv')

    def end_btn(self):
        carousel = self.parent.parent

        self.show_stats(carousel)

        for slide in carousel.slides[0:len(carousel.slides) - 1]:
            slide.show_answer()

        #carousel.load_slide(carousel.slides[0])

    def show_stats(self, carousel):
        stats = self.ids.stats
        right_answers = self.parent.parent.parent.parent.right_answers

        stats.text = f"Правильно:\n{right_answers}/{len(carousel.slides) - 1}" \
                     f"\n{'%.0f' % ((right_answers/(len(carousel.slides) - 1)) * 100)}%"


class SettingsScreen(Screen):
    Builder.load_file('kv_files/SettingsScreen.kv')


class ParonimApp(MDApp):
    """Main App class"""

    def build(self):
        # Creating main theme style
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "DeepOrange"

        # Creating fonts
        self.create_fonts()

        # Creating Screen Manager
        sm = ScreenManager()

        # Adding all screens
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(PracticeChooseScreen(name='practice'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(EgaTestsScreen(name='ega'))

        return sm

    def create_fonts(self):
        """Class that`s create custom fonts"""

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


if __name__ == '__main__':
    ParonimApp().run()
