# Ejercicio 24

# numero = input("Dime un numero: ")
#
# if numero.isnumeric():
#     diccionario1 = {
#         "1": "Uno",
#         "2": "Dos",
#         "3": "Tres",
#         "4": "Cuatro",
#         "5": "Cinco",
#         "6": "Seis",
#         "7": "Siete",
#         "8": "Ocho",
#         "9": "Nueve"
#     }
#     for digito in numero:
#         print(diccionario1[digito], end=" / ")
# else:
#     print("No introduciste un numero")


# Ejercicio 25

# diccionario2 = {
#     ":(":"🙁",
#     ":)":"😀",
#     ":l":"😐",
#     ">:(":"😡",
#     ":P":"😛",
#     ":3":"😽",
#     "UwU":"😊",
#     "xP":"😝",
#     ":o":"😱",
#     "<3":"❤",
#     ":D":"😁"
# }
#
# texto = "Hola :D ¿Te gustaría verni al cine? :) ¿No? :( porfa UwU"
#
# texto_partido = texto.split(" ")
#
# for i in range(len(texto_partido)):
#     if texto_partido[i] in diccionario2.keys():
#         texto_partido[i] = diccionario2[texto_partido[i]]
#
#
# texto = " ".join(texto_partido)
# print(texto)

# Ejercicio 26 normal

# nombres = "Michelle,Ismael,Espe,Ángel,Araceli"
# edades = "23,29,28,39,30"
#
# nombres_partidos = nombres.split(",")
# edades_partidos = edades.split(",")
#
# dato = []
# datos = {}
#
# for i in range(len(nombres.split(","))):
#
#     dato.append([nombres_partidos[i],edades_partidos[i]])
#     datos.update(dato)
#     dato.clear()
#
#
# print(datos)
#
# print(datos["Michelle"])

# Ejercicio 26 con Zip

nombres = "Michelle,Ismael,Espe,Ángel,Araceli"
edades = "23,29,28,39,30"

nombres_partidos = nombres.split(",")
edades_partidos = edades.split(",")

datos = zip(nombres_partidos,edades_partidos)

# Por cada nombre / edad en el zip de nombre edad...?
diccionario = {nombres_partidos:edades_partidos for nombres_partidos,
               edades_partidos in zip(nombres_partidos,edades_partidos)}


print(diccionario)