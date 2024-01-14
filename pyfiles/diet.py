from pyfiles.mainwindow import MainWindow
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DietWindow(MainWindow):
    def __init__(self, **kwargs):
        super(DietWindow, self).__init__(**kwargs)


class DietContent(GridLayout):
    def __init__(self, **kwargs):
        super(DietContent, self).__init__(**kwargs)
        self.add_widget(Calc())
        top = DietTop()
        
class Calc(GridLayout):
    def __init__(self, **kwargs):
            super(Calc, self).__init__(**kwargs)
            self.cols = 1        
            self.result_label = Label(text="")
            self.add_widget(self.result_label)

    def calculate_calories(self):
        try:
            mass = float(self.ids.mass_input.text)
            height = float(self.ids.height_input.text)
            age = int(self.ids.age_input.text)  
            gender = self.ids.gender_spinner.text
            pal = float(self.ids.pal_input.text)

            if gender == "Mężczyzna":
                result = (66.47 + (13.7 * mass) + (5 * height) - (6.76 * age)) * pal    #mezczyzna
              
            elif gender == "Kobieta":
                result = (655.1 + (9.567 * mass) + (1.85 * height) - (4.68 * age)) * pal    #kobieta
                
            else:
                result = self.result_label.text ="Podano złą wartość !"
                
            self.result_label.text = f"Twoje zapotrzebowanie kaloryczne: {result:.2f} kcal"
            self.result_label.font_size = 24

        except ValueError:
            self.result_label.text = "Błędne dane!"
    
class DietTop(BoxLayout):
    pass


            

            

            
            
