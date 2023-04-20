from kivy.app import App
from kivy.uix.button import Button

#classe que representa o aplicativo
class Test(App):
    #função build irá ser disparada ao iniciar o aplicativo
    def build(self):
        #joga na interface 'Test' os elementos retornados
        return Button(text="Olá Mundo!!")
    
Test().run()