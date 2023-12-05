#prueba2
import turtle
import random
import tkinter as tk
# Crear ventana
ventana = turtle.Screen()
ventana.title("Juego de la Tortuga")
ventana.bgcolor("white")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Crear tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()
tortuga.speed(0)
tortuga.shapesize()
# Crear manzana
manzana = turtle.Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.speed(0)
manzana.goto(random.randint(-390, 390), random.randint(-290, 290))

# Crear obstáculos
obstaculos = []
for _ in range(9):
    obstaculo = turtle.Turtle()
    obstaculo.shape("square")
    obstaculo.color("black")
    obstaculo.penup()
    obstaculo.speed(0)
    obstaculo.goto(random.randint(-390, 390), random.randint(-290, 290))
    obstaculos.append(obstaculo)

# Crear mensaje de 
mensaje_perdida = tk.Tk()
mensaje_perdida.title("HAS PERDIDO")
mensaje_perdida.geometry("300x100")
mensaje_perdida.withdraw()  # Ocultar la ventana <de mensaje al inicio

# Funciones para mover la tortuga
def mover_arriba():
    tortuga.setheading(90)
    y = tortuga.ycor()
    tortuga.sety(y + 20)

def mover_abajo():
    tortuga.setheading(270)
    y = tortuga.ycor()
    tortuga.sety(y - 20)

def mover_izquierda():
    tortuga.setheading(180)
    x = tortuga.xcor()
    tortuga.setx(x - 20)

def mover_derecha():
    tortuga.setheading(0)
    x = tortuga.xcor()
    tortuga.setx(x + 20)

# Asignar las teclas
ventana.listen()
ventana.onkeypress(mover_arriba, "w")
ventana.onkeypress(mover_abajo, "s")
ventana.onkeypress(mover_izquierda, "a")
ventana.onkeypress(mover_derecha, "d")

# Bucle 
while True:
    turtle.update()

    # Verificar alcanzado la manzana
    if tortuga.distance(manzana) < 20:
        manzana.goto(random.randint(-390, 390), random.randint(-290, 290))
        tortuga.shapesize(stretch_wid=tortuga.shapesize()[0] + 0.1)

    # Verificar si la tortuga ha chocado
    for obstaculo in obstaculos:
        if tortuga.distance(obstaculo) < 20:
            mensaje_perdida.deiconify()
            break

    # Verificar 
    if tortuga.xcor() > 390 or tortuga.xcor() < -390 or tortuga.ycor() > 290 or tortuga.ycor() < -290:
        mensaje_perdida.deiconify() 
        break
# Salir del juego
turtle.done()
