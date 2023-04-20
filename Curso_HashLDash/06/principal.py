from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

#6 - Python Kivy - ScrollView e Size Hints!

class Tarefas(ScrollView):
    def __init__(self,tarefas,**kwargs): #**kwargs -> keyword arguments --> letra == a, etc... Podemos entender **kwargs como um dicionário que recebe os todos os parâmetros que passamos e tenta levalos para suas respectivas posições corretas, tipo quando se usarmos tarefas=tarefas, estamos especificando o parâmetro que vai receber o valor de tarefas
        super().__init__(**kwargs)

        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa,font_size=30,size_hint_y=None,height=200))

class Test(App):
    def build(self):
        return Tarefas(['Fazer Compras','Buscar Filho','Lavar a calçada','Pagar Contas','Ir Trabalhar','Terminar Curso', 'Cobrar Assistente'])
    
if __name__ == '__main__':
    aplicativo = Test()
    aplicativo.run()