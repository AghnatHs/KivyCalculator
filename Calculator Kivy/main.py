import kivy

from kivy.metrics import dp, sp
from kivy.core.window import Window

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

__version__ = "1.0"

class CalculatorScreen(FloatLayout):

    def __init__(self,**kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        self.size = (Window.size[0],Window.size[1])
        self.calculation = ""

    def deleteValue(self,type=None):
        if type!=None:
            self.calculation = ""
            self.ids.calculatorInput.text = self.calculation
        else:
            self.calculation = self.calculation[:-1]
            self.ids.calculatorInput.text = self.calculation

    def inputValue(self,value):
        self.calculation = str(self.calculation)+str(value)
        self.ids.calculatorInput.text = self.calculation

    def calculateValue(self):
        try:    
            self.calculation = self.calculation.replace("x","*")
            self.calculation = self.calculation.replace(":","/")
            self.calculation = self.calculation.replace("^","**")
            self.calculation = str(eval(self.calculation))
            self.ids.calculatorInput.text = self.calculation
        except:
            self.calculation = ""
            self.ids.calculatorInput.text = "Error"
    
    def updateValue(self):
        self.ids.calculatorInput.text = self.calculation

class CalculatorApp(App):
    def build(self):
        Builder.load_file("main.kv")
        calculator = CalculatorScreen()
        return calculator


if __name__=="__main__":
    app = CalculatorApp()
    app.run()