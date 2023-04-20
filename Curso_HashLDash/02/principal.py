from kivy.app import App
from kivy.uix.button import Button
#para garantir uma boa organização dos elementos, usaremos um Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class Test(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        button = Button(text='Botão 1')
        label = Label(text="Texto 1")
        """
        Por padrão, os elementos são inseridos da esquerda pra direita pela ordem
        que são adicionados no BoxLayout
        mas podemos trocar isso adicionando o parâmetro orientation = 'vertical'
        """

        box.add_widget(button)
        box.add_widget(label)


        #podemos trabalhar com mais de um layout ao mesmo tempo, usando a tecnica de empacotamento

        box2 = BoxLayout()
        button2 = Button(text="Botão 2")
        label2 = Label(text="Texto2")

        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        return box
    
Test().run()