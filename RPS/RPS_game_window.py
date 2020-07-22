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
		def rock(self):
			global n
			n=-1
		def paper(self):
			global n
			n=0
		def scissor(self):
			global n
			n=1
		def main(self):
			p_wins, com_wins, comp_choice ,p_choice = main_body.main(n)
			self.p_wins.text = str(p_wins)
			self.com_wins.text = str(com_wins)
			self.comp_choice.text = str(comp_choice)
			self.p_choice.text = str(p_choice)
			
class RPSApp(App):
		def build(self):
				return MyGrid()

if __name__=="__main__":
		RPSApp().run()
