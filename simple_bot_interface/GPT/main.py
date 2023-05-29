from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Bot(Screen):
    def ligar_bot(self):
        pass

    def desligar_bot(self):
        pass

class Config(Screen):
    def fa(self):
        pass

    def fb(self):
        pass

class MyApp(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    MyApp().run()
