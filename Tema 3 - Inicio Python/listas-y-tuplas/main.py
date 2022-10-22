from random import randint
from random import choice

#
# numeros = [1,2,3,4,90]
# print(numeros)
# print(numeros[0])
# x = str(numeros[0])+" "+str(numeros[-1])
# print(x)
# print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}")
#
# dias = ["Lunes","Martes","Miercoles","Jueves"]
# print(dias)
# print(dias[3])
#
# dias.append("Viernes")
# print(dias)
#
#
# tabla = [[1,2,3],[9,8,7]]
# print(tabla[1][0])
#
# mezcla = [[5,6,7],"Hola",["cosas","adios"]]
#
# print(mezcla[2])


# nombre = "Daniel"
# apellido1 = "Gutierrez"
# apellido2 = "Ortiz"
#
# nombre_completo = [nombre, apellido1, apellido2]
#
# print(nombre_completo)
#
# # Desestructurar:
#
# [n1, n2, n3] = nombre_completo
#
# print(n1, n2, n3)

# Referencias:

# Esto solo hace que copia sea una referencia a lista
# lista = [1, 3, 5, 7]
# copia = lista
# copia[2] = 999
# print(lista)

# Esto crearia una lista nueva con los mismos valores.
# copia = list(lista)

# lista = [1, 3, 5, 7]
# print(lista)
# # Esto crea una copia del array no una referencia:
# prueba = lista[1:3]
# lista[2] = 5000
# print(prueba)
#
# otra = [2,4,6,8]
#
# # Es posible unir dos listasen una simplemente haciendo esto (generando una nueva):
# union = lista+otra
# print(union)
#
# # Se puede hacer +=[x] para hacer lo mismo que el .append
# lista += [10000]
#
# print(lista)
#
# # Esto crea una lista de las listas metidas y si alguna se modifica, la lista de listas
# # tambien se modifica
#
# nombres = ["Ana","Pedro"]
# edades = [22,21]
# info = [nombres, edades]
#
# nombres[0] = "Juan"
# print(info)

cositas = ["Raquel", 12, 7.4, True, [1, 2, 3]]

print(len(cositas))
# Comprueba si "Raquel" está en la lista
print("Raquel" in cositas)  # -> True

# Comprueba si "13" no está en la lista
print(13 not in cositas)  # -> True

print(randint(1, 8))

# No son la misma cosa ! :
"Hola" + "adios"  # String
["Hola"] + ["Adios"]  # Lista

# Se puede hacer así
print(cositas[randint(0, len(cositas) - 1)])

# Pero es mas sencillo importando 'choice'
print(choice(cositas))

# INDEX

print(cositas.index(7.4))  # Devuelve la posicion en la lista de '7.4'

# MAX Y MIN

nombres = ["Juan", "Antonio", "David"]
print(max(nombres))  # -> Juan, ya que es por orden alfabético
print(min(nombres))  # -> Antonio "" "" "" ""

prueba3 = [True, True, False, True, False]
print(max(prueba3))  # -> Sale True
print(min(prueba3))  # -> Sale False

# SPLIT Si no tiene parametro lo divide todo por caracteres

nombre_entero = "Jesús González Pérez"
partes = nombre_entero.split(" ")
print(partes)

[nombre, apellido1, apellido2] = nombre_entero.split(" ")

print(nombre, apellido1, apellido2.upper())

# JOIN

print("".join(nombre_entero))


# Ordenar

numeros = [3,5,1,2,-3]

ordenada = sorted(numeros)
print(numeros)
print(ordenada)