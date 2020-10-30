### Instituto tecnológico y de estudios superiores de Monterrey


#Tiro Parabólico, Freegames (cañón)

- Andrea Fernanda Molina Blandon A00827133
- Isaac Alejandro Enriquez Trejo A00829207

# GIT
Sistema de control de versiones, el cual registra los cambios de un codigo 
durante el desarrollo de este. En este caso, se llevo el registro de juego 
"cañón" de Freegames del lenguaje de programación Python. 

### Actividad 4: Tiro parabólico

¿Qué hace el .py?
-----------------
Freegames ofrece un juego de tiro parabólico entre su gigantesca selección,
este programa el objetivo es dispararle a bolas azules por medio de clics
en la pantalla. El disparo hace que salga una bolita roja a una velocidad
que se puede editar facilmente, y además, cuando detecta una colisión con
las bolas azules éstas desaparecen como si se "rompieran".


¿Cómo hacer que el juego se termine si no se dispara a todo?
-------------------------------------------------------------
Dentro de la función move() se encuentra el siguiente bloque de código:

    for target in targets:
        if not inside(target):
            return
			
Esto hace que si una de las bolas azules toquen el borde del juego este
se detenga de inmediato. Nosotros modificamos ese fragmento para que fuera:

    for target in targets:
        if not inside(target):
            target.x = 200
			
De esta forma las bolas azules simplemente reaparecen al lado derecho de la
pantalla y el juego continua de forma indefinida. Se puso que x=200 debido a
que las dimensiones del juego se ubican en un plano cartesiano que va desde
-200 hasta +200 tanto en 'X', así como en 'Y'.


¿Cómo modificar la velocidad del proyectil y de los objetivos?
---------------------------------------------------------------
En el código original de Freegames, dentro de la función tap() se encuentra 
el siguiente bloque de código:

	def tap(x, y):
		"Respond to screen tap."
		if not inside(ball):
			ball.x = -199
			ball.y = -199
			speed.x = (x + 200) / 25
			speed.y = (y + 200) / 25
			
Lo que nos interesa son las lineas que dicen speed.x y speed.y, a las cuales
se les puede aumentar un poco los números para hacer el proyectil más rápido:

	def tap(x, y):
		"Respond to screen tap."
		if not inside(ball):
			ball.x = -199
			ball.y = -199
			speed.x = (x + 480) / 25
			speed.y = (y + 480) / 25
			
El otro bloque de código que dicta la velocidad se encuentra en la función move(),
es para la velocidad de las bolas azules y de la 'gravedad' al parecer:

	for target in targets:
		target.x -= 0.5

	if inside(ball):
		speed.y -= 0.35
		ball.move(speed)
		
Debe nortarse que la velocidad de las bolas azules es negativa, debido a que
se mueven de derecha a izquieda, por eso se resta del total. Modificando un
poco los valores es posible hacer que se muevan más rápido las bolas azules
así como el efecto de la 'gravedad' sobre el proyectil:

    for target in targets:
        target.x -= 3

    if inside(ball):
        speed.y -= 1.00
        ball.move(speed)
