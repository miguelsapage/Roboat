"""
Projeto CP - 2020/2021

Roboat - Classes

Autor: Miguel Sapage (96291)
Engenharia Mecânica
"""

from math import *
from graphics import *
from button import Button
from random import random, randrange
from time import sleep
import numpy as np
import re

class Cais:
    def __init__(self):
        
        self.win = win = GraphWin("Cais",200,200)
        win.setCoords(0,0,100,100)
        
        #Janela de opção de localização do cais
        Text(Point(50,90), "Deseja escolher a").draw(win)
        Text(Point(50,83), "localização do cais?").draw(win)
        
        self.aleat = Button(win,Point(50,60),35,10,"Aleatório")
        self.aleat.activate()
        
        self.choose = Button(win,Point(50,25),35,10,"Escolher")
        self.choose.activate()
    
    def deflocc(self,win):
        #Cais com posição fixa
        self.cais = Rectangle(Point(0,25),Point(10,20)).draw(win)
        self.cais.setFill("brown")
        cx, cy = self.cais.getCenter().getX(), self.cais.getCenter().getY()
        return cx, cy
        
    def randomloc(self):
        #Localização aleatória
        if random() < 0.5:
            xcoord = randrange(5,95)
            x = float(xcoord)
            if x == 5 or x == 95:
                ycoord = randrange(6,94)
                y = float(ycoord)
            else:
                if random() < 0.5:
                    y = 6
                else:
                    y = 94
        else:
            ycoord = randrange(6,94)
            y = float(ycoord)
            if y == 6 or y == 94:
                xcoord = randrange(5,95)
                x = float(xcoord)
            else:
                if random() < 0.5:
                    x = 5
                else:
                    x = 95
        return x, y
    
    def interact(self):
        #Botões de decisão da posição do cais
        while True:
            p = self.win.getMouse()
            if self.aleat.clicked(p):
                return "Aleatório"
            if self.choose.clicked(p):
                return "Escolher"
    
    def caisescolherie(self, win):
        aviso = Text(Point(50,50), "Escolha um ponto sobre a linha!!").draw(win)
        limite = Rectangle(Point(5,6), Point(95,94)).draw(win)
        #Garantia de um cais na posição correta
        while True:
            p = win.getMouse()
            #Garantia de um cais com proporções constantes
            if 4.8<p.getX()<5.2 or 94.8<p.getX()<95.2:
                cais = Rectangle(Point((p.getX()-5),(p.getY()+2.5)),Point((p.getX()+5),(p.getY()-2.5)))
                if p.getY() < 50:
                    rx = p.getX()
                    ry = p.getY() + 5.1
                else:
                    rx = p.getX()
                    ry = p.getY() - 5.1
                break
            elif 5.8<p.getY()<6.2 or 93.8<p.getY()<94.2:
                cais = Rectangle(Point((p.getX()-2),(p.getY()+6)),Point((p.getX()+2),(p.getY()-6)))
                if p.getX() < 50:
                    rx = p.getX() + 4.1
                    ry = p.getY()
                else:
                    rx = p.getX() - 4.1
                    ry = p.getY()
                break
        cais.setFill("brown")
        limite.undraw()
        aviso.undraw()
        cais.draw(win)
        
        #Para impedir impurezas dentro do cais e localizar o roboat corretamente
        cc = cais.getCenter()
        cx, cy = cc.getX(), cc.getY()
        
        return cx, cy, rx, ry
    
    def caisaleatie(self, win, xcoord, ycoord):
        #Garantia de um cais com proporções constantes
        if xcoord == 5 or xcoord == 95:
            cais = Rectangle(Point((xcoord-5),(ycoord+2.5)),Point((xcoord+5),(ycoord-2.5)))
            if ycoord <= 50:
                rx = xcoord
                ry = ycoord + 5.6
            else:
                rx = xcoord
                ry = ycoord - 5.6
        else:
            cais = Rectangle(Point((xcoord-2),(ycoord+6)),Point((xcoord+2),(ycoord-6)))
            if xcoord <= 50:
                rx = xcoord + 4.1
                ry = ycoord
            else:
                rx = xcoord - 4.1
                ry = ycoord
        cais.setFill("brown")
        cais.draw(win)  
        
        return rx, ry
    
    def close(self):
        self.win.close()

