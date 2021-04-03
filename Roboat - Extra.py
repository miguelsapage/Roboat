"""
Projeto CP - 2020/2021

Roboat - Implementação Extra

Autor: Miguel Sapage (96291)
Engenharia Mecânica
"""

from graphics import *
from random import random, randrange
from classes import *
from math import *

def main():
        #Piscina
        win = GraphWin("Roboat",650,500)
        win.setCoords(0, 0, 100, 100)
        win.setBackground("blue")
        
        
        caischoice = Cais()
        choice = caischoice.interact()
        
        #Localização do cais
        if choice == "Aleatório":
            caischoice.close()
            cx, cy = caischoice.randomloc()
            #Desenho o cais e devolve as variáveis necessárias
            rx, ry = caischoice.caisaleatie(win, cx, cy)         
        elif choice == "Escolher":
            #Escolha da localização pelo utilizador
            caischoice.close()
            #Desenho o cais e devolve as variáveis necessárias
            cx, cy, rx, ry = caischoice.caisescolherie(win)
        
        #Desenha os objetos e devolve as variáveis necessárias
        opie = Open()
        r, robo, pointer, icenter, quitbutton, cleanbutton = opie.openie(win, rx, ry, cx, cy)
        
        #Colocação das impurezas
        points, pointscoordx, pointscoordy= [], [], []
        while True:
            p = win.getMouse()
            sair = quitbutton.interact(p)
            limpar = cleanbutton.interact(p)
            if sair == "Quit":
                break
            elif limpar == "Clean":
                pointer, points, pointscoordx, pointscoordy = r.altmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
            px,py = p.getX(),p.getY()
            v = r.verifydist(icenter, px, py, 4)
            #Não premite impurezas dentro dos objetos
            if (cx-7<px<cx+7 and cy-9<py<cy+9) or px<3 or px>97 or py<3 or py>97 or (px>81 and py<8) or v == True:
                pass
            else:
                p.draw(win)
                points.append(p)
                pointscoordx.append(p.getX())
                pointscoordy.append(p.getY())
            
        win.close()
main()