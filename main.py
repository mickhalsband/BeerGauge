from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

__author__ = 'mick'

from kivy.app import App
from kivy.uix.widget import Widget


class BeerGauge(Widget):
    pass


class ToolBar(StackLayout):
    pass


class BGButton(Button):
    def do_action(self, ªtext):
        print text


class BeerGaugeApp(App):
    def build(self):
        return BeerGauge()


if __name__ == '__main__':
    BeerGaugeApp().run()