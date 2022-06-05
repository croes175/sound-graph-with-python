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
from kivy.clock import Clock

from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


# Archivos complementarios

import numpy as np
import pygame 
from kivy.properties import StringProperty
import datetime
import simpleaudio
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter

from scipy.signal import get_window


import threading


pygame.mixer.init(44100,-16,2,512)






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
    #  Declarate the screen variables 
    sliderF = ObjectProperty(None)
    sliderA = ObjectProperty(None)
    sliderP = ObjectProperty(None)
    image=ObjectProperty(None)
    Prueba=ObjectProperty(None)


    def on_touch_up(self,touch):

        print(touch.button)
        self.grafica()



    




    resolucion_f=0
    resolucion_a=0

    root="read.png"



    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.t1 = threading.Thread(target=self.grafica)

        self.f=0

        #Clock.schedule_interval(self.callback_time, 2)




    
        


    



    def tono(self):

        senal2= 100*(self.grafica())
        
        
        sound = pygame.sndarray.make_sound(senal2)
        sound.play(-1)
        pygame.time.delay(1000)
        sound.stop()

    def ventana(self,m):

        a=self.ids.ventana1.text

        if a== 'windows':
            a='hamming'
        
        w = get_window(a, m)
        return w


    def resolucion(self,res,amp,fre):

        a=self.resolucion_f
        b=self.resolucion_a

        if a==0 or amp > a or a> 2*amp:
            a=2*amp
       
        if b==0 or fre>b or b>2*fre :
            b=2*fre
            
        self.resolucion_a=b
        self.resolucion_f=a
        
        return b,a

        



        
        # En esta parte hacemos el autoescalamiento de la señal
        Fres=((fre//res)+1)*res
        Ares=((amp//res)+1)*res
        return Fres,Ares


        



       


    def grafica(self):

        

        print(self.sliderP.value)

        try:

            fre=int(self.sliderF.value)
            amp=int(self.sliderA.value)
            fase=float(self.sliderP.value)

            if amp==0:
                raise 
            

        except Exception as e:
            print(e)
            print("Error")
            return


        fs=44100
        T=0.25

       

        
        
        b = np.arange(0, 1, step=1/fs)

        L=b.size

        

        senal=(amp*np.cos(2*np.pi*b*fre+fase)).astype(np.int16)
       
       
        senal2=np.c_[senal,senal]
        

       
        fig, ax = plt.subplots(2)

        # Señal En tiempo

     

        # Señal en Frecuencia



        Fres,Ares=self.resolucion(100,amp,fre)

        print(Fres,Ares,"resolucion")




        


        # Tecnica de ventaneado

        

        
        senal=(amp*np.cos(2*np.pi*b*fre+fase)).astype(np.double)

        

        ax[0].set_ylim(-Ares,Ares)

    
        ax[0].plot(b,senal)

        windows= self.ventana(L)
        senal_w=senal*windows


        fy=np.abs(np.fft.fft(senal_w))/L

         #fy=10*np.log(fy)no es necesario usar ventaneo

        # Es necesario Centrar la frecuencia ya que el calculo inicial de la FFT o Transformada discreta conlleva a eso

        fy=np.fft.fftshift(fy)

        
        xy=np.linspace(-fs/2,fs/2 , len(fy))



        ax[1].set_xlim(-Fres,Fres)

        ax[1].set_ylim(-100,100)

        ax[1].plot(xy,fy)

        plt.savefig('Formato.png')


        self.image.source='Formato.png'
        self.image.reload()

        

        plt.close()
        
        return senal2
        


    def callback(self):
        
        
        print(self.username.text)
        pygame.mixer.Sound('latigo_sheldon_cooper_big_bang_theory.wav').play()

    def callback_time(self,a):
        if (sm.current=="menu"):
            
            self.grafica()

            
        else:
            pass 
            
            
        
    def exit(self,a):
        sm.current="Intro"

    def animar(self):

        self.ids.image.anim_delay = 0.10
        self.ids.image._coreimage.anim_reset(True)
        




        
class Intro(Screen):
    pass




        
class Redes(Screen):

    def __init__(self,**kwargs):
        super(Intro, self).__init__(**kwargs)
        
        


class MyApp(App):
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()
   
    def build(self):

        global sm
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='menu'))   
        sm.add_widget(Intro(name='Intro'))
        return sm




if __name__ == '__main__':
     a= MyApp()
     a.run()


       
        

