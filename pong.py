import turtle
#Pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Pong Game")
pantalla.setup(600,400)
#Paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.shape("square")
paleta_izq.color("white")
paleta_izq.shapesize(stretch_len=1,stretch_wid=5)
paleta_izq.penup()
paleta_izq.goto(-250,0)

#Paleta derecha
paleta_der = turtle.Turtle()
paleta_der.shape("square")
paleta_der.color("white")
paleta_der.shapesize(stretch_len=1,stretch_wid=5)
paleta_der.penup()
paleta_der.goto(250,0)

pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.dx = 5
pelota.dy = -5

def paleta_izq_up():
    y = paleta_izq.ycor()
    y = y + 20
    paleta_izq.sety(y)

def paleta_izq_dwn():
    y = paleta_izq.ycor()
    y = y - 20
    paleta_izq.sety(y)

def paleta_der_up():
    y = paleta_der.ycor()
    y = y + 20
    paleta_der.sety(y)

def paleta_der_dwn():
    y = paleta_der.ycor()
    y = y - 20
    paleta_der.sety(y)

pantalla.listen()
pantalla.onkeypress(paleta_izq_up,"w")
pantalla.onkeypress(paleta_izq_dwn,"s")
pantalla.onkeypress(paleta_der_up,"Up")
pantalla.onkeypress(paleta_der_dwn,"Down")

puntaje_izq = 0
puntaje_der = 0

tablero = turtle.Turtle()
tablero.color("white")
tablero.goto(0,150)
tablero.write(f"Player1 {puntaje_izq} - Player2 {puntaje_der}",align="center", font=("Verdana",24,"normal"))
while True:
    pantalla.update()

    pelota.sety(pelota.ycor() + pelota.dy)
    pelota.setx(pelota.xcor() + pelota.dx)

    if pelota.ycor() > 140:
        pelota.sety(140)
        pelota.dy = pelota.dy * -1
    
    if pelota.ycor() < -140:
        pelota.sety(-140)
        pelota.dy = pelota.dy * -1

    if pelota.xcor() > 250:
        pelota.goto(0,0)
        pelota.dx = pelota.dx * -1
        puntaje_izq = puntaje_izq + 1
    if pelota.xcor() < -250:
        pelota.goto(0,0)
        pelota.dx = pelota.dx * -1
        puntaje_der = puntaje_der + 1
    if (pelota.xcor() > 230 and pelota.xcor() < 240) and (pelota.ycor() < paleta_der.ycor() + 40 and pelota.ycor() > paleta_der.ycor()- 40):
        pelota.setx(230)
        pelota.dx = pelota.dx * -1

    if (pelota.xcor() < -230 and pelota.xcor() > -240) and (pelota.ycor() < paleta_izq.ycor() + 40 and pelota.ycor() > paleta_izq.ycor()- 40):
        pelota.setx(-230)
        pelota.dx = pelota.dx * -1
    if paleta_izq.ycor() > 145:
        paleta_izq.sety(145)

    if paleta_izq.ycor() < -145:
        paleta_izq.sety(-145)
    
    if paleta_der.ycor() > 145:
        paleta_der.sety(145)

    if paleta_der.ycor() < -145:
        paleta_der.sety(-145)

turtle.done()