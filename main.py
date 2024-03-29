import kivy
import kivy_config

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

from os import listdir

from pyfiles.windowmanager import manager

from pyfiles.home import *
from pyfiles.train import *
from pyfiles.diet import *
from pyfiles.stats import *
from pyfiles.profile import *


class NavBar(Widget):
    def __init__(self, current, **kwargs):
        super(NavBar, self).__init__(**kwargs)

        home_image = './img/house-gray.png'
        train_image = './img/barbell-gray.png'
        diet_image = './img/carrot-gray.png'
        stats_image = './img/chart-bar-gray.png'

        match current.name:
            case 'home':
                home_image = './img/house-white.png'
            case 'train':
                train_image = './img/barbell-white.png'
            case 'diet':
                diet_image = './img/carrot-white.png'
            case 'stats':
                stats_image = './img/chart-bar-white.png'
            case _:
                pass

        home_button = NavButton('home', home_image)
        train_button = NavButton('train', train_image)
        diet_button = NavButton('diet', diet_image)
        stats_button = NavButton('stats', stats_image)

        self.buttons = [home_button, train_button, diet_button, stats_button]
        for button in self.buttons:
            self.layout.add_widget(button)

class NavButton(Widget):
    def __init__(self, window, img, **kwargs):
        super(NavButton, self).__init__(**kwargs)
        self.window = window
        self.button.background_normal = img
        self.button.background_down = img
    
    def change_window(self):
        global manager
        manager.current = self.window
        

class Separator(Widget):
    pass

class TopBar(Widget):
    pass

class NotificationBell(Widget):
    pass

class ProfileIcon(Widget):
    pass

class Content(Widget):
    pass

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        self.title = 'MMS'
        global manager
        return manager

if __name__ == '__main__':
    KV_PATH = './kvfiles/'
    for file in listdir(KV_PATH):
        Builder.load_file(KV_PATH + file)

    # pages 
    home_window = HomeWindow(name='home')
    home_window.content.add_widget(HomeContent())

    train_window = TrainWindow(name='train')
    train_window.content.add_widget(TrainContent())

    diet_window = DietWindow(name='diet')
    diet_window.content.add_widget(DietContent())

    stats_window = StatsWindow(name='stats')
    stats_window.content.add_widget(StatsContent())

    main_screens = [home_window, train_window, diet_window, stats_window]
    for screen in main_screens:
        screen.layout.add_widget(NavBar(current=screen))
        manager.add_widget(screen)

    manager.current = 'home'

    profile_window = ProfileWindow(name='profile')
    manager.add_widget(profile_window)

    MainApp().run()
