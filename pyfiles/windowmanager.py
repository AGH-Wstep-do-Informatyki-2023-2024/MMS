from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)

manager = WindowManager(transition=NoTransition())