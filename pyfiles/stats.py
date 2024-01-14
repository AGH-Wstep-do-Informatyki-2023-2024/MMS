from pyfiles.mainwindow import MainWindow
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class StatsWindow(MainWindow):
    def __init__(self, **kwargs):
        super(StatsWindow, self).__init__(**kwargs)

class ExerciseSelector(GridLayout):
    def __init__(self, **kwargs):
        super(ExerciseSelector, self).__init__(**kwargs)

        self.result_label = Label()
        self.add_widget(self.result_label)

    def on_spinner_text(self, text):
        pass

    def onerepmax(self):
        try:
            if self.ids.exercise_spinner.text == "Wybierz ćwiczenie":
                raise ValueError("Wybierz ćwiczenie przed obliczeniem")
            
            weight = float(self.ids.weight_input.text)
            reps = float(self.ids.reps_input.text)

            if reps != 0 or weight!= 0:
                result = (0.0333*weight*reps)+weight
                self.result_label.text = f'Twój ciężar maksymalny na jedno powtórzenie: {result:.2f} kg'
                self.result_label.font_size = 20
            else:
                self.result_label.text ="Podano złą wartość !"
        
        except ValueError as e:
            popup = Popup(title='Błąd', content=Label(text=str(e)), size_hint=(None, None), size=(400, 200))
            popup.open()

class StatsContent(BoxLayout):
    def __init__(self, **kwargs):
        super(StatsContent, self).__init__(**kwargs)
        exercise_selector = ExerciseSelector()
        self.add_widget(exercise_selector)

class StatsTop(BoxLayout):
    pass
