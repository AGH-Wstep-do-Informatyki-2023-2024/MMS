from pyfiles.mainwindow import MainWindow
from kivy.uix.widget import Widget

class StatsWindow(MainWindow):
    def __init__(self, **kwargs):
        super(StatsWindow, self).__init__(**kwargs)

class StatsContent(Widget):
    def __init__(self, **kwargs):
        super(StatsContent, self).__init__(**kwargs)