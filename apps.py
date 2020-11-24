
import kivy

from kivy.app import App
from kivy.uix.label import Label


kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string(""" 
<ScreenOne>: 
	BoxLayout: 
	    orientation:"vertical"
	    TextInput:
	        id:weight
	        hint_text:"enter the weight excluding of vechile"
	    TextInput:
	        id:bags
	        hint_text:"enter no.of bags"
	    TextInput:
	        id:acers
	        hint_text:"enter no.of acers"
		Button: 
			text: "Go to Screen 2"
			on_press: 
				app.calc()
				root.manager.current = 'screen_two'
		    

<ScreenTwo>: 



""")


# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass



# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))



# Create the App class
class ScreenApp(App):
    def build(self):
        return screen_manager

    def calc(self):
       try:
        weight=self.root.get_screen("screen_one").ids.weight.text
        bags= self.root.get_screen("screen_one").ids.bags.text
        acers=self.root.get_screen("screen_one").ids.acers.text
        total_weight = int((int(weight) - int(bags)) / 75)/(int(acers))
        print(int(total_weight))
        self.root.get_screen("screen_two").add_widget(Label(text=str(int(total_weight)),on_press=self.change))
       except:
         pass

    def change(self):
        self.root.get_screen("screen_two").current="first_screen"

sample_app = ScreenApp()
sample_app.run()
