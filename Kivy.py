from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.lang import Builder
import kivy
from kivy.uix.scatter import Scatter
import io
from kivy.core.image import Image as CoreImage
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





class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)

    def imagenes():
        pass
        
        

    



class LoginScreen(Screen):

    root="read.png"

    



    def tono(self,Frecuency,Amplitud,image):

        print(image)

        

        try:

            fre=int(Frecuency)
            amp=int(Amplitud)
            print(amp)
            print(fre)
        except Exception as e:
            print(e)
            print("Error")
            return

        fs=44100
        T=0.25

        
        b=np.linspace(0,1 , int(fs*T))
        b=T*b

        senal=(amp*np.cos(2*np.pi*b*fre)).astype(np.int16)
       
       
        senal2=np.c_[senal,senal]
        
        sound = pygame.sndarray.make_sound(senal2)
        sound.play(-1)
        pygame.time.delay(1000)
        sound.stop()

       
        fig, ax = plt.subplots(2)

        # Señal En tiempo

        ax[0].stem(b, senal)

        # Señal en Frecuencia


        fy=np.abs(np.fft.fft(senal))
        xy=np.linspace(-fs/2,fs/2 , len(fy))


        ax[1].stem(xy,fy)


        
        


        

        
      
        plt.savefig('Formato.png')
        
        image.source='Formato.png'
        image.reload()

        plt.close()
        


    def callback(self):
        
        
        print(self.username.text)
        pygame.mixer.Sound('latigo_sheldon_cooper_big_bang_theory.wav').play()

    def exit(self):
        
        sm.current='Intro'
        
class Intro(Screen): 

    def exit(self):
        sm.current='menu'
        
class Redes(Screen):

    def __init__(self,**kwargs):
        super(Intro, self).__init__(**kwargs)
        
        


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
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='menu'))   
        sm.add_widget(Intro(name='Intro'))
        return sm




if __name__ == '__main__':
     a= MyApp()
     a.run()


       
        

