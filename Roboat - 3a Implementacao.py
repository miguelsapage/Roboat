"""
Projeto CP - 2020/2021

Roboat - 3ª Implementação

Autor: Miguel Sapage (96291)
Engenharia Mecânica
"""

from graphics import *
from classes import *
from math import *

def main():         
    #Escolha de colocação dos obstáculos
    obstaculos = Escolha3I()
    obschoice = obstaculos.interact()
    
    if obschoice == "Aleatório":
        obstaculos.close()
        
        #Piscina
        win = GraphWin("Roboat",650,500)
        win.setCoords(0, 0, 100, 100)
        win.setBackground("blue")
        
        #Desenha os objetos e devolve as variáveis necessárias
        op3i = Open()
        pointer, icenter, xr, yr, r, robo, cx, cy = op3i.open3i(win)
        
    elif obschoice == "Ler Ficheiro":
        obstaculos.close()
        #Lê o ficheiro e cria ambiente
        op3i = Open()
        win, cx, cy, icenter = op3i.readfile3I()
        
        #Desenha o roboat
        r = Roboat()
        xr, yr = r.roboposcais(cx,cy)
        robo = r.roboposie(win,xr,yr)
        pointer = r.pointerie(win,xr,yr,cx,cy)
    
    #Botões + Menu impurezas
    quitbutton, cleanbutton, imp, impchoice = op3i.BteMenu3i(win)
    
    while True:
    #Regressa ao menu de impurezas após terminar limpar impurezas lidas de ficheiro
        if impchoice == "Quit":
            imp.close()
            break
        elif impchoice == "Clicks no Rato":
            #Guarda os pontos clicados e as suas coordenadas
            points, pointscoordx, pointscoordy= [], [], []
            imp.close()
            while True:
                p = win.getMouse()
                sair = quitbutton.interact(p)
                limpar = cleanbutton.interact(p)
                if sair == "Quit":
                    break
                elif limpar == "Clean":
                #O método move usado é diferente conforme a primeira escolha 
                    if obschoice == "Aleatório":
                        pointer, points, pointscoordx, pointscoordy = r.normalmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
                    elif obschoice == "Ler Ficheiro":
                        pointer, points, pointscoordx, pointscoordy = r.altmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
                px,py = p.getX(),p.getY()
                v = r.verifydist(icenter, px, py, 4)
                #Não premite impurezas dentro dos objetos
                if (px<cx+7 and cy-7<py<cy+7) or dist((xr,yr),(px,py))<2.5 or px<3 or px>97 or py<3 or py>97 or (px>81 and py<8) or v == True:
                    pass
                else:
                    p.draw(win)
                    points.append(p)
                    pointscoordx.append(p.getX())
                    pointscoordy.append(p.getY())
    
        elif impchoice == "Ler Ficheiro":
            imp.close()
            #Guarda os pontos clicados e as suas coordenadas
            points, pointscoordx, pointscoordy= [], [], []
            imp.readfile(win, r, icenter, xr, yr, points, pointscoordx, pointscoordy, cx, cy)
            while True:
                p = win.getMouse()
                sair = quitbutton.interact(p)
                limpar = cleanbutton.interact(p)
                if sair == "Quit":
                    break
                elif limpar == "Clean":
                #O método move usado é diferente conforme a primeira escolha
                    if obschoice == "Aleatório":
                        pointer, points, pointscoordx, pointscoordy = r.normalmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
                    elif obschoice == "Ler Ficheiro":
                        pointer, points, pointscoordx, pointscoordy = r.altmove(win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx,cy)
                    break
        imp = Impurezas()
        impchoice = imp.interact()
        
    win.close()
main()