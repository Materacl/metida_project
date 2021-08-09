from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


def make_page(name, color=None):
    if color is None:
        color = [1, 1, 1, 1]

    page = Label(text=name, font_size=30)
    page_layout = AnchorLayout(anchor_x='center', anchor_y='center')
    btns_layout = BoxLayout(orientation='vertical', spacing=1, size_hint=[1, 1])

    page_layout.add_widget(btns_layout)
    page.add_widget(page_layout)

    start_btn = Button(text='Start',
                       font_size=30,
                       background_normal='',
                       background_color=[7 / 255, 9 / 255, 13 / 255, 1])
    #start_btn.bind(on_press=start_func)

    menu_btn = Button(text='Menu',
                      font_size=30,
                      background_normal='',
                      background_color=[7 / 255, 9 / 255, 13 / 255, 1])
    #start_btn.bind(on_press=menu_func)

    page_layout.add_widget(start_btn)
    btns_layout.add_widget(menu_btn)

    return page
