from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class Test(App):
    def build(self):
        box = BoxLayout(orientation="vertical")

        """
        Trabalharemos com eventos em nossos botões!
        on_release => quando o botão for 'solto' a função será executada
        on_press => quando o botão for pressionado, a função será executada
        """

        button = Button(text='Botão 1',font_size=30,on_release=self.incrementar)
        self.label = Label(text="1",font_size=30)

        box.add_widget(button)
        box.add_widget(self.label)


        return box
        
    def incrementar(self,button):
        button.text = "soltei"
        valor = int(self.label.text)
        self.label.text = str(valor + 1) 


        
    
Test().run() 