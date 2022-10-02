# import os.path
# import random
# import datetime
#
# print(os.getcwd())
# print(os.path.exists("C:/Python27"))

# print(random.random())
# print(random.randint(3, 7))
#
# print(datetime.datetime.now().date())

# Si importamos así, especificamente, podemos usar directamente los métodos sin referenciar al import general

from random import random, randint
from datetime import datetime, date

# print(random())
# print(randint(3, 7))
#
# print(datetime.now().date())

# Ejercicio 9

# numero = input("Dime un float y te diré la potencia del exponente que me digas: ")
#
# if numero.count(".") == 1:
#     potencia = input("Dime ahora la potencia: ")
#
#     if potencia.isdigit():
#         print(f"El numero {numero} elevado a {potencia} es {float(numero).__pow__(int(potencia))}")
#     else:
#         print("La potencia debe ser un numero entero.")
# else:
#     print("El numero float introducido no es correcto.")

# Ejercicio 10
# 1 -> Piedra
# 2 -> Papel
# 3 -> Tijera

# ana = randint(1, 3)
# juan = randint(1, 3)
#
# if ana == juan:
#     if ana == 1:
#         print("Ana sacó piedra y Juan tambien, ¡Empate!")
#     elif ana == 2:
#         print("Ana sacó papel y Juan también, ¡Empate!")
#     elif ana == 3:
#         print("Ana sacó tijera y Juan también, ¡Empate!")
# elif ana == 1:
#     if juan == 2:
#         print("Ana sacó piedra y Juan papel, ¡Juan gana!")
#     else:
#         print("Ana sacó piedra y Juan tijera, ¡Ana gana!")
# elif ana == 2:
#     if juan == 1:
#         print("Ana sacó papel y Juan piedra, ¡Ana gana!")
#     else:
#         print("Ana sacó papel y juan tijera, ¡Juan gana!")
# else:
#     if juan == 1:
#         print("Ana sacó tijera y Juan piedra, ¡Juan gana!")
#     else:
#         print("Ana sacó tijera y juan papel, ¡Ana gana!")

# Ejercicio 11
#
# golpes = int(input("Dime el numero de golpes que dio el jugador: "))
#
#
# if golpes == 1:
#     print("Hole-In-One!")
# else:
#     ideal = int(input("Ahora dime el par del hoyo: "))
#     if golpes <= ideal-2:
#         print("Eagle")
#     elif golpes == ideal -1:
#         print("Birdie")
#     elif golpes == ideal:
#         print("Par")
#     elif golpes == ideal+1:
#         print("Bogey")
#     elif golpes == ideal+2:
#         print("Double Bogey")
#     elif golpes >= ideal+3:
#         print("Go Home!")

# Ejercicio 12
# correcto = False
#
# while correcto == False:
#     alnum = input("Dime una cadena alfanumérica: ")
#     if alnum.isalnum():
#         correcto = True
#         print("Correcto")
#     else:
#         print("Incorrecto")

# Ejercicio 13

# num = int(input("Dime un numero: "))

# contador = 1

# while contador <= num:
#     print("*" * num)
#     contador +=  1
#
# contador = 1
#
# while contador <= num:
#     print("*" * contador)
#     contador += 1

# Ejercicio 14

# aleatorio = randint(0,50)
#
# print(aleatorio)
#
# intento = int(input("Intenta adivinar un número entre el 0 y el 50 en el menor numero de intentos: "))
#
# contador = 1
#
# while intento != aleatorio:
#     contador += 1
#     if intento > aleatorio:
#         print(f"El numero es mas pequeño que {intento}")
#         intento = int(input("Sigue intentandolo: "))
#     elif intento < aleatorio:
#         print(f"El numero es mas grande que {intento}")
#         intento = int(input("Sigue intentandolo: "))
#
# print(f"Correcto!, lo adivinaste en {contador} intentos.")

# Ejercicio 15

print("Piensa un numero entre el 1 y el 50, voy a adivinarlo en el menor numero de intentos posible.")

generado = randint(0,50)

print(f"¿Es tu numero el {generado}?  ")
adivinado = input("")
contador = 0

while adivinado != "s":
        contador += 1
        print(f"Dejame intentarlo otra vez, pero antes, es tu numero mayor o menor que {generado}?  ")
        distancia = input("")

        if distancia == "mayor":
                generado = randint(generado,50)
                adivinado = input(f"En ese caso, es tu numero el {generado}?  ")
        elif distancia == "menor":
                generado = randint(0,generado)
                adivinado = input(f"En ese caso, es tu numero el {generado}?  ")

print(f"Adivinado, he tardado {contador} intentos :P")