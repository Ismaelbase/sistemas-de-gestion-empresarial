# Ejercicio 1
#
# opcion = input("Que tipo de comida quieres?: ")
#
# comidas = {
#     "fruta":"Manzana, platano o pera.",
#     "verdura":"Tomate, lechuga o zanahoria",
#     "carne":"Cerdo, ternera o pollo",
#     "pescado":"Sardinas, caballa o salmonete"
# }
#
# resultado = comidas.get(opcion.lower(), "No tenemos de ese tipo de comida");
#
# print(resultado)

# Ejercicio 2
#
# def mostrar(lista):
#     for i in range(len(lista)):
#         print(f"Posicion {i} -> {lista[i]}")
#
# def modificar(lista):
#     for i in range(len(lista)):
#
#         print(f"Posicion {i} antes de modificar -> {lista[i]}")
#         lista[i] *= 2
#         print(f"Posicion {i} despues de modificar -> {lista[i]}")
#
# def longitud(lista):
#     print(len(lista))
#
# lista_ejemplo = [5,10,15,20,25,30]
#
#
# print("Puedes [mostrar] una lista, [modificar] multiplicando por dos sus valores o mostrar su [longitud]. ")
# opcion = input("Que opcion deseas: ")
# print("")
#
# opciones = {
#     "mostrar":mostrar,
#     "modificar":modificar,
#     "longitud":longitud
# }
#
# print(opciones.get(opcion)(lista_ejemplo))
#


# Ejercicio 3

# numero = int(input("Dime un numero: "))
# opcion = input("Dime si quieres cambiarlo a [octal], [binario] o [hexadecimal]: ")
#
# convertir = {
#     "octal":format(numero, 'o'),
#     "binario":format(numero, 'b'),
#     "hexadecimal":format(numero, 'x')
# }
#
#
# print(convertir.get(opcion))

# Ejercicio 4
#
# persona = {
#     "nombre": "daniel garcía peraltes",
#     "edad": 29,
#     "peso": 87,
#     "altura": 183
# }
#
# info = {
#     "La persona":persona.get("nombre"),
#     persona.get("edad"):"años",
#     persona.get("peso"):"kilos",
#     persona.get("altura"):"centimetros"
#
# }
#
# for clave,valor in info.items():
#     print(str(clave)+" "+str(valor))

# Ejercicio 5

producto = {
    "nombre":"Solomillo a la pimienta verde",
    "precio":"18.95798",
    "calorias":"1050",
    "vegano":"False"
}

cambio = {
    "nombre":str(producto.get("nombre")),
    "precio":float(producto.get("precio")),
    "calorias":int(producto.get("calorias")),
    "vegano":bool(producto.get("vegano"))
}

for clave,valor in producto.items():
    producto[clave]=cambio.get(clave)

print(producto)