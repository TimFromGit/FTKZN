from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.button import Button


from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 640)

# fon color
from kivy.core.window import Window
Window.clearcolor = (0, 0, 0, 0)
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<BoxLayout>:
    orientation: "vertical"
    spacing: 2
<GridLayout>:
    cols: 2
    padding: 3
    spacing: 3
    size: root.size
<TextInput>:
    size_hint: (1,0.2)
    multiline: False
<Label>:
    size_hint: (1,0.2)

<MenuScreen>:
    BoxLayout:
        GridLayout:
            size_hint: (1,0.2)
            Image: 
                source: 'img/log.jpg'
                size_hint: (0.1,1)
            Label:
                text:'Welcome to FriendsTravel!'
        TextInput:
            hint_text: "Enter your login"
        TextInput:
            hint_text: "Enter your password"
            password: True
        GridLayout:
            size_hint: (1,0.25)
            Button:
                text: "Enter"
            Button: 
                text: "Registration"
        Label:
            text: "Nearest taravel:"
            size_hint: (1,0.15)
        Image: 
            source: 'img/img2.jpg'
        GridLayout:
            Button: 
                text: "Travels"
                on_press:
                    root.manager.current="travels"
                    root.manager.transition.direction = 'left'
            Button: 
                text:"Rent equipment"           
            Button: 
                text:"Photo"
                on_press:
                    root.manager.current="photo"
                    root.manager.transition.direction = 'left'
            Button: 
                text:"Articles"     
            Button: 
                text:"Chat"
            Button: 
                text:"Remarks"

<Travels>:
    BoxLayout:
        Image:
            source: 'img/travels.jpg'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'
            size_hint: (1,0.1)

""")

class ScreenManager(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Travels(Screen):
    pass

class Photo(Screen):	
	def __init__(self, **kwargs):
		super(Photo, self).__init__(**kwargs)
		
		self.bl=BoxLayout(orientation="vertical")

		carousel = Carousel(loop=True)
		for i in range(3):
			src = "img/f%d.jpg" % i
			image = Factory.AsyncImage(source=src, allow_stretch=True)
			carousel.add_widget(image)
		self.btn = Button(text="Back to menu", on_press=lambda x: set_screen('menu'), size_hint = (1,0.1))
		self.bl.add_widget(carousel)
		self.bl.add_widget(self.btn)
		self.add_widget(self.bl)


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Travels(name='travels'))
sm.add_widget(Photo(name='photo'))

def set_screen(name_screen):
    sm.current = name_screen


class FriendsTravelApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    FriendsTravelApp().run()