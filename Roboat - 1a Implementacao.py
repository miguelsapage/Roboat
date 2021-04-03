"""
Projeto CP - 2020/2021

Roboat - 1ª Implementação

Autor: Miguel Sapage (96291)
Engenharia Mecânica
"""

from graphics import *
from classes import *
from math import *
        
def main():
    #Piscina
    win = GraphWin("Roboat",650,500)
    win.setCoords(0, 0, 100, 100)
    win.setBackground("blue")
    
    #Desenha os objetos e devolve as variáveis necessárias
    op1i = Open()
    pointer, icenter, xr, yr, quitbutton, r, robo, cx, cy = op1i.ambienteobjetos(win)
    
    #Colocação das impurezas
    while True:
        p = win.getMouse()
        sair = quitbutton.interact(p)
        if sair == "Quit":
            break
        px,py = p.getX(),p.getY()
        v = r.verifydist(icenter, px, py, 4)
        #Não premite impurezas dentro dos objetos
        if v == True or (px<12 and 18<py<27) or dist((xr,yr),(px,py))<2.5 or px<3 or px>97 or py<3 or py>97 or (px>92 and py<8):
            pass
        else:
            p.draw(win)
            r.leavecais(robo, pointer)
            pointer = r.move(win, robo, pointer, p, px, py, icenter, 5.5)
            pointer = r.moveback(win, robo, pointer, cx, cy, icenter, 5.5)
            
    win.close()
main()