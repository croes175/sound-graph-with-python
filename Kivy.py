from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# Archivos complementarios

import numpy as np
import pygame 
from kivy.properties import StringProperty
import datetime
import simpleaudio
import time
import matplotlib.pyplot as plt


pygame.mixer.init(44100,-16,2,512)
pygame.mixer.init()



# Create the manager

# Add few screens

# By default, the first screen added into the ScreenManager will be
# displayed. You can then change to another screen.

# Let's display the screen named 'Title 2'
# A transition will automatica


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
       
        self.param=GridLayout()
        self.titulo=Label(text='Frecuency value', pos=(300,100))
        self.param.add_widget(self.titulo)
        self.username = TextInput(multiline=False,pos=(300,200))
        self.param.add_widget(self.username)
        self.param.add_widget(Label(text='Amplitud'))
        self.amplitud = TextInput(multiline=False)
        self.param.add_widget(self.amplitud)
        self.button=Button(text ="Push Me !",size =(100, 100), pos=(100,100))
        self.button.bind(on_press = self.callback)
        self.param.add_widget(self.button)
        self.button1=Button(text ="Tono !!",size =(100, 100),pos=(400,400))
        self.button1.bind(on_press = self.tono)
        self.param.add_widget(self.button1)
        self.button2=Button(text ="Exit",size =(100, 100),pos=(600,100))
        self.button2.bind(on_press = self.exit)
        self.param.add_widget(self.button2)
        self.add_widget(self.param)
        



    def tono(self,event):

        try:

            fre=int(self.username.text)
            amp=int(self.amplitud.text)
        except:
            return

        fs=44100
        T=0.25

        
        b=np.linspace(0,1 , int(fs*T))
        b=T*b

        senal=(amp*4096*np.cos(2*np.pi*b*fre)).astype(np.int16)
       
       
        senal2=np.c_[senal,senal]
        
        sound = pygame.sndarray.make_sound(senal2)
        sound.play(-1)
        pygame.time.delay(1000)
        sound.stop()

       
        fig, ax = plt.subplots()
        

        ax.stem(b, senal)
        plt.show()
        
        time.sleep(1)


    def callback(self,event):
        
        print("hola mundo")
        print(self.username.text)
        pygame.mixer.Sound('latigo_sheldon_cooper_big_bang_theory.wav').play()

    def exit(self,event):
        
        sm.current='Intro'
        
class Intro(Screen): 
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)
       
        self.button=Button(text =" INICIO",size =(1, 1),pos=(10,10))
        self.button.bind(on_press = self.exit)
        self.add_widget(self.button)
    def exit(self,event):
        sm.current='menu'
        



sm = ScreenManager()
sm.add_widget(LoginScreen(name='menu'))   
sm.add_widget(Intro(name='Intro'))
  


class MyApp(App):
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
   
    def build(self):

        return sm




if __name__ == '__main__':
     MyApp().run()


       
        