class Ilha:
    def __init__(self):
        
        self.win = win = GraphWin("Ilhas",200,200)
        win.setCoords(0, 0, 100, 100)
        
        #Janela de opção de número de ilhas
        Text(Point(50,90), "Quantas ilhas").draw(win)
        Text(Point(50,83), "deseja colocar?").draw(win)
        
        self.ok = Button(win,Point(50,25),25,10,"OK")
        self.ok.activate()
        
        self.nilhas = Entry(Point(50,50), 3).draw(win)
        
                
    def getValue(self):
        #Registo do número de ilhas pretendidas
        ni = int(self.nilhas.getText())
        return ni
    
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.ok.clicked(pt):
                return "OK"
    
    def defloci(self,win):
        #Ilhas com posição fixa
        i1 = Circle(Point(10,80), 3).draw(win)
        i2 = Circle(Point(26,76), 3).draw(win)
        i3 = Circle(Point(82,25), 3).draw(win)
        i4 = Circle(Point(75,60), 3).draw(win)
        i5 = Circle(Point(40,52), 3).draw(win)
        i1.setFill("green")
        i2.setFill("green")
        i3.setFill("green")
        i4.setFill("green")
        i5.setFill("green")
        ax, ay = i1.getCenter().getX(), i1.getCenter().getY()
        bx, by = i2.getCenter().getX(), i2.getCenter().getY()
        cx, cy = i3.getCenter().getX(), i3.getCenter().getY()
        dx, dy = i4.getCenter().getX(), i4.getCenter().getY()
        ex, ey = i5.getCenter().getX(), i5.getCenter().getY()
        ilist = [(ax,ay),(bx,by),(cx,cy),(dx,dy),(ex,ey)]
        return ilist
    
    def defloci2(self,win):
        #Ilhas com posição fixa adicionais
        i6 = Circle(Point(57,85), 3).draw(win)
        i7 = Circle(Point(62,57), 3).draw(win)
        i8 = Circle(Point(33,15), 3).draw(win)
        i6.setFill("green")
        i7.setFill("green")
        i8.setFill("green")
        fx, fy = i6.getCenter().getX(), i6.getCenter().getY()
        gx, gy = i7.getCenter().getX(), i7.getCenter().getY()
        hx, hy = i8.getCenter().getX(), i8.getCenter().getY()
        ilist = [(fx,fy),(gx,gy),(hx,hy)]
        return ilist
    
    def aleatloc(self, win, n):
        center = []
        points = []
        for i in range(n):
            #Cria uma ilha
            ilha = self.makeCircle(14, 86, 16, 84, 3)
            point = (ilha.getCenter().getX(), ilha.getCenter().getY())
            #Verifica sobreposição com outras ilhas
            while self.checkOverLap(ilha, center):
                #Cria uma nova ilha
                ilha = self.makeCircle(14, 86, 16, 84, 3)
                point = (ilha.getCenter().getX(), ilha.getCenter().getY())
            #Adiciona as ilhas que não se sobrepõem à lista center
            center.append(ilha)
            points.append(point)
        self.drawIlhas(win, center, n)
        return points
        
    def makeCircle(self, xmin, xmax, ymin, ymax, radius):
        x = randrange(xmin, xmax)
        y = randrange(ymin, ymax)
        ilha = Circle(Point(x, y), radius)
        ilha.setFill("green")
        return ilha
    
    def checkOverLap(self, ilha, array):
    #Se houver sobrposição retorna True
        for ilhacheck in array:
            if dist((ilha.getCenter().getX(),ilha.getCenter().getY()), (ilhacheck.getCenter().getX(),ilhacheck.getCenter().getY()))  < ilha.getRadius() + ilhacheck.getRadius() + 10:
                return True
        return False
    
    def drawIlhas(self, win, array, n):
        for x in range(0, n):
            array[x].draw(win)
            
    def close(self):
        self.win.close()

