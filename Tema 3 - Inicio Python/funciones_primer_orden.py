frutas = [{
    "nombre": "Manzana",
    "precio": 2.4,
    "categoria": "A"
},
    {
        "nombre": "Peras",
        "precio": 1.3,
        "categoria": "B"
    },
    {
        "nombre": "Naranjas",
        "precio": 4.4,
        "categoria": "C"
    }]


# Se puede hacer una función que devuelva los valores que queremos para luego meterselo a la funcion MAX y sacar el precio MAXIMO

def criterio(fruta):
    return fruta["precio"]


print(max(frutas, key=criterio))

# Tambien podemos usarlo en el sorted para orndear estructuras de datos segun el criterio que queramos:
print(sorted(frutas, key=criterio, reverse=True))

# Tambien es posible usar funciones sin nombre, llamadas lambda

print("LAMBDA MAX: ")
print(max(frutas, key=lambda fruta: fruta["precio"]))

# Incluso introduciendole mas parametros despues

print("LAMBDA SORTED: ")
print(sorted(frutas, key=lambda fruta: fruta["precio"], reverse=True))

frutas = {"Manzana": {
    "nombre": "Manzana",
    "precio": 2.4,
    "categoria": "A"},
    "Peras": {
        "nombre": "Peras",
        "precio": 1.3,
        "categoria": "B"},
    "Naranjas": {
        "nombre": "Naranjas",
        "precio": 4.4,
        "categoria": "C"}
}

# Recorriendo las values de un mapa, podemos tambien aplicar la ordenación.
print("LAMBDA MAX DICCIONARIO ")
print(max(frutas.values(),key=lambda fruta:fruta["precio"]))

print("LAMBDA SORTED DICCIONARIO ")
print(sorted(frutas.values(), key=lambda fruta:fruta["precio"]))

