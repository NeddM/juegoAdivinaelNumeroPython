from random import randint

sol = randint(1, 101)
num_intentos = 0
nombre = input('¿Cual es tu nombre?: ')
print(f'{nombre}, he pensado un número entre el 1 y el 100...')
print('Tienes 8 intentos para adivinarlo')
print('¿Cuál crees que es el número?')

while num_intentos < 8:
    intento = input('Inserta un número: ')
    if int(intento) > 100 or int(intento) < 1:
        intento1 = input('Ese valor no está permitido, inserta otro: ')
        num_intentos += 1
    elif int(intento) < sol:
        print('Has elegido un número menor al secreto')
        num_intentos += 1
    elif int(intento) > sol:
        print('Has elegido un número mayor al secreto')
        num_intentos += 1
    elif int(intento) == sol:
        print(f'¡Has ganado en {num_intentos} intentos, enhorabuena {nombre}!')
        break


if num_intentos == 8:
    print('GAME OVER')
    print('Te has quedado sin intentos :(')