class Roboat:
    def robopos(self,win):
        #Roboat com posição fixa
        r = Circle(Point(5,17.9),2).draw(win)
        r.setFill("grey")
        pr = r.getCenter()
        return r, pr
    
    def pointer(self,win):
        #Pointer com posição fixa
        p = Polygon(Point(5.7, 18.4),Point(5.7, 17.4),Point(6.9,17.9)).draw(win)
        p.setFill("red")
        return p
    
    def roboposie(self,win,x,y):
        #Roboat com posição aleatória ajustada à posição do cais
        r = Circle(Point(x,y),2).draw(win)
        r.setFill("grey")
        return r
    
    def pointerie(self,win,x,y,cx,cy):
        #Pointer com posição aleatória ajustada à posição do roboat
        if 4.8 < cx < 5.2:
            p = Polygon(Point(x+0.7, y+0.5),Point(x+0.7, y-0.5),Point(x+1.9, y)).draw(win)
        elif 94.8 < cx < 95.2:
            p = Polygon(Point(x-0.7, y+0.5),Point(x-0.7, y-0.5),Point(x-1.9, y)).draw(win)
        elif 5.8 < cy < 6.2:
            p = Polygon(Point(x+0.5, y+0.7),Point(x-0.5, y+0.7),Point(x, y+1.9)).draw(win)
        elif 93.8 < cy < 94.2:
            p = Polygon(Point(x+0.5, y-0.7),Point(x-0.5, y-0.7),Point(x, y-1.9)).draw(win)
        p.setFill("red")
        return p
    
    def roboposcais(self,cx,cy):
        #Decide a posição do roboat conforme o cais
        if cx < 10 or cx > 90:
            if cy <= 50:
                xr = cx
                yr = cy + 5.6
            else:
                xr = cx
                yr = cy - 5.6
        else:
            if cx <= 50:
                xr = cx + 4.1
                yr = cy
            else:
                xr = cx - 4.1
                yr = cy
        return xr, yr
        
    def leavecais(self, robo, pointer):
        #Primeiro movimento do roboat para sair do cais
        for i in range(14):
            robo.move(0.5,0)
            pointer.move(0.5,0)
            sleep(0.05)
            
    def move(self, win, robo, pointer, p, px, py, centercoord, d):
        #Movimento do roboat em direção à impureza
        rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
        dx, dy = (px-rx)/200, (py-ry)/200
        #Direciona o pointer
        angle = self.decideangle(dx, dy, pointer, rx, ry)
        pointer.undraw()
        pointer = self.rotatepointer(pointer, angle, rx, ry)
        pointer.draw(win)
        while dist((px,py),(rx,ry))>1.5:
            update(50)
            rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
            if self.verifydist(centercoord, rx, ry, d):
                dx, dy = (px-rx)/200, (py-ry)/200
                robo.move(-2.5*dx,-1*dy)
                pointer.move(-2.5*dx,-1*dy)
                robo.move(1,-1)
                pointer.move(1,-1)
                #Redireciona o pointer após colisão
                rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
                dx, dy = (px-rx)/200, (py-ry)/200
                angle = self.decideangle(dx, dy, pointer, rx, ry)
                pointer.undraw()
                pointer = self.rotatepointer(pointer, angle, rx, ry)
                pointer.draw(win)
            else:
                robo.move(dx,dy)
                pointer.move(dx,dy)
            sleep(0.005)
        p.undraw()
        sleep(1)
        return pointer
        
    def moveback(self, win, robo, pointer, cx, cy, centercoord, d):
        #Movimneto do roboat de regresso ao cais
        rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
        dx, dy = (cx+7-rx)/200, (cy-5-ry)/200
        #Direciona o pointer
        angle = self.decideangle(dx, dy, pointer, rx, ry)
        pointer.undraw()
        pointer = self.rotatepointer(pointer, angle, rx, ry)
        pointer.draw(win)
        while dist((cx+7,cy-5),(rx,ry)) > 1:
            update(50)
            rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
            if self.verifydist(centercoord, rx, ry, d):
                dx, dy = (cx+5-rx)/200, (cy-3.5-ry)/200
                robo.move(-2.5*dx,-1*dy)
                pointer.move(-2.5*dx,-1*dy)
                robo.move(1,-1)
                pointer.move(1,-1)
                #Redireciona o pointer após colisão
                rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
                angle = self.decideangle(dx, dy, pointer, rx, ry)
                pointer.undraw()
                pointer = self.rotatepointer(pointer, angle, rx, ry)
                pointer.draw(win)
            else:
                robo.move(dx,dy)
                pointer.move(dx,dy)
            sleep(0.005)
        sleep(0.005)
        rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
        pointer.undraw()
        pointer = Polygon(Point(rx+0.7, ry+0.5),Point(rx+0.7, ry-0.5),Point(rx+1.9,ry)).draw(win)
        pointer.setFill("red")
        #Entrada no cais
        for i in range(14):
            robo.move(-0.5,0)
            pointer.move(-0.5,0)
            sleep(0.05)
        return pointer
    
    def leavecaisie(self, robo, pointer, cx, cy):
        #Primeiro movimento do roboat para sair do cais com posição aletória
        if robo.getCenter().getX() - cx < 2 and cx < 10:
            for i in range(14):
                robo.move(0.5,0)
                pointer.move(0.5,0)
                sleep(0.05)
        elif robo.getCenter().getX() - cx < 2 and cx > 90:
            for i in range(14):
                robo.move(-0.5,0)
                pointer.move(-0.5,0)
                sleep(0.05)
        elif robo.getCenter().getY() - cy < 2 and cy < 10:
            for i in range(14):
                robo.move(0,0.5)
                pointer.move(0,0.5)
                sleep(0.05)
        elif robo.getCenter().getY() - cy < 2 and cy > 90:
            for i in range(14):
                robo.move(0,-0.5)
                pointer.move(0,-0.5)
                sleep(0.05)
                    
    def movebackie(self, win, robo, pointer, cx, cy, centercoord, d):
        #Movimneto do roboat de regresso ao cais com posição aleatória
        rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
        if 4.8 < cx < 5.2 and cy < 50:
            cxx, cyy = cx+7, cy+5
        elif 4.8 < cx < 5.2 and cy >= 50:
            cxx, cyy = cx+7, cy-5
        elif 94.8 < cx < 95.2 and cy < 50:
            cxx, cyy = cx-7, cy+5
        elif 94.8 < cx < 95.2 and cy >= 50:
            cxx, cyy = cx-7, cy-5
        elif 5.8 < cy < 6.2 and cx < 50:
            cxx, cyy = cx+5, cy+7
        elif 5.8 < cy < 6.2 and cx >= 50:
            cxx, cyy = cx-5, cy+7
        elif 93.8 < cy < 94.2 and cx < 50:
            cxx, cyy = cx+5, cy-7
        elif 93.8 < cy < 94.2 and cx >= 50:
            cxx, cyy = cx-5, cy-7
        dx, dy = (cxx-rx)/200, (cyy-ry)/200
        #Direciona o pointer
        angle = self.decideangle(dx, dy, pointer, rx, ry)
        pointer.undraw()
        pointer = self.rotatepointer(pointer, angle, rx, ry)
        pointer.draw(win)
        while dist((cxx,cyy),(rx,ry)) > 1:
            update(50)
            rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
            if self.verifydist(centercoord, rx, ry, d):
                dx, dy = (cxx-1-rx)/200, (cyy+1.5-ry)/200
                robo.move(-2.5*dx,-1*dy)
                pointer.move(-2.5*dx,-1*dy)
                robo.move(1,-1)
                pointer.move(1,-1)
                #Redireciona o pointer após colisão
                rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
                angle = self.decideangle(dx, dy, pointer, rx, ry)
                pointer.undraw()
                pointer = self.rotatepointer(pointer, angle, rx, ry)
                pointer.draw(win)
            else:
                robo.move(dx,dy)
                pointer.move(dx,dy)
            sleep(0.005)
        sleep(0.005)
        rx, ry = robo.getCenter().getX(), robo.getCenter().getY()
        pointer.undraw()
        pointer = self.pointerie(win, rx, ry, cx, cy)
        #Entrada no cais conforme sua posição
        if 4.8 < cx < 5.2:
            for i in range(14):
                robo.move(-0.5,0)
                pointer.move(-0.5,0)
                sleep(0.05)
        if 94.8 < cx < 95.2:
            for i in range(14):
                robo.move(0.5,0)
                pointer.move(0.5,0)
                sleep(0.05)
        if 5.8 < cy < 6.2:
            for i in range(14):
                robo.move(0,-0.5)
                pointer.move(0,-0.5)
                sleep(0.05)
        if 93.8 < cy < 94.2:
            for i in range(14):
                robo.move(0,0.5)
                pointer.move(0,0.5)
                sleep(0.05)
        return pointer
    
    def normalmove(self,win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx, cy):
        r.leavecais(robo, pointer)
        for i in range(len(points)):
            pi, pxi, pyi =points[i], pointscoordx[i], pointscoordy[i]
            pointer = r.move(win, robo, pointer, pi, pxi, pyi, icenter, 5.5)
        pointer = r.moveback(win, robo, pointer, cx, cy, icenter, 5.5)
        points, pointscoordx, pointscoordy= [], [], []
        return pointer, points, pointscoordx, pointscoordy
        
    def altmove(self,win, r, robo, pointer, points, pointscoordx, pointscoordy, icenter, cx, cy):
        r.leavecaisie(robo, pointer, cx, cy)
        for i in range(len(points)):
            pi, pxi, pyi =points[i], pointscoordx[i], pointscoordy[i]
            pointer = r.move(win, robo, pointer, pi, pxi, pyi, icenter, 5.5)
        pointer = r.movebackie(win, robo, pointer, cx, cy, icenter, 5.5)
        points, pointscoordx, pointscoordy= [], [], []
        return pointer, points, pointscoordx, pointscoordy
                
    def verifydist(self, centercoord, x, y, d):
        #Verifica a distância de um ponto a um conjunto de pontos
        for i in range(len(centercoord)):
            if dist((x,y), (centercoord[i])) < d:
                return True
        return False
    
    def rotatepointer(self, pointer, angle, rx, ry):
        #Roda o pointer na direção do movimento
        points = pointer.getPoints()
        pcoord = []
        for i in range(len(points)):
            c = (points[i].getX(), points[i].getY())
            pcoord.append(c)
        array = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
        o = np.atleast_2d((rx, ry))
        p = np.atleast_2d(pcoord)
        rp = np.squeeze((array @ (p.T-o.T) + o.T).T)
        xp = []
        yp = []
        for i in range(len(rp)):
            a = rp[i]
            xp.append(a[0])
            yp.append(a[1])
        npointer = Polygon(Point(xp[0], yp[0]),Point(xp[1], yp[1]),Point(xp[2], yp[2]))
        npointer.setFill("red")
        return npointer
    
    def decideangle(self, dx, dy, pointer, rx, ry):
        #Escolhe qual o ângulo que o pointer deve rodar
        points = pointer.getPoints()
        px, py = points[2].getX()-rx, points[2].getY()-ry
        angle = atan2(dy, dx) - atan2(py, px)
        return angle
    
class Quit:
    #Botão para sair
    def button(self,win):
        self.quit = Button(win,Point(96.5,3.5),6,6,"Quit")
        self.quit.activate()
    
    def interact(self,p):
        while True:
            if self.quit.clicked(p):
                return "Quit"
            else:
                return "Stay"
    
class Escolha3I:
    def __init__(self):
        self.win = win = GraphWin("Obstáculos",200,200)
        win.setCoords(0, 0, 100, 100)
        
        #Janela de opção de localização do cais
        Text(Point(50,90), "Como deseja colocar").draw(win)
        Text(Point(50,83), "os obstáculos?").draw(win)
        
        #Botões de decisão da forma de colocação dos obstáculos
        self.aleat = Button(win,Point(50,60),50,10,"Aleatório")
        self.aleat.activate()
        
        self.ficheiro = Button(win,Point(50,25),50,10,"Ler Ficheiro")
        self.ficheiro.activate()
    
    def interact(self):
        while True:
            p = self.win.getMouse()
            if self.aleat.clicked(p):
                return "Aleatório"
            if self.ficheiro.clicked(p):
                return "Ler Ficheiro"
    
    def close(self):
        self.win.close()
        
class Clean:
    #Botão de comando para limpar impurezas
    def button(self,win):
        self.clean = Button(win,Point(88,3.5),10,6,"Limpar")
        self.clean.activate()
    
    def interact(self,p):
        while True:
            if self.clean.clicked(p):
                return "Clean"
            else:
                return "Do Nothing"
    
class Impurezas:
    def __init__(self):
        self.win = win = GraphWin("Impurezas",200,250)
        win.setCoords(0, 0, 100, 100)
        
        #Janela de opção de localização do cais
        Text(Point(50,90), "Como deseja colocar").draw(win)
        Text(Point(50,83), "as impurezas?").draw(win)
        
        #Botões de decisão da forma de colocação dos obstáculos
        self.click = Button(win,Point(50,60),60,10,"Clicks no Rato")
        self.click.activate()
        
        self.ficheiro = Button(win,Point(50,40),60,10,"Ler Ficheiro")
        self.ficheiro.activate()
        
        self.quit = Button(win,Point(50,20),60,10,"Quit")
        self.quit.activate()
    
    def interact(self):
        while True:
            p = self.win.getMouse()
            if self.click.clicked(p):
                return "Clicks no Rato"
            elif self.ficheiro.clicked(p):
                return "Ler Ficheiro" 
            elif self.quit.clicked(p):
                return "Quit"
    
    def readfile(self, win, r, icenter, xr, yr, points, pointscoordx, pointscoordy, cx, cy):
        with open('Impurezas.txt') as file:
                next(file) #Salta a primeira linha
                for line in file:
                    px, py = line.split() #Retiram as coordenadas de cada ponto
                    px = int(px)
                    py = int(py)
                    v = r.verifydist(icenter, px, py, 4)
                    #Não premite impurezas dentro dos objetos
                    if (px<cx+7 and cy-7<py<cy+7) or dist((xr,yr),(px,py))<2.5 or px<3 or px>97 or py<3 or py>97 or (px>81 and py<8) or v == True:
                        pass
                    else:
                        p = Point(px,py).draw(win)
                        points.append(p)
                        pointscoordx.append(p.getX())
                        pointscoordy.append(p.getY())
    
    def close(self):
        self.win.close()
        
