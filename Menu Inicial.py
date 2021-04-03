"""
Projeto CP - 2020/2021

Roboat - Menu Inicial

Autor: Miguel Sapage (96291)
Engenharia Mecânica
"""

from graphics import *
from button import Button
from classes import *
from math import *

class Options():
    def __init__(self,win):
        #Botões de opção de implantações
        self.i1 = Button(win,Point(50,80),50,10,"1ª Implementação")
        self.i1.activate()
        self.i2 = Button(win,Point(50,60),50,10,"2ª Implementação")
        self.i2.activate()
        self.i3 = Button(win,Point(50,40),50,10,"3ª Implementação")
        self.i3.activate()
        self.quit = Button(win,Point(50,20),20,10,"Sair")
        self.quit.activate()
    
    def interact(self,win):
        while True:
            p = win.getMouse()
            px,py = p.getX(),p.getY()
            if self.quit.clicked(p):
                return "Quit"
            elif self.i1.clicked(p):
                return "1ª Implementação"
            elif self.i2.clicked(p):
                return "2ª Implementação"
            elif self.i3.clicked(p):
                return "3ª Implementação"
            elif dist((px,py),(5,5))<=3:
                return "Extra"
            else:
                return "Stay"
    
    def close(self,win):
        win.close()
        
        
#Menu inicial
def main():
    #Volta ao menu inicial no fim de o jogo correr
    while True:
        win = GraphWin("Menu inicial",300,300)
        win.setCoords(0, 0, 100, 100)
        win.setBackground(color_rgb(255,150,20))
        extra = Circle(Point(5,5), 3).draw(win)
        extra.setFill(color_rgb(255, 140, 30))
        extra.setOutline(color_rgb(255, 140, 30))
                
        op = Options(win)
        choice = op.interact(win)
        op.close(win)  #Fecha a janela enquanto o jogo está a correr
        if choice == "1ª Implementação":
            exec(compile(open("Roboat - 1ª Implementação.py", "rb").read(), "Roboat - 1ª Implementação.py", 'exec'))
        elif choice == "2ª Implementação":
            exec(open("Roboat - 2ª Implementação.py").read())
        elif choice == "3ª Implementação":
            exec(compile(open("Roboat - 3ª Implementação.py", "rb").read(), "Roboat - 3ª Implementação.py", 'exec'))
        elif choice == "Extra":
            exec(compile(open("Roboat - Extra.py", "rb").read(), "Roboat.py", 'exec'))
        elif choice == "Quit":
            break
        
    win.close()
main()