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
		p_wins = ObjectProperty(None)
		com_wins = ObjectProperty(None)
		
		def rock(self):
				n=-1
		def paper(self):
				n=0
		def scissor(self):
				n=1
		
		def main(self):
				p_wins,com_wins=main_body.main(n)
				
				self.p_wins.text = str(p_wins)
				self.com_wins.text = str(com_wins)

class RPSApp(App):
		def build(self):
				return MyGrid()

if __name__=="__main__":
		RPSApp().run()
