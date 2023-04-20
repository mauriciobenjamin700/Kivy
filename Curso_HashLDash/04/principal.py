from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#trabalharemos com linguagem Kivy agora para melhorar nossos layouts
class Incrementador(BoxLayout):
    """
    Esta classe será desenvolvida no arquivo .'kv' 
    detalhe: o nome do arquivo '.kv' deve ser todo em minúsculo e igual ao nome do aplicativo
    #neste caso nossa classe tem o nome de 'Incrementador' logo no arquivo '.kv' deve ser chamado de "test.kv", dentro do arquivo 'test.kv' existe uma <incrementador> que se refere a esta classe Incrementador que estamos trabalhando
    """
    pass

class Test(App):
    def build(self):
        

        return Incrementador()
        

        
    
Test().run() 