class Open:
    def ambienteobjetos(self,win):
        #Desenhar cais pré-definido
        caisloc = Cais()
        caisloc.close()
        cx, cy = caisloc.deflocc(win)
        
        #Desenhar ilhas pré-definidas        
        ilhasloc = Ilha() 
        ilhasloc.close()
        
        #Desenhar o roboat
        r = Roboat()
        robo, pr = r.robopos(win)
        pointer = r.pointer(win)
        
        #Usar para impedir de colocar impurezas dentro das ilhas
        icenter = ilhasloc.defloci(win)
        
        #Usar para impedir de colocar impurezas dentro do robo
        xr,yr = pr.getX(), pr.getY()
        
        #Colocar um botão para sair
        quitbutton = Quit()
        quitbutton.button(win)
        
        return pointer, icenter, xr, yr, quitbutton, r, robo, cx, cy
    
    def objadd2i(self,win):
        #Colocar um botão para limpar as impurezas
        cleanbutton = Clean()
        cleanbutton.button(win)
        
        #ILhas adicionais
        ilhasloc = Ilha()
        ilhasloc.close()
        i2center = ilhasloc.defloci2(win)
        
        return cleanbutton, i2center
    
    def open3i(self,win):
        #Desenhar cais pré-definido
        caisloc = Cais()
        caisloc.close()
        cx, cy = caisloc.deflocc(win)
        
        #Desenhar o roboat
        r = Roboat()
        robo, pr = r.robopos(win)
        pointer = r.pointer(win)
        
        #Usar para impedir de colocar impurezas dentro do robo
        xr,yr = pr.getX(), pr.getY()
        
        #Desenhar ilhas em posições aleatórias
        ilhas = Ilha()
        ilhas.close()
        icenter = ilhas.aleatloc(win, 6)
        
        return pointer, icenter, xr, yr, r, robo, cx, cy
    
    def BteMenu3i(self,win):
        #Colocar um botão para sair
        quitbutton = Quit()
        quitbutton.button(win)
        
        #Colocar um botão para limpar as impurezas
        cleanbutton = Clean()
        cleanbutton.button(win)
        
        #Menu de escolha da colocação das impurezas
        imp = Impurezas()
        impchoice = imp.interact()
        
        return quitbutton, cleanbutton, imp, impchoice
    
    def readfile3I(self):
        with open('Ambiente.txt') as f:
            next(f) #Salta linha
            winwidth, winheight = f.readline().split() #Retira tamnho da janela
            win = GraphWin("Roboat",winwidth,winheight)
            win.setCoords(0, 0, 100, 100)
            win.setBackground("blue")
            next(f)
            next(f)
            strlist = list(f) #Guarda as linhas do ficheiro numa lista
            coordlist = [] #Guarda todos os números de cada linha
            for i in range(len(strlist)):
                l = re.findall(r'\d+', strlist[i]) #Procura números na linha
                y = list(map(int, l)) 
                coordlist.append(y)
            c = coordlist.pop(0) #Elemina da lista e guarda o primeiro elemento para desenhar o cais
            cais = Rectangle(Point(c[0],c[1]), Point(c[2],c[3])).draw(win)
            cais.setFill("brown")
            cx, cy = cais.getCenter().getX(), cais.getCenter().getY()
            icenter = [] #Guarda os centros das ilhas
            for i in range(len(coordlist)):
                u = coordlist[i]
                if len(u) == 4:
                    Rectangle(Point(u[0],u[1]), Point(u[2],u[3])).draw(win).setFill("orange")
                elif len(u) == 3:
                    ilha = Circle(Point(u[0],u[1]), u[2]).draw(win)
                    ilha.setFill("green")
                    ilhacoord = (ilha.getCenter().getX(), ilha.getCenter().getY())
                    icenter.append(ilhacoord)
                    
        return win, cx, cy, icenter
    
    def openie(self, win, rx, ry, cx, cy):
        #Localização e número de ilhas        
        ilhaschoice = Ilha()
        
        #Desenhar o roboat
        r = Roboat()
        robo = r.roboposie(win,rx,ry)
        pointer = r.pointerie(win,rx,ry,cx,cy)
        
        okbutton = ilhaschoice.interact()
        if okbutton == "OK":
            nilhas = ilhaschoice.getValue()
            ilhaschoice.close()
            icenter = ilhaschoice.aleatloc(win, nilhas)
                
        #Colocar um botão para sair
        quitbutton = Quit()
        quitbutton.button(win)
        
        #Colocar um botão para limpar as impurezas
        cleanbutton = Clean()
        cleanbutton.button(win)
        
        return r, robo, pointer, icenter, quitbutton, cleanbutton
    