def suma(x, y):
    return x + y


resultado = suma(5, 8)


# print(f"Resultado: {resultado}")

# *datos hace que los datos introducidos se traten como una lista
def sumarTodo(*datos):
    total = 0
    for numero in datos:
        total += numero
    return total


resultado = sumarTodo(5, 8)
# print(f"Resultado: {resultado}")

resultado = sumarTodo(5, 5, 34, 3, 2, 1)


# print(f"Resultado: {resultado}")


# **datos hace que los valores introducidos se interpreten como un diccionario ! !
def mostrarDatos(**datos):
    for (clave, valor) in datos.items():
        print(f"{clave} vale {valor}")


mostrarDatos(sandia=5, loro=3, coche=15)
