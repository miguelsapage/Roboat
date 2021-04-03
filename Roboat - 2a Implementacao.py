"""
Projeto CP - 2020/2021

Roboat - 2ª Implementação

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
    op2i = Open()
    pointer, icenter, xr, yr, quitbutton, r, robo, cx, cy = op2i.ambienteobjetos(win)
    cleanbutton, i2center = op2i.objadd2i(win)
    
    #Juntar todos os centros das ilhas numa só lista
    icenter.extend(i2center)
    
    #Colocação das impurezas
    points, pointscoordx, pointscoordy= [], [], []
    while True:
        p = win.getMouse()
        sair = quitbutton.interact(p)
        limpar = cleanbutton.interact(p)
        if sair == "Quit":
            break
        elif limpar == "Clean":
            pointer, points, pointscoordx, pointscoordy = r.normalmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
        px,py = p.getX(),p.getY()
        v = r.verifydist(icenter, px, py, 4)
        #Não premite impurezas dentro dos objetos
        if v == True or (px<12 and 18<py<27) or dist((xr,yr),(px,py))<2.5 or px<3 or px>97 or py<3 or py>97 or (px>81 and py<8):
            pass
        else:
            p.draw(win)
            points.append(p)
            pointscoordx.append(p.getX())
            pointscoordy.append(p.getY())                                        
        
    win.close()
main()