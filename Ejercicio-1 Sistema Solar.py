# Sistema Solar
app.fondo = 'negro'

Sol = Star(200, 200, 20, 50, relleno=gradiente('naranjaOscuro', 'rojoNaranja', 'rojo'))

# Planetas
Mercurio = Group(
    Circle (200, 200, 40, relleno= None, borde= 'plateado'),
    Circle (200, 160, 10, relleno=gradiente('gris', 'grisOscuro', inicio='derecha'), borde='grisPizarra'),
    )
    
Venus = Group(
    Circle (200, 200, 70, relleno= None, borde= 'plateado'),
    Circle (200, 130, 10, relleno=gradiente('naranja','coral', 'rojo', 'carmesi', inicio='izquierda-superior')),
    )
    
Tierra = Group(
    Circle (200, 200, 100, relleno= None, borde= 'plateado'),
    Circle (200, 100, 10, relleno=gradiente('verdeAmarillento', 'azul', inicio='izquierda-inferior')),
    Circle (185, 90, 5, relleno= 'gris'),
    )
Tierra.dirección = 'sentido-horario'

Marte = Group(
    Circle (200, 200, 130, relleno= None, borde= 'plateado'),
    Circle (200, 70, 10, relleno=gradiente('carmesi', 'ladrillo', inicio='izquierda')),
    )
    
Jupiter = Group(
    Circle (200, 200, 160, relleno= None, borde= 'plateado'),
    Circle (200, 40, 12, relleno=gradiente('marronArenoso','naranjaMarron', 'chocolate', inicio='derecha-superior')),
    )
    
Saturno = Group (
    Circle (200, 200, 190, relleno= None, borde= 'plateado'),
    Circle (200, 10, 12, relleno=gradiente('trigo', 'bisque', inicio='izquierda-superior')),
    Oval (200, 10, 40, 8, relleno= None, borde='madera'),
    )
    
Estrella = Group(
    Line(45, 42, 0, 0, relleno=gradiente('negro', 'blanco', inicio='izquierda'), anchuraDeLinea=3, opacidad=70),
    Star (45, 42, 6, 8, relleno='blanco', opacidad=80)
    )
Estrella.dx = 10
Estrella.dy = 10

estrella = Group(
    Line(50, 350, 0, 400, relleno=gradiente('negro', 'blanco', inicio='izquierda'), anchuraDeLinea=3, opacidad=70),
    Star (50, 350, 6, 8, relleno='blanco', opacidad=80)
    )
Estrella.dx = 10
Estrella.dy = 10
estrella.dx = 10
estrella.dy = -10

def enPaso():
    Mercurio.rotarÁngulo += 4.5
    Venus.rotarÁngulo += 4
    Tierra.rotarÁngulo += 3.5
    Marte.rotarÁngulo += 3
    Jupiter.rotarÁngulo += 2.5
    Saturno.rotarÁngulo += 2
    Sol.puntos += 1
    Estrella.centroX += Estrella.dx
    Estrella.centroY += Estrella.dy
    estrella.centroX += estrella.dx
    estrella.centroY += estrella.dy
    
    
    