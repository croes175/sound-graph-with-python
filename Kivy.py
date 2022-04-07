from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

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


def prueba():
    print("Prueba 1")


class LoginScreen(Screen):

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
        
        
        print(self.username.text)
        pygame.mixer.Sound('latigo_sheldon_cooper_big_bang_theory.wav').play()

    def exit(self,event):
        
        sm.current='Intro'
        
class Intro(Screen): 
    def __init__(self, **kwargs):
        super(Intro, self).__init__(**kwargs)
        self.total=BoxLayout()
        self.button=Button(text =" Señales",size =(1, 1),pos=(10,10))
        self.button.bind(on_press = self.exit)
        self.total.add_widget(self.button)
        self.add_widget(self.total)
    def exit(self,event):
        sm.current='menu'
        
class Redes(Screen):

    def __init__(self,**kwargs):
        super(Intro, self).__init__(**kwargs)
        
        


sm = ScreenManager()
sm.add_widget(LoginScreen(name='menu'))   
sm.add_widget(Intro(name='Intro'))
sm.add_widget(
  


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


       
        

