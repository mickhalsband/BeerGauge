from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.stacklayout import StackLayout

__author__ = 'mick'

from kivy.app import App
from kivy.uix.widget import Widget


# TODO: Input male/female & body weight (categories?)
# TODO: Human figure progress bar with safety levels (&blood alcohol level):
#	* Driving safety
#	* Hangover free
# TODO: optional input bed-time, upon which
#	* a red-line indicating last point at which hangover is avoided at requested bedtime
# 
# Future todos: 
#	* maybe a soberness test (stability and/or accuracy) calibrating the alcohol level estimation
#	* maybe learn according to past experience (hangover false/positives etc.)
#	* input results from self-tests for blood alcohol, upon which a model would be re-calibrated.


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
    """
    Automatically decrease levels according to pre-configured interval and step
    """
    decrease_step = 5
    decrease_interval = 0.5

    def __init__(self, **kwargs):
        super(BeerGaugeBar, self).__init__(**kwargs)
        Clock.schedule_interval(self.decrease_levels, self.decrease_interval)

    def progress(self, change):
        self.value += change

    def decrease_levels(self, *largs):
        self.value -= self.decrease_step


class BeerGaugeApp(App):
    def build(self):
        return BeerGauge()


if __name__ == '__main__':
    BeerGaugeApp().run()