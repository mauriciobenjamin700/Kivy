from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class Menu(Screen):
    """
    No menu haverá 3 botões:
        1 - Bot
            1.1 Botão Ligar Bot
            1.2 Botão Desligar bot
            1.3 Label com timer iniciando de 0:0 até a hora que o bot achou o resultado ou for parado manualmente
            1.4 Voltar ao menu
        
        2 - Configurações do bot
            Em faze de análise ainda

        3 - Botão Sair
    """      
    pass

class Bot(Screen):
    pass


class Gerenciador(ScreenManager):
    pass

class Aplicativo(App):
    def build(self):
        return Gerenciador()
    

if __name__ == '__main__':
    aplicativo = Aplicativo()
    aplicativo.run()