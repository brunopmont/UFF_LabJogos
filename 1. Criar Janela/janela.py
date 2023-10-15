from PPlay.window import *
from PPlay.gameimage import *

janela = Window(600, 300)
janela.set_title('Bruno Porto Monteiro')
janela.set_background_color((200, 45, 45))

fundo = GameImage("kanyegoat.jpg")

while True:
    janela.update()
    fundo.draw()