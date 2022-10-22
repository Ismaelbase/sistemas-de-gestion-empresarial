# Ejercicio 20 - Palabras que aparecen en las dos listas.

Peces = ["Lubina", "Atún", "Lenguado", "Anchoa", "Bonito", "Dorada", "Trucha"]
Animales = ["Lémur", "Trucha", "Girafa", "Pantera", "Atún", "León", "Anchoa"]

Repetidos = []
# for i in Peces:
#     for j in Animales:
#         if i == j:
#             Repetidos.append(i)
#


for pez in Peces:
    if pez in Animales:
        Repetidos.append(pez)

print(Repetidos)

# Ejercicio 20 - Palabras que solo están en la primera lista.

Solo_primera_lista = []
# aparece = False
#
# for i in Peces:
#     aparece = False
#     for j in Animales:
#         if i == j:
#             aparece == True
#     if aparece == False:
#         Solo_primera_lista += i + " "


for pez in Peces:
    if pez not in Animales:
        Solo_primera_lista.append(pez)

print(Solo_primera_lista)

# Ejercicio 20 - Palabras que solo están en la segunda lista.

animales_segunda = []

for animal in Animales:
    if animal not in Peces:
        animales_segunda.append(animal)

print(animales_segunda)

# Ejercicio 20 - Unir sin repetidas.
repetidas2 = Peces

for animal in Animales:
    if animal not in Peces:
        repetidas2.append(animal)

print(repetidas2)

# Ejercicio 21

Flores = ["Rosa", "Tulipán", "Girasol", "Rosa", "Orquídea", "Margarita", "Margarita",
          "Calendula"]  # Se repite Rosa y Margarita
flores_sin_repetidos = []

for flor in Flores:
    if flor not in flores_sin_repetidos:
        flores_sin_repetidos.append(flor)

print(flores_sin_repetidos)

# Ejercicio 21 corregido mejor:

for flor in Flores:
    veces_repetida = Flores.count(flor)
    if Flores.count(flor) > 1:
        contador = 0
        while contador < veces_repetida - 1:
            Flores.remove(flor)
            contador += 1

print(Flores)

# Ejercicio 21 - Otro ejemplo mejor:
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for flor in Flores:
    if flor.count(flor) > 1:
        Flores.remove(flor)
print(Flores)

# Ejercicio 22

Texto = "Cuantas vocales tendrá esta frase? Ni idea, vamos a averiguarlo."
contador = 0
for letra in Texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1

vocales = ["a", "e", "i", "o", "u"]

cuenta = 0

for vocal in vocales:
    if vocal in Texto:
        cuenta += Texto.count(vocal)

print("=========================")
print(cuenta)

# Otra forma de hacer el 22 mejor:

cuenta2 = 0

for letra in Texto:
    if letra.lower() in 'aeiou':
        contador += 1
print(cuenta2)

print(f"Hay un total de {contador} vocales en la frase -> {Texto}")

# Ejercicio 23

cuenta_a = 0
cuenta_e = 0
cuenta_i = 0
cuenta_o = 0
cuenta_u = 0

for letra in Texto:
    if letra == "a":
        cuenta_a += 1
    elif letra == "e":
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

print("========================")

# Contar cada vocal por separado.

vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    if vocal in Texto:
        print(f"Hay {Texto.count(vocal)} vocales {vocal}.")



# Practica clase

num = input("Dime un número float")

partes = num.split(".")

if len(partes) == 2 and partes[0].isnumeric() and partes[1].isnumeric():
    print("Es un número float !")
else:
    print("No es un número float !")





