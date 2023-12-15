from pyfiles.mainwindow import MainWindow
# from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomeWindow(MainWindow):
    def __init__(self, **kwargs):
        super(HomeWindow, self).__init__(**kwargs)

class HomeContent(GridLayout):
    def __init__(self, **kwargs):
        super(HomeContent, self).__init__(**kwargs)
        self.num_of_elements = 0
        self.height = self.minimum_height

        for i in range(10):
            label = Label(text=f'{i}', height=200)
            btn = Button(text=f'{i}')
            self.add_widget(label)
            self.add_widget(btn)
            self.num_of_elements += 2
        
            self.height += label.height
            self.height += btn.height