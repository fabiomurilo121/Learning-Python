from kivy.app import App
from kivy.uix.button import Button
#Tkinter
class Teste(App): #herda as funcionalidade
    def build(self): #Inicializa e constroi o aplicativo
        return Button(text = 'Ola mundo')

#instanciando a classe

Teste().run()