import kivy
import kivy_config

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

class HomeWindow(MainWindow):
    def __init__(self, **kwargs):
        super(HomeWindow, self).__init__(**kwargs)

class TrainWindow(MainWindow):
    def __init__(self, **kwargs):
        super(TrainWindow, self).__init__(**kwargs)

class DietWindow(MainWindow):
    def __init__(self, **kwargs):
        super(DietWindow, self).__init__(**kwargs)

class StatsWindow(MainWindow):
    def __init__(self, **kwargs):
        super(StatsWindow, self).__init__(**kwargs)

class ProfileWindow(Screen):
    def __init__(self, **kwargs):
        super(ProfileWindow, self).__init__(**kwargs)

class NavBar(Widget):
    def __init__(self, manager, current, **kwargs):
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

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)

class MainApp(App):
    def __init__(self, manager, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.manager = manager

    def build(self):
        self.title = 'MMS'
        return self.manager

if __name__ == '__main__':
    kv = Builder.load_file('structure.kv')
    manager = WindowManager()

    home_window = HomeWindow(name='home')
    train_window = TrainWindow(name='train')
    diet_window = DietWindow(name='diet')
    stats_window = StatsWindow(name='stats')

    main_screens = [home_window, train_window, diet_window, stats_window]
    for screen in main_screens:
        screen.layout.add_widget(NavBar(manager=manager, current=screen))
        manager.add_widget(screen)

    manager.current = 'home'

    profile_window = ProfileWindow(name='profile')
    manager.add_widget(profile_window)

    MainApp(manager).run()