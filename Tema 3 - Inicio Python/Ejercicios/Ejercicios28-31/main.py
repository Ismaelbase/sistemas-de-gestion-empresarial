# Ejercicio 28 - MCM

# def min_comun_multiplo(n1, n2):
#     if n1 == n2:
#         resultado = f"El minimo común multiplo es : {n1}"
#         return resultado
#     else:
#         mayor = 0
#         if n1 > n2:
#             mayor = n1
#         else:
#             mayor = n2
#
#
#     while (True):
#         if ((mayor % n1 == 0) and (mayor % n2 == 0)):
#             mcm = mayor
#             break
#         mayor += 1
#     return mcm
#
# print(min_comun_multiplo(10, 111))


# Ejercicio 28 - MCD

# def min_comun_divisor(n1,n2):
#     if n1 == n2:
#         return f"El minimo común divisor es {n1}"
#     else:
#         minimo = min(n1,n2)
#
#         while minimo > 0:
#             if n1 % minimo == 0 and n2 % minimo == 0:
#                 return minimo
#                 break
#             minimo -= 1
#
# print(min_comun_divisor(60,12))

# Ejercicio 29
#
# def dar_vuelta_int(n1):
#
#     return int("".join(list(str(n1))[::-1]))
#
#
# print(dar_vuelta_int(54321))


# Ejercicio 30 - Frecuencia de palabras


def frencuencia_palabras(texto:str = ""):

    diccionario = dict()

    for palabra in texto.split(" "):
        if palabra in diccionario:
            diccionario[palabra]=diccionario.get(palabra)+1
        else:
            diccionario[palabra] = 1

    return diccionario;

texto = "Clavel Clavel Hortensia Lirio Rosa Tulipán Clavel Margarita Rosa Tulipán Margarita Caléndula Rosa Rosa Camelia Petunia Clavel Petunia Hortensia Tulipán"

texto_dicc = frencuencia_palabras(texto)

print(frencuencia_palabras(texto))

# Ejercicio 30 - Palabra más repetida

def palabra_mas_repetida(dicc:dict):

    maxima = max(dicc.values())
    for (clave,valor) in dicc.items():
        if valor == maxima:
            mas_repetida = tuple((clave,valor))
            break

    return mas_repetida

print(palabra_mas_repetida(texto_dicc))


# Ejercicio 31

agenda_dicc = {
    '01234567L':
        {'dni': '01234567L', 'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576',
         'descuento': 12.5},
    '71476342J':
        {'dni': '71476342J', 'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321',
         'descuento': 8.0},
    '63823376M':
        {'dni': '63823376M', 'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233',
         'descuento': 5.2},
    '98376547F':
        {'dni': '98376547F', 'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855',
         'descuento': 15.7}
}


def mas_descuento_dicc(dicc:dict):
    maximo = list(dicc.values())
    menor = maximo[0].get('descuento')

    for cliente in maximo:
        if cliente.get('descuento') > menor:
            menor = cliente.get('descuento')
            cliente_mas_descuento = cliente

    return cliente_mas_descuento

print(mas_descuento_dicc(agenda_dicc))






agenda_lista = [
    {'dni': '01234567L', 'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576',
     'descuento': 12.5},
    {'dni': '71476342J', 'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321',
     'descuento': 8.0},
    {'dni': '63823376M', 'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233',
     'descuento': 5.2},
    {'dni': '98376547F', 'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855',
     'descuento': 15.7}
]

def mas_descuento_list(lista:list):
    menor = agenda_lista[0].get('descuento')


    for cliente in lista:
        if cliente.get('descuento')>menor:
            menor = cliente.get('descuento')
            mas_descuento = cliente

    return mas_descuento

print(mas_descuento_list(agenda_lista))






























