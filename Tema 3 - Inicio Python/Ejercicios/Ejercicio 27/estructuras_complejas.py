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

# print(agenda_lista, agenda_dicc)

texto = """dni;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

# Printer lista de manera bonita:
#
# for persona in agenda_lista:
#     for (clave,valor) in persona.items():
#         print(f"{clave} -> {valor}", end=" \n")
#     print("=============================")
#

# ============= Otra forma =======================
#
# for persona in agenda_lista:
#     for atributo in persona.items():
#         print(f"{atributo[0]} -> {atributo[1]}", end=" \n")
#     print("=============================")
#

# Printer de la agenda de manera bonita:
#
# for agenda in agenda_dicc.values():
#     for atributo in agenda.items():
#         print(f"{atributo[0]} -> {atributo[1]}", end=" \n")
#     print("=============================")
#

# Para conseguir un valor del diccionario:
#
# dni = input("Dime el dni de la persona a buscar: ")
# print(agenda_dicc.get(dni, "Ese dni no esta en la base de datos"))

# Para hacerlo en la lista es mas complejo
#
# dni = input("Dime el dni de la persona a buscar: ")
# buscado = None
#
# for persona in agenda_lista:
#     if (persona['dni'] == dni):
#         # Se puede printear directamente.
#         # print(persona)
#         # Tambien hacer una copia e imprimir al final del bucle
#         buscado = {**persona}
#         break  # Se puede usar para parar el bucle !
#
# if buscado is None:
#     print("Ese DNI no esta en la base de datos.")
# else:
#     print(buscado)

# 27.1
#
#
# todo = []
# diccionario = dict()
#
# lineas = texto.split("\n")
# cabecera = lineas[0].split(";")
#
# for i in range(1,len(lineas)):
#     datos = lineas[i].split(";")
#     conjunto = dict(zip(cabecera, datos))
#     conjunto['descuento'] = float(conjunto['descuento'])
#     todo.append(conjunto)
#
# print(todo)

# 27.1 Atencion a como recorre la lista en este ejemplo: !!

# todo = []
# diccionario = dict()
#
# lineas = texto.split("\n")
# cabecera = lineas[0].split(";")
#
# for linea in lineas[1:]:
#     datos = lineas.split(";")
#     conjunto = dict(zip(cabecera, datos))
#     todo.append(conjunto)

# print(todo)

# 27.2


# diccionario = dict()
# diccinario2 = dict()
#
# lineas = texto.split("\n")
# cabecera = lineas[0].split(";")
#
# for i in range(1,len(lineas)):
#     datos = lineas[i].split(";")
#     diccinario2 = dict(zip(cabecera, datos))
#     diccionario[datos[0]]=diccinario2
#
# print(diccionario)

# 27.2 Dani

agenda_dicc = dict()
lineas = texto.split("\n")
cabecera = lineas[0].split(";")

for linea in lineas[1:]:  # <--- Atento a esto !
    datos = linea.split(";")
    persona = dict(zip(cabecera, datos))
    persona["descuento"] = float(persona["descuento"])
    agenda_dicc[persona["dni"]] = persona

print(agenda_dicc)
