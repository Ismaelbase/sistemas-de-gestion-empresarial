def sumar(x, y):
    la_suma = x + y
    return la_suma


def rectangulo(alto, ancho):
    for i in range(alto):
        # Se multiplica el emoji por el ancho
        print("😂" * ancho)


def rectangulo_string(alto, ancho):
    res = ""
    for i in range(alto):
        res += "😜" * ancho + "\n"
    return res


print(sumar(1, 4))

# rectangulo(9,4)

print(rectangulo_string(8, 8))


# Se puede poner una funcion que no haga nada para rellenarla mas tarde asi:

def area_perimetro(radio):
    pass


# Se puede devolver mas de un valor, devolviendo tuplas o diccionarios:

def area_perimetro_cuadrado(lado):
    return {"area": lado ** 2, "perimetro": lado * 4}


# Se puede meter los parametros por nombre, desordenados si quieres:
# def area_triangulo(base,altura):
#     return base*altura/2
#
# print(area_triangulo(altura=4,base=5), end="\n")

# Tambien se pueden poner parametros por defecto !


def area_triangulo(base=5, altura=10):
    return base * altura / 2


print(area_triangulo())
