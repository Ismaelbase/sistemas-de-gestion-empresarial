import random

# Ejercicio 2
# A
# import random
#
# cantidad_dados = int(input("Dime la cantidad de dados que deseas tirar."))
# print(cantidad_dados)
# numero_indicado = int(input("Dime el numero por el que quieres apostar."))
#
# for i in range(cantidad_dados):
#     tirada = random.randint(1,6)
#     print(i)
#     print(f"Tirada numero {i+1} -> {tirada}")
#     if tirada == numero_indicado:
#         print(f"Salio el {numero_indicado} ¡Tu ganas!")
#         break
#     if(i == cantidad_dados-1):
#         print("No ha salido, perdiste.")


# B
#
# cantidad_dados = int(input("Dime la cantidad de dados que deseas tirar: "))
#
# mayor_tirada = random.randint(1,6)
# cantidad_dados = cantidad_dados -1
# print(f"Tirada 1 -> {mayor_tirada}")
#
# for i in range(cantidad_dados):
#     tirada = random.randint(1,6)
#     print(f"Tirada {i+2}-> {tirada}")
#
#     if(mayor_tirada<tirada):
#         mayor_tirada = tirada
#
# print(f"El valor mas alto obtenido es -> {mayor_tirada}")


# C
#
# cantidad_dados = int(input("Dime la cantidad de dados a tirar: "))
#
# jugador1 = list()
# jugador2 = list()
#
# for i in range(cantidad_dados):
#     jugador1.append(random.randint(1,6))
#     print(f"Tirada jugador 1 -> {jugador1[i]}")
#     jugador2.append(random.randint(1,6))
#     print(f"Tirada jugador 2 -> {jugador2[i]}")
#     print("============================")
#
# j1_mayor = max(jugador1)
# j2_mayor = max(jugador2)
#
# if(j1_mayor>j2_mayor):
#     print(f"La tirada mas alta del jugador 1 fue [{j1_mayor}] y la del Jugador 2 [{j2_mayor}] -> Jugador 1 Gana.")
# elif(j2_mayor>j1_mayor):
#     print(f"La tirada mas alta del jugador 1 fue [{j1_mayor}] y la del Jugador 2 [{j2_mayor}] -> Jugador 2 Gana.")
# else:
#     print(f"La tirada mas alta del jugador 1 fue [{j1_mayor}] y la del Jugador 2 [{j2_mayor}]  -> Empate. ")


# D
#
# cantidad_dados = int(input("Dime la cantidad de dados que quieres tirar: "))
#
# puntos_j1 = 0
# puntos_j2 = 0
#
# for i in range(cantidad_dados):
#     tirada = random.randint(1,6)
#     print(f"Tirada {i} -> {tirada}")
#     if(tirada % 2 == 0):
#         puntos_j1 += 1
#     else:
#         puntos_j2 += 1
#
# if(puntos_j1 > puntos_j2):
#     print(f"El jugador 1 tiene {puntos_j1}  y el Jugador 2 {puntos_j2} -> Jugador 1 gana.")
# elif(puntos_j2 > puntos_j1):
#     print(f"El jugador 1 tiene {puntos_j1}  y el Jugador 2 {puntos_j2} -> Jugador 2 gana.")
# else:
#     print(f"El jugador 1 tiene {puntos_j1}  y el Jugador 2 {puntos_j2} -> Empate.")

# E
# import random
#
# numero_jugadores = int(input("Dime cuantos jugadores van a jugar: "))
#
# tiradas = list()
#
# for i in range(numero_jugadores):
#
#     tirada = random.randint(1,6)
#     tiradas.append(tirada)
#     print(f"Jugador {i} -> {tirada}")
#
# menor_tirada = tiradas.index(min(tiradas))
#
# print(f"Gana el jugador {menor_tirada}.")

# F

#
# cantidad_dados = int(input("Dime una cantidad de dados a tirar: "))
#
# tiradas_j1 = list()
# tiradas_j2 = list()
#
# for i in range(cantidad_dados):
#
#     tirada_j1 = random.randint(1, 6)
#     print(f"Jugador 1 tirada {i} -> {tirada_j1}")
#
#     tirada_j2 = random.randint(1, 6)
#     print(f"Jugador 2 tirada {i} -> {tirada_j2}")
#
#     tiradas_j1.append(tirada_j1)
#     tiradas_j2.append(tirada_j2)
#
# suma_j1 = (min(tiradas_j1)+max(tiradas_j1))
# suma_j2 = (min(tiradas_j2)+max(tiradas_j2))
#
# if(suma_j1>suma_j2):
#     print(f"La suma del mayor y menor dado del jugador 1 es {suma_j1} y la del jugador 2 {suma_j2} el jugador 1 gana")
# elif(suma_j2>suma_j1):
#     print(f"La suma del mayor y menor dado del jugador 1 es {suma_j1} y la del jugador 2 {suma_j2} el jugador 2 gana")
# else:
#     print(f"La suma del mayor y menor dado del jugador 1 es {suma_j1} y la del jugador 2 {suma_j2} empate.")

# G
tirada_actual = 0
tirada_antiga = 0
cantidad_dados = int(input("Dime una cantidad de dados: "))

tirada_antigua = random.randint(1, 100)
print(f"Tirada 1 -> {tirada_antigua}")
for i in range(cantidad_dados - 1):

    tirada_actual = random.randint(1, 100)
    print(f"Tirada {i + 2} -> {tirada_actual}")

    if (tirada_actual == tirada_antigua):
        print("¡Dos tiradas seguidas, tu ganas!")
        break
    else:
        tirada_antigua = tirada_actual

