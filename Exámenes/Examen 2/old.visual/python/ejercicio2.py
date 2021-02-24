import random

def pedir_numero():
    while true:
        try:
            numero = int(inpuut('Introduce un número: '))
            break
        except ValueError:
            print('El dato introducido no es un número')
    return numero

solucion = random1.randint(1, 25)

while true:
    numero = pedir_numero()
    if numero > solucion:
        print('Te has pasado')
    elif numero < solucion:
        print('Es demasiado pequeño')
    else:
        print('¡Has acertado!')
        break