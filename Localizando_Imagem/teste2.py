from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Color, Rectangle


class ImageSelector(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageSelector, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        # Crie uma caixa (BoxLayout) para o cabeçalho com o logotipo e o título
        header_box = BoxLayout(size_hint=(1, 0.1))
        header_box.padding = [10, 10]
        header_box.spacing = 10
        
        # Adicione o logotipo
        logo = AsyncImage(source='logo.png')
        logo.size_hint = (None, 1)
        logo.width = 30
        header_box.add_widget(logo)
        
        # Adicione o título
        title_label = Label(text='Google Drive', font_size='20sp', color=[0, 0, 0, 1])
        header_box.add_widget(title_label)
        
        self.add_widget(header_box)
        
        # Crie uma caixa (BoxLayout) para o seletor de arquivos com o ícone e o nome do arquivo selecionado
        file_box = BoxLayout(size_hint=(1, 0.9))
        file_box.padding = [10, 10]
        file_box.spacing = 10
        
        # Adicione o widget de seleção de arquivo com o estilo do Google Drive
        file_chooser = FileChooserIconView(path=os.getcwd())
        file_chooser.filters = ['*.jpg', '*.jpeg', '*.png']
        file_chooser.thumb_size = 150
        file_chooser.size_hint = (0.7, 1)
        file_chooser.pos_hint = {'x': 0, 'y': 0}
        file_box.add_widget(file_chooser)
        
        # Adicione o widget de visualização do arquivo selecionado
        preview_box = FloatLayout(size_hint=(0.3, 1))
        preview_box.canvas.before.add(Color(0.5, 0.5, 0.5, 1))
        preview_box.canvas.before.add(Rectangle(pos=preview_box.pos, size=preview_box.size))
        file_box.add_widget(preview_box)
        
        # Adicione o widget de nome do arquivo selecionado
        selected_file_label = Label(text='Nenhum arquivo selecionado', font_size='16sp', color=[0, 0, 0, 1])
        selected_file_label.size_hint = (1, 0.1)
        selected_file_label.pos_hint = {'x': 0, 'y': 0.9}
        preview_box.add_widget(selected_file_label)
        
        # Adicione o widget de miniatura do arquivo selecionado
        selected_file_preview = AsyncImage()
        selected_file_preview.size_hint = (0)

class MyApp(App):
    def build(self):
        return ImageSelector()

if __name__ == '__main__':
    MyApp().run()