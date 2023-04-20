from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#Layouts Dinâmicos

class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs): #**kwargs -> keyword arguments --> letra == a, etc... Podemos entender **kwargs como um dicionário que recebe os todos os parâmetros que passamos e tenta levalos para suas respectivas posições corretas, tipo quando se usarmos tarefas=tarefas, estamos especificando o parâmetro que vai receber o valor de tarefas
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa,font_size=30))

class Test(App):
    def build(self):
        return Tarefas(['Fazer Compras','Buscar Filho','Lavar a calçada'],orientation='horizontal') #usando **kwargs podemos passar a orientação e modifica quando quizer já que ele entende onde deve colocalo e ajusta automaticamente para nós
    
if __name__ == '__main__':
    aplicativo = Test()
    aplicativo.run()