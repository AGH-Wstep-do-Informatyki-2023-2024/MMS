from pyfiles.mainwindow import MainWindow
from kivy.uix.gridlayout import GridLayout
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
            btn1 = Button(text=f'{i}', background_color=(0, 0, 1, 1), height=200)
            btn2 = Button(text=f'{i}', background_color=(0, 1, 0, 1), height=200)
            self.add_widget(btn1)
            self.add_widget(btn2)
            self.num_of_elements += 2
        
            self.height += btn1.height
            self.height += btn2.height