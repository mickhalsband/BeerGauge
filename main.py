from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.stacklayout import StackLayout

__author__ = 'mick'

from kivy.app import App
from kivy.uix.widget import Widget

class BeerGauge(Widget):
    pass

class ToolBar(StackLayout):
    pass


class ProgressionTable:
    table = {
        'Beer': 20,
        'Wine': 40,
        'Whisky': 60,
        'Other': 10
    }


class BGButton(Button):
    def do_action(self):
        print self.text
        self.parent.progressBar.progress(ProgressionTable.table[self.text])


class BeerGaugeBar(ProgressBar):
    def progress(self, change):
        self.value += change


class BeerGaugeApp(App):
    def build(self):
        return BeerGauge()


if __name__ == '__main__':
    BeerGaugeApp().run()