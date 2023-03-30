import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import pyttsx3 as pt

kivy.require('2.0.0')

class screenone(Screen):
    def __init__(self,**kwargs):
        super(screenone,self).__init__(**kwargs)
        layout_screen1=BoxLayout(orientation='vertical')
        layout_screen1.size_hint=(1,0.3)
        with self.canvas.before:
            self.background = Image(source='"C:/Users/Admin/Desktop/51220e108642081.5fc25721cd382.jpg"', allow_stretch=True, keep_ratio=False)
            self.bind(size=self._update_background, pos=self._update_background)
        image_start=Image(source="C:\\Users\\Admin\\Desktop\\naruto-shippuden-akatsuki-itachi-uchiha-wallpaper-720x1280_184.jpg",size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        button_start=Button(text="start",bold=True)
       # button_start.bind(on_press=self.speak)
        #layout_screen1.add_widget(image_start)
        layout_screen1.add_widget(button_start)

        self.add_widget(layout_screen1)

    def _update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

       # def speak(self,*args):
           # engine=pt.init()
            #engine.say("hello")
           # engine.runAndWait()


class NeuralRandom(App):
    def build(self):
        screenmanager=ScreenManager()

        screenmanager.add_widget(screenone(name="screen-one"))
        # label=Label(text="NeuralRandom")
        # layout1 = BoxLayout(orientation='vertical',spacing=10,padding=20)
        # #label=Label(text="hello",pos=(0,0),bold=True,color=(1,0,0,1),font_size=22)
        # image=Image(source="C:/Users/Admin/Desktop/51220e108642081.5fc25721cd382.jpg")
        # layout=BoxLayout(orientation='horizontal')
        # button=Button(text="click")
        # button1=Button(text="goes")
        # button2=Button(text="went")
        # layout.add_widget(button1)
        # layout.add_widget(button)
        # layout.add_widget(button2)
        #
        # #layout1.size_hint(0.5,0.5)
        # layout1.add_widget(layout)
        # layout1.add_widget(image)
        # return(label)
        #
        # #return(layout1)
        return screenmanager


neuralRandom=NeuralRandom()
neuralRandom.run()
