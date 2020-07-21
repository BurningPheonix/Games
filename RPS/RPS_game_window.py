import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

os.chdir(os.cwd())
import main_body
n=int()
class MyGrid(Widget):
	p_wins = ObjectProperty(None)
	com_wins = ObjectProperty(None)
	def win_count(self):
		self.p_wins.text = self.p_wins.text
		self.com_wins.text = self.com_wins.text
		
	def rock(self):
		n=-1
	def paper(self):
		n=0
	def scissor(self):
		n=1
	
	def main(self):
		p_wins,com_wins=main_body.main(n)
		win_count()
class RPSApp(App):
	def build(self):
		return MyGrid()

if __name__=="__main__":
	RPSApp().run()
