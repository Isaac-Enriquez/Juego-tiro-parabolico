#A00827133 Andrea Fernanda Molina Blandon
#A00829207 Isaac Alejandro Enriquez Trejo

from random import randrange
from turtle import *
from freegames import vector


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Se define una funcion que detalla las caracteristicas
#del proyectil rojo, la velocidad y posicion de esta
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 480) / 25
        speed.y = (y + 480) / 25

#Esta función detecta si algo está dentro de la pantalla.
#Retorna True si está dentro de los bordes.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Esta función dibuja el proyectil y sus objetivos.
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()
    
#se determinan los puntos objetivos por el proyectil
#en la funcion se definen posiciones aleatorias
#y la velocidad de este
def move():
    "Move ball and targets."
    #Este bloque genera de forma aleatoria nuevos objetivos.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3 #Esta linea modifica la velocidad de los objetivos

    if inside(ball):
        speed.y -= 1.00 #Esta linea controla la gravedad
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    #Este bloque de código hace que el juego no acabe
    #cuando se sale de los límites una bolita y en cambio
    #lo pone en el inicio de nuevo a la misma altura.
    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()