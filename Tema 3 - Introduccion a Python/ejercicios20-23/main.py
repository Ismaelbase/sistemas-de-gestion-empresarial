# Ejercicio 20 - Palabras que aparecen en las dos listas.

Peces = ["Lubina","Atún","Lenguado","Anchoa","Bonito","Dorada","Trucha"]
Animales = ["Lémur","Trucha","Girafa","Pantera","Atún","León","Anchoa"]

Repetidos = ""
for i in Peces:
    for j in Animales:
        if i == j:
            Repetidos += i+" "

print(Repetidos)


# Ejercicio 20 - Palabras que solo estan en la primera lista.

Solo_primera_lista = ""
# aparece = False
#
# for i in Peces:
#     aparece = False
#     for j in Animales:
#         if i == j:
#             aparece == True
#     if aparece == False:
#         Solo_primera_lista += i + " "


for peces in Peces:
    if peces not in Animales:
        Solo_primera_lista += peces + " "

print(Solo_primera_lista)


# Ejercicio 20 - Palabras que solo estan en la segunda lista.

animales_segunda = ""

for animal in Animales:
    if animal not in Peces:
        animales_segunda += animal + " "

print(animales_segunda)

# Ejercicio 20 - Palabras que aparecen en ambas listas.

repetidas2 = ""

for repetidos in Peces:
    if repetidos in Animales:
        repetidas2 += repetidos +" "

print(repetidas2)

# Ejercicio 21

Flores = ["Rosa","Tulipan","Girasol","Rosa","Orquidea","Margarita","Margarita","Calendula"] #Se repite Rosa y Margarita
flores_sin_repetidos = []

for flor in Flores:
    if flor not in flores_sin_repetidos:
        flores_sin_repetidos.append(flor)

print(flores_sin_repetidos)

# Ejercicio 22

Texto = "Cuantas vocales tendra esta frase? Ni idea, vamos a averiguarlo."
contador = 0
for letra in Texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1

print(contador)

# Ejercicio 23

cuenta_a = 0
cuenta_e = 0
cuenta_i = 0
cuenta_o = 0
cuenta_u = 0

for letra in Texto:
    if letra == "a":
        cuenta_a += 1
    elif letra =="e":
        cuenta_e += 1
    elif letra == "i":
        cuenta_i += 1
    elif letra == "o":
        cuenta_o += 1
    elif letra == "u":
        cuenta_u += 1

print(f"Hay {cuenta_a} vocales 'a'")
print(f"Hay {cuenta_e} vocales 'e'")
print(f"Hay {cuenta_i} vocales 'i'")
print(f"Hay {cuenta_o} vocales 'o'")
print(f"Hay {cuenta_u} vocales 'u'")