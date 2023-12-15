from pyfiles.mainwindow import MainWindow
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior

storage = JsonStore('trainings.json')
IMG_PATH = './img/'

class TrainLabel(Widget):
    def __init__(self, id, **kwargs):
        super(TrainLabel, self).__init__(**kwargs)
        self.id = id
        self.name = storage.get(id)['name']
        self.icon = IMG_PATH + storage.get(id)['icon']

        self.namelabel.text = self.name
        self.iconlabel.source = self.icon

    def show_description(self):
        print(self.name)


class TrainWindow(MainWindow):
    def __init__(self, **kwargs):
        super(TrainWindow, self).__init__(**kwargs)

class TrainContent(GridLayout):
    def __init__(self, **kwargs):
        super(TrainContent, self).__init__(**kwargs)
        self.height = self.minimum_height + 100
        
        top = TrainTop()
        self.add_widget(top)
        self.height += top.height

        self.trainlabels = []
        for id in storage.keys():
            label = TrainLabel(id)
            self.trainlabels.append(label)
            self.add_widget(label)
            self.height += label.height


class TrainTop(BoxLayout):
    pass
