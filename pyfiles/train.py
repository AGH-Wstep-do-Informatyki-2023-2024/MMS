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

ne_window = None
nt_window = None

configuration = {}
exercises = []

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
            global nt_second
            nt_first.reset_first()
            nt_second.reset_second()
            
            global configuration
            configuration = {}

            global exercises
            exercises = []

            # print(configuration)

            # print(exercises)

        if self.previous == 'train_new_training_second':
            global ne_window
            global nt_window

            ne_window.reset()
            nt_window.reset()
            

class NewExerciseLabel(BoxLayout):
    def __init__(self, **kwargs):
        super(NewExerciseLabel, self).__init__(**kwargs)

class NewExerciseMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(NewExerciseMenu, self).__init__(**kwargs)
    
class AddExercise(Button):
    def __init__(self, **kwargs):
        super(AddExercise, self).__init__(**kwargs)

    def add_exercise(self):
        global manager
        manager.current = 'new_exercise'

    def add_timer(self):
        global manager
        manager.current = 'new_timer'

class NewTimerWindow(Screen):
    def __init__(self, **kwargs):
        super(NewTimerWindow, self).__init__(**kwargs)
        self.reset()

    def reset(self):
        self.content = NewTimerContent()
        self.add_widget(self.content)

class NewTimerContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTimerContent, self).__init__(**kwargs)

class NewExerciseWindow(Screen):
    def __init__(self, **kwargs):
        super(NewExerciseWindow, self).__init__(**kwargs)
        self.content = None
        self.reset()

    def reset(self):
        if self.content:
            self.content.clear_widgets()
        self.content = NewExerciseContent()
        self.add_widget(self.content)


class NewExerciseContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewExerciseContent, self).__init__(**kwargs)
        self.tbb.layout.add_widget(BackButton('train_new_training_second'))

    def add_exercise(self):
        if self.ex_name.text.strip() == '':
            return
        
        global exercises
        new_ex = {
            'name': self.ex_name.text.strip(),
            'description': self.ex_description.text.strip()
            }
        exercises.append(new_ex)
        
        global manager
        manager.current = 'train_new_training_second'

        global nt_second
        nt_second.content.reset()

        self.ex_name.text = ''
        self.ex_description.text = ''

        # print(exercises)
        

class NewTrainingSecondContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTrainingSecondContent, self).__init__(**kwargs)

        global manager
        if manager.has_screen('new_exercise'):
            manager.remove_widget(manager.get_screen('new_exercise'))

        if manager.has_screen('new_timer'):
            manager.remove_widget(manager.get_screen('new_timer'))

        global ne_window
        global nt_window
            
        ne_window = NewExerciseWindow(name='new_exercise')
        nt_window = NewTimerWindow(name='new_timer')
        manager.add_widget(ne_window)
        manager.add_widget(nt_window)

        self.tbb.layout.add_widget(BackButton('train_new_training_first'))

        self.reset()

    def add_object(self, object):
        self.content_layout.add_widget(object)

        self.num_of_elements += 1
        self.content_layout.height += object.height

    def reset(self):
        self.num_of_elements = 0
        self.content_layout.height = self.content_layout.minimum_height
        self.content_layout.clear_widgets()

        global exercises

        print(exercises)
        global manager
        print(manager.screens)
        for ex in exercises:
            new_ex = NewExerciseLabel()
            new_ex.img.source = IMG_PATH + 'barbell-white.png'
            new_ex.label.text = ex['name']
            self.add_object(new_ex)
        
        self.add_object(NewExerciseMenu())

        self.add_object(Label(text=''))


class NewTrainingFirstContent(GridLayout):
    def __init__(self, **kwargs):
        super(NewTrainingFirstContent, self).__init__(**kwargs)

        self.tbb.layout.add_widget(BackButton('train'))
        self.change_icon(None)

    def go_next(self, next):
        if self.name.text.strip() == '':
            return
        
        if not self.current_icon:
            return 

        global manager
        manager.current = next

        global configuration
        configuration['name'] = self.name.text.strip()
        configuration['icon'] = self.current_icon
        configuration['description'] = self.description.text.strip()

        global nt_second 
        nt_second.content.name_label.text = self.name.text.strip()

        # print(configuration)

    def change_icon(self, icon):
        self.current_icon = icon
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

        # global nt_first
        # global manager
        # manager.remove_widget(nt_first)



class NewTrainingSecond(Screen):
    def __init__(self, **kwargs):
        super(NewTrainingSecond, self).__init__(**kwargs)
        self.reset_second()

    def reset_second(self):
        self.content = NewTrainingSecondContent()
        self.add_widget(self.content)

        self.content.reset()

        # global nt_second
        # global manager
        # manager.remove_widget(nt_second)

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
