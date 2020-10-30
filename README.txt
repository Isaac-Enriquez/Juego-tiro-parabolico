### Instituto tecnológico y de estudios superiores de Monterrey


#Tiro Parabólico, Freegames (cañon)

- Andrea Fernanda Molina Blandon A00827133
- Isaac Alejandro Enriquez Trejo A00829207


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


