import random
from random import randint
from random import choice

# Ejercicio 16
#
# opciones = ["Piedra","Papel","Tijera","Lagarto","Spock"]
#
# jugador = input("Piedra, Papel, Tijera, Lagarto, Spock, 1..., 2... y 3!:  ")
#
# maquina = choice(opciones)
#
# if jugador == "Piedra" or jugador == "Papel" or jugador == "Tijera" or jugador == "Spock" or jugador == "Lagarto":
#     print(f"Tu has elegido {jugador} y yo {maquina}")
#     if(jugador == "Piedra" and (maquina == "Lagarto" or maquina == "Tijera")):
#         if maquina == "Lagarto":
#             print("La Piedra aplasta al lagarto.")
#         else:
#             print("La Piedra rompe la tijera.")
#
#         print("Tu ganas!")
#
#     elif(jugador == "Papel" and (maquina == "Piedra" or maquina == "Spock")):
#         if maquina == "Piedra":
#             print("El Papel envuelve a la piedra.")
#         else:
#             print("El Papel desautoriza a Spock.")
#
#         print("Tu ganas!")
#
#     elif(jugador == "Tijera" and (maquina == "Papel" or maquina == "Lagarto")):
#
#         if maquina == "Papel":
#             print("La Tijera corta el Papel.")
#         else:
#             print("La Tijera decapita al Lagarto.")
#
#         print("Tu ganas!")
#
#     elif(jugador == "Spock" and (maquina == "Piedra" or maquina == "Tijera")):
#         if maquina =="Piedra":
#             print("Spock pulveriza la Piedra.")
#         else:
#             print("Spock rompe la Tijera.")
#
#         print("Tu ganas!")
#
#     elif(jugador == "Lagarto" and (maquina == "Papel" or maquina == "Spock")):
#         if maquina == "Papel":
#             print("El Lagarto se come el Papel.")
#         else:
#             print("El Lagato envenena a Spock.")
#
#         print("Tu ganas!")
#
#     else:
#         if (maquina == "Piedra" and (jugador == "Lagarto" or jugador == "Tijera")):
#             if jugador == "Lagarto":
#                 print("La Piedra aplasta al lagarto.")
#             else:
#                 print("La Piedra rompe la tijera.")
#
#         elif (maquina == "Papel" and (jugador == "Piedra" or jugador == "Spock")):
#             if jugador == "Piedra":
#                 print("El Papel envuelve a la piedra.")
#             else:
#                 print("El Papel desautoriza a Spock.")
#
#         elif (maquina == "Tijera" and (jugador == "Papel" or jugador == "Lagarto")):
#
#             if jugador == "Papel":
#                 print("La Tijera corta el Papel.")
#             else:
#                 print("La Tijera decapita al Lagarto.")
#
#
#         elif (maquina == "Spock" and (jugador == "Piedra" or jugador == "Tijera")):
#             if jugador == "Piedra":
#                 print("Spock pulveriza la Piedra.")
#             else:
#                 print("Spock rompe la Tijera.")
#
#         elif (maquina == "Lagarto" and (jugador == "Papel" or jugador == "Spock")):
#             if jugador == "Papel":
#                 print("El Lagarto se come el Papel.")
#             else:
#                 print("El Lagato envenena a Spock.")
#
#         print("Tu pierdes!")
# else:
#     print("Tienes que elegir entre Piedra, Papel, Tijera, Lagarto o Spock.")


# Ejercicio 17
#
# texto = input("Dime un texto, incluye mayúsculas, minúsculas y espacios y te diré si es o no un palíndromo:  ")
#
# palindromo = True
#
# print(texto)
# print(texto[::-1])
#
# if texto != texto[::-1]:
#     palindromo = False
#     print("No es un palindromo")
# else:
#     print("Es un palindromo")

# Ejercicio 18
#
# num1 = int(input("Dame un entero y le daré la vuelta: "))
# texto = num1.__str__();
#
# print(str(texto[::-1]))

# Ejercicio 19

num2 = int(input("Dame un entero y te lo ordenaré de menor a mayor: "))
# txt = str(num2)
# print(txt)
# array = list(txt)
# print(array)
# array.sort()
# print(array)
# ordenado = "".join(array)
# print(ordenado)
# numero_ordenado = int(ordenado)
# print(numero_ordenado)

# numero_ordenado = "".join(list(str(num2)).sort())

print(numero_ordenado)