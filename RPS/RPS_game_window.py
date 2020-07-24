import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

os.chdir(os.getcwd())
import main_body
global n
n = 0
class MyGrid(Widget):
                global p_wins
                global com_wins
                global comp_choice
                global p_choice
                p_wins = ObjectProperty(None)
                com_wins = ObjectProperty(None)
                comp_choice = ObjectProperty(None)
                p_choice = ObjectProperty(None)
                def hand(self,i):
                    #Rock=-1 Paper=0 Scissor=1
                        global n
                        global p_wins
                        global com_wins
                        global comp_choice
                        global p_choice
                        n=i
                        p_wins, com_wins, comp_choice ,p_choice = main_body.main(n)
                        self.p_wins.text = str(p_wins)
                        self.com_wins.text = str(com_wins)
                        self.comp_choice.text = str(comp_choice)
                        self.p_choice.text = str(p_choice)
                def reset(self):
                        global p_wins
                        global com_wins
                        p_wins = 0
                        com_wins = 0
                        self.p_wins.text = "0"
                        self.com_wins.text = "0"
                        self.comp_choice.text = "The CPU's choice is shown here"
                        self.p_choice.text = "Your choice is shown here"
                        main_body.rezero()
                        
class RPSApp(App):
                def build(self):
                                return MyGrid()

if __name__=="__main__":
                RPSApp().run()
    
