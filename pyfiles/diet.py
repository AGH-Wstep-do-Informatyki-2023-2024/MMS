from pyfiles.mainwindow import MainWindow
from kivy.uix.widget import Widget

class DietWindow(MainWindow):
    def __init__(self, **kwargs):
        super(DietWindow, self).__init__(**kwargs)

class DietContent(Widget):
    def __init__(self, **kwargs):
        super(DietContent, self).__init__(**kwargs)
