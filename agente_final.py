from turtle import *
# from tkinter import *
from random import randrange
import random
import turtle


# ? number_of_obstacles = int(input('Introduzca el número de obstaculos deseados:\n'))


# create a new drawing board(window) and a turtle. 
# Let’s create window and the turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Agente reactivo simple")
# agent = turtle.Turtle()
# agent = Turtle()

window.setup(width=900, height=700, startx=None, starty=None)

# «fastest»: 0
# «fast»: 10
# «normal»: 6
# «slow»: 3
# «slowest»: 1
# ! agente
speed(0)


number_of_obstacles = 1
cm = 30 #MEDIDA DE LOS CUADROS
sx = -400 #SETUP X (Posición inicial del lapicero en X)
sy = 300 #SETUP Y (Posición inicial del lapicero en Y)
cx = sx #COORDENADAS DEL LAPIZ EN X
cy = sy #COORDENADAS DEL LÁPIZ EN Y


# Tamaño de la cuadrícula (20x20)
size_of_grid = 20 

c = 1 #AUXILIAR QUE INDICA SI EL AGENTE SE MUEVE A LA DERECHA O IZQUIERDA
co = 0 #VARIABLE AUXILIAR PARA ESQUIVAR


list_obstacles = [] 
posix = list() #VARIABLE QUE GUARDA LAS COORDENADAS (px, py)
nx = 0 #VARIABLE AUXILIAR PARA IMPRIMIR
ny = 1 #VARIABLE AUXILIAR PARA IMPRIMIR
        
def create_obstacles():
    global list_obstacles
    global number_of_obstacles
    
    # * obstacle
    color("red") #COLOR DEL LÁPIZ Y RELLENO RESPECTIVAMENTE
    
    aux = sx     #AUXILIAR PARA GUARDAR COORDENADAS EN X
    auy = sy     #GUARDA TODAS LAS COORDENADAS POSIBLES EN Y
    lx = list()  #GUARDA TODAS LAS COORDENADAS EN X
    ly = list()  #GUARDA TODAS LAS COORDENADAS EN Y
    list_coordinates = list()   #GUARDA TODAS LAS COORDENADAS POSIBLES
    random_num_obstacle_position = 0       #AUXILIAR EN LA ELECCIÓN DE LOS OBSTACULOS ALEATORIOS
    list_obstacles = []      #GUARDA LAS COORDENADAS DE LOS OBSTACULOS GENERADOS
    
    for i in range(18):
        aux += cm
        auy -= cm
        lx.append(aux)
        ly.append(auy)
    
    for x in lx:
        for y in ly:                #CICLO PARA EVITAR QUE SE GENEREN OBSTACULOS EN LA PRIMERA Y ULTIMA FILA
            list_coordinates.append((x,y)) 
    #print("LOS ARREGLOS LX Y LY SON: \nLX: ", lx,"\nLY: ", ly,"\nL: ",l)


    for i in range (number_of_obstacles):
        
        # * obstacle
        # ! este es un comentario de prueba
        penup()
        
        random_num_obstacle_position = random.choice(list_coordinates)
        while True:
            if random_num_obstacle_position in list_obstacles:
                random_num_obstacle_position = random.choice
            else:
                break
        list_obstacles.append((random_num_obstacle_position))
        # * obstacle
        setposition(random_num_obstacle_position)
        pendown()
        begin_fill()
        setheading(90)
        forward(cm)
        left(90)
        forward(cm)
        left(90)
        forward(cm)
        left(90)
        forward(cm)
        end_fill()
        penup()

    setposition(sx,sy)

def agente():

    global c
    global cx
    global cy
    global nx
    global ny
    global posix
    co = 0 #POSICIONES QUE BAJA AL ESQUIVAR
    color("black", "lime") #COLOR DEL LÁPIZ Y RELLENO RESPECTIVAMENTE
    
    for i in range(size_of_grid):
        if c == False:
            c = 1
            for i in range(size_of_grid):
                if c == 21:
                    break
                posix = ((round(pos()[0]-cm)),(round(pos()[1])))
                print("HACIA ESTE: ", c, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1]))
                pendown()
                begin_fill()
                pintar()
                end_fill()
                cx -= cm    
                
                if posix in list_obstacles:
                    cx += cm
                    cy -= cm
                    penup()
                    setposition(cx,cy)
                    pendown()
                    begin_fill()
                    pintar()
                    end_fill()
                    cx -= cm
                    setposition(cx, cy)
                    begin_fill()
                    pintar()
                    end_fill()
                    cx -= cm
                    setposition(cx, cy)
                    begin_fill()
                    pintar()
                    end_fill()
                    cy += cm
                    setposition(cx, cy)
                    co += 1
                    c += 1
                
                setposition(cx,cy)
                c+=1
            cx += cm
            cy -= cm
            penup()
            setposition(cx, cy)
            #print("POSCIÓN FINAL FUERA DEL CICLO: ", c, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1])) #POSCIÓN FINAL FUERA DEL CICLO
            c = True      
            
        else:
            c = 1
            for i in range(size_of_grid):
                
                if c == 21:
                    break
                
                #print("C: ", c)
                penup()
                setposition(cx,cy)
                pendown()
                begin_fill()
                setheading(90)
                pintar()
                end_fill()
                posix = ((round(pos()[0]+cm)),(round(pos()[1])))
                cx += cm
                print("HACIA OESTE: ", c," POSICIÓN EN X, Y: ", round(pos()[0])," ",round(pos()[1]))
                c+=1
                
                if posix in list_obstacles:
                    cx -= cm
                    cy -= cm
                    penup()
                    setposition(cx,cy)
                    pendown()
                    begin_fill()
                    pintar()
                    end_fill()
                    cx += cm
                    setposition(cx, cy)
                    begin_fill()
                    pintar()
                    end_fill()
                    cx += cm
                    setposition(cx, cy)
                    begin_fill()
                    pintar()
                    end_fill()
                    cy += cm
                    setposition(cx, cy)
                    co += 1
                    c += 1
                    
            print("FINAL DE LA FILA: ", c, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1])) #POSCIÓN FINAL FUERA DEL CICLO
            cx -= cm
            cy -= cm
            penup()
            setposition(cx,cy)
            c = False

def pintar():
    turtle.forward(cm)
    turtle.left(90)
    turtle.forward(cm)
    turtle.left(90)
    turtle.forward(cm)
    turtle.left(90)
    turtle.forward(cm)
    turtle.left(90)
    
def meta():
    color("purple", "purple")
    penup()
    setheading(90)
    setposition(170, 300)
    begin_fill()
    pintar()
    end_fill()
    
meta()
create_obstacles()
agente()
window.mainloop()
