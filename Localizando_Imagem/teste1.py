# Importe as bibliotecas necessárias:
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView


#Crie uma classe para a sua tela:


class ImageSelector(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageSelector, self).__init__(**kwargs)

        #Adicione widgets à sua tela:

        self.orientation = 'vertical'
        
        # label para o título da tela
        self.title_label = Label(text='Selecione a imagem')
        self.add_widget(self.title_label)
        
        # widget de seleção de arquivo
        self.file_chooser = FileChooserListView(path=os.getcwd())
        self.add_widget(self.file_chooser)
        
        # botão para confirmar a seleção
        self.select_button = Button(text='Selecionar')
        self.select_button.bind(on_press=self.select_image)
        self.add_widget(self.select_button)
        
        # widget de visualização do diretório selecionado
        self.directory_label = Label(text='')
        self.add_widget(self.directory_label)

#Crie uma função para tratar o evento de seleção do arquivo:

    def select_image(self, instance):
        self.directory_label.text = self.file_chooser.selection[0]

#Crie a classe principal do seu aplicativo e defina a sua tela como a sua interface gráfica:

class MyApp(App):
    def build(self):
        return ImageSelector()

if __name__ == '__main__':
    MyApp().run()
