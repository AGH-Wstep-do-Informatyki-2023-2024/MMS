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

nt_first = None
nt_second = None

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

class BackButton(Button):
    def __init__(self, previous, **kwargs):
        super(BackButton, self).__init__(**kwargs)
        self.previous = previous
    
    def go_back(self):
        global manager
        manager.current = self.previous

        if self.previous == 'train':
            global nt_first
            nt_first.reset_first()


class NewTrainingSecondContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTrainingSecondContent, self).__init__(**kwargs)


class NewTrainingFirstContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTrainingFirstContent, self).__init__(**kwargs)

        self.tbb.layout.add_widget(BackButton('train'))
        self.change_icon(None)

    def change_icon(self, icon):
        self.icons.clear_widgets()

        barbell = IMG_PATH + 'barbell-gray.png'
        runner = IMG_PATH + 'person-simple-run-gray.png'
        bike = IMG_PATH + 'person-simple-bike-gray.png'

        match icon:
            case 'barbell':
                barbell = IMG_PATH + 'barbell-white.png'
            case 'runner':
                runner = IMG_PATH + 'person-simple-run-white.png'
            case 'bike':
                bike = IMG_PATH + 'person-simple-bike-white.png'
            case _:
                pass

        self.icons.add_widget(IconButton(
            content=self,
            icon='barbell',
            background_normal=barbell,
            background_down=barbell,
        ))

        self.icons.add_widget(IconButton(
            content=self,
            icon='runner',
            background_normal=runner,
            background_down=runner,
        ))

        self.icons.add_widget(IconButton(
            content=self,
            icon='bike',
            background_normal=bike,
            background_down=bike,
        ))

class IconButton(Button):
    def __init__(self, content, icon, **kwargs):
        super(IconButton, self).__init__(**kwargs)
        
        self.icon = icon
        self.content = content

    def change(self):
        self.content.change_icon(self.icon)

class NewTrainingFirst(Screen):
    def __init__(self, **kwargs):
        super(NewTrainingFirst, self).__init__(**kwargs)
        self.reset_first()

    def reset_first(self):
        self.content = NewTrainingFirstContent()
        self.add_widget(self.content)


class NewTrainingSecond(Screen):
    def __init__(self, **kwargs):
        super(NewTrainingSecond, self).__init__(**kwargs)

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

        global nt_first
        nt_first = NewTrainingFirst(name='train_new_training_first')
        
        global nt_second
        nt_second = NewTrainingSecond(name='train_new_training_second')

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
