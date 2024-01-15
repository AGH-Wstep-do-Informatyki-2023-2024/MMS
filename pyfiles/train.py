from pyfiles.mainwindow import MainWindow
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from pyfiles.windowmanager import manager

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

class TopBackButton(Widget):
    def __init__(self, **kwargs):
        super(TopBackButton, self).__init__(**kwargs)
        # self.previous = previous

    # def go_back(self):
    #     global manager
    #     manager.current = self.previous

class BackButton(Button):
    def __init__(self, previous, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.previous = previous
    
    def go_back(self):
        global manager
        manager.current = self.previous


class NewTrainingContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTrainingContent, self).__init__(**kwargs)

        self.tbb.layout.add_widget(BackButton('train'))
        # self.reset()

    # def reset(self):
    #     self.clear_widgets()
    #     self.add_widget(TopBackButton('train'))
    #     self.add_widget(Label(text='no co tam halo'))
    #     print('reset 1')

class NewTrainingFirst(Screen):
    def __init__(self, **kwargs):
        super(NewTrainingFirst, self).__init__(**kwargs)
        # self.content = NewTrainingContent()

        self.reset_first()

        # self.add_widget(self.content)

    def reset_first(self):
        self.content = NewTrainingContent()
        self.add_widget(self.content)
        # self.content.clear_widgets()
        # self.content.add_widget(TopBackButton('train'))
        # self.content.add_widget(Label(text='no co tam halo'))
        # self.content.add_widget()


class NewTrainingSecond(Screen):
    def __init__(self, **kwargs):
        super(NewTrainingSecond, self).__init__(**kwargs)
        # self.reset()

    def reset(self):
        self.clear_widgets()
        self.add_widget(TopBackButton('train_new_training_first'))
        print('reset 2')

class DarkTextInput(TextInput):
    def __init__(self, **kwargs):
        super(DarkTextInput, self).__init__(**kwargs)


class TrainWindow(MainWindow):
    def __init__(self, **kwargs):
        super(TrainWindow, self).__init__(**kwargs)

        global manager

        nt_first = NewTrainingFirst(name='train_new_training_first')
        # nt_first.content = NewTrainingContent()
        nt_second = NewTrainingSecond(name='train_new_training_second')
        # nt_second.content = NewTrainingContent()


        manager.add_widget(nt_first)
        manager.add_widget(nt_second)


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
    def __init__(self, **kwargs):
        super(TrainTop, self).__init__(**kwargs)

    def new_training(self):
        global manager
        manager.current = 'train_new_training_first'
