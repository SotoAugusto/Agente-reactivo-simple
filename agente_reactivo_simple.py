# command to install turtle using deprecated version
# pip install turtle --use-deprecated=backtrack-on-build-failures
from turtle import *
import tkinter
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
# pencolor("black")
# turtle.pencolor("black")
shape("circle")

window.setup(width=900, height=700, startx=None, starty=None)



# «fastest»: 0
# «fast»: 10
# «normal»: 6
# «slow»: 3
# «slowest»: 1
# ! agente
speed(0)



size_square = 30
# Tamaño de la cuadrícula (nxn)
size_of_grid = 19

number_of_obstacles = 5

agent_initial_position_X = -400 
agent_initial_position_Y = -270 

pencil_position_X = agent_initial_position_X 
pencil_position_Y = agent_initial_position_Y 



column = 1 
co = 0 #VARIABLE AUXILIAR PARA ESQUIVAR


list_obstacles = [] 
posix = list() #VARIABLE QUE GUARDA LAS COORDENADAS (px, p = 0)

        
def create_obstacles():
    global list_obstacles
    global number_of_obstacles
    
    # * obstacle
    color("red") 
    
    random_num_obstacle_position = 0       #AUXILIAR EN LA ELECCIÓN DE LOS OBSTACULOS ALEATORIOS
    obstacle_position_X = agent_initial_position_X     #AUXILIAR PARA GUARDAR COORDENADAS EN X
    obstacle_position_Y = agent_initial_position_Y     #GUARDA TODAS LAS COORDENADAS POSIBLES EN Y
    
    lx = list()  #GUARDA TODAS LAS COORDENADAS EN X
    ly = list()  #GUARDA TODAS LAS COORDENADAS EN Y
    list_coordinates = list() 
    list_obstacles = []      
    

    for i in range(size_of_grid-2):
        obstacle_position_X += size_square
        obstacle_position_Y += size_square
        lx.append(obstacle_position_X)
        ly.append(obstacle_position_Y)
    
    for x in lx:
        for y in ly: #CICLO PARA EVITAR QUE SE GENEREN OBSTACULOS EN LA PRIMERA Y ULTIMA FILA
            list_coordinates.append((x,y)) 
    # print("LOS ARREGLOS LX Y LY SON: \nLX: ", lx,"\nLY: ", ly,"\nL: ",list_coordinates)


    for i in range (number_of_obstacles):
        
        # * obstacle
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
        forward(size_square)
        left(90)
        forward(size_square)
        left(90)
        forward(size_square)
        left(90)
        forward(size_square)
        end_fill()
        penup()

    setposition(agent_initial_position_X,agent_initial_position_Y)

def agent():
    turtle.forward(size_square)
    
    global column
    global pencil_position_X
    global pencil_position_Y
    global posix
    co = 0 #POSICIONES QUE BAJA AL ESQUIVAR
    color("black", "lime") #COLOR RELLENO Y CONTORNO RESPECTIVAMENTE
    
    for i in range(size_of_grid):
        
        if column == False:
            column = 1
            

            for i in range(size_of_grid):
                if column == (size_of_grid+1):                    
                    break
                posix = ((round(pos()[0]-size_square)),(round(pos()[1])))
                
                # print ("POSIX ACAAAAA", posix)
                
                # print("HACIA OESTE: ", column, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1]))
                pendown()
                begin_fill()
                draw_square()
                end_fill()
                pencil_position_X -= size_square    
                
                if posix in list_obstacles:
                    pencil_position_X += size_square
                    pencil_position_Y -= size_square
                    penup()
                    setposition(pencil_position_X, pencil_position_Y)
                    pendown()
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_X -= size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_X -= size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_Y += size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    co += 1
                    column += 1
                
                setposition(pencil_position_X,pencil_position_Y)
                column+=1
            pencil_position_X += size_square
            pencil_position_Y += size_square
            penup()
            setposition(pencil_position_X, pencil_position_Y)
            #print("POSCIÓN FINAL FUERA DEL CICLO: ", c, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1])) #POSCIÓN FINAL FUERA DEL CICLO
            column = True  
                
            
        else:
            
            column = 1
            for i in range(size_of_grid):

                if column == (size_of_grid+1):
                    
                    break
                
                #print("C: ", c)
                penup()
                setposition(pencil_position_X,pencil_position_Y)
                pendown()
                begin_fill()
                setheading(90)
                draw_square()
                end_fill()
                posix = ((round(pos()[0]+size_square)),(round(pos()[1])))
                pencil_position_X += size_square
                # print("HACIA ESTE: ", column," POSICIÓN EN X, Y: ", round(pos()[0])," ",round(pos()[1]))
                column+=1
                
                
                if posix in list_obstacles:
                    pencil_position_X -= size_square
                    pencil_position_Y -= size_square
                    penup()
                    setposition(pencil_position_X,pencil_position_Y)
                    pendown()
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_X += size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_X += size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    begin_fill()
                    draw_square()
                    end_fill()
                    pencil_position_Y += size_square
                    setposition(pencil_position_X, pencil_position_Y)
                    co += 1
                    column += 1
                    
                    
                    
                    
            # print("FINAL DE LA FILA: ", column, " POSICIÓN EN X, Y: ", round(pos()[0])," ", round(pos()[1])) #POSCIÓN FINAL FUERA DEL CICLO
            pencil_position_X -= size_square
            pencil_position_Y += size_square
            penup()
            setposition(pencil_position_X,pencil_position_Y)
            column = False
            
            

def draw_square():
    turtle.forward(size_square)
    turtle.left(90)
    turtle.forward(size_square)
    turtle.left(90)
    turtle.forward(size_square)
    turtle.left(90)
    turtle.forward(size_square)
    turtle.left(90)
    
# def meta():
#     color("purple", "purple")
#     penup()
#     setheading(90)
#     setposition(170, 300)
#     begin_fill()
#     pintar()
#     end_fill()
    
    
        
def meta():
    color("purple", "purple")
    penup()
    setheading(90)
    setposition(140, 270)
    # setposition(170, 300) #for grid 20
    begin_fill()
    draw_square()
    end_fill()
    
    
meta()
create_obstacles()
agent()
tkinter.messagebox.showinfo(title="Agente reactivo simple", message="FINIIIIIIIIIIIIIIIIIISH")
exit()
# window.mainloop()