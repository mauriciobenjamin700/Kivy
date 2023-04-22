from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

#9 - Python Kivy - Múltiplas telas com ScreenManager

class Gerenciador(ScreenManager):
    pass

class Tarefas(Screen):
    def __init__(self,tarefas=[],**kwargs): #**kwargs -> keyword arguments --> letra == a, etc... Podemos entender **kwargs como um dicionário que recebe os todos os parâmetros que passamos e tenta levalos para suas respectivas posições corretas, tipo quando se usarmos tarefas=tarefas, estamos especificando o parâmetro que vai receber o valor de tarefas
        super().__init__(**kwargs)

        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def addwidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''


class Tarefa(BoxLayout):
    def __init__(self, text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text 

class Test(App):
    def build(self):
        #return Tarefas(['Fazer Compras','Buscar Filho','Lavar a calçada','Pagar Contas','Ir Trabalhar','Terminar Curso', 'Cobrar Assistente'])
        return Gerenciador()
if __name__ == '__main__':
    aplicativo = Test()
    aplicativo.run()

"""
Formas de Referencias no arquivo KV
root
self
self.parents

"""