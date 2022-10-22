# """
# Esto es un comentario de varias lineas,0
# se escribe poniendo 3 comillas a cada lado :P
# """
# # Definir variables:
# valor_entero = 32
# valor_decimal = 55.5
# valor_booleano = False
# valor_string = "Hello World."
# #se puede definir separadores con sep=""
# print(valor_entero, valor_decimal, valor_booleano, valor_string, sep=";", end="\n\n")
# print("Siguiente print :P.")
# # Asi se pueden concatener cosas
# print(valor_decimal, "minutos")
# print(type(valor_entero), type(valor_string))
#
# PI = 3.1415
# radio = 5.2
# area = PI*radio**2 # **2 es elevado a 2
# # Metiendo una instruccion entre parentesis hace que se puedan poner en varias lineas.
# area=(PI*
#       radio
#       **2)
# print(area)
#
# frase = \
# """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
# industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
# make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing
# Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of
# Lorem Ipsum.
# """
#
# print(frase)
#
# numero = 7//3
# print(numero)


variable1, variable2 = 12.4, 13.4

nombre, apellido1, apellido2 = "Ismael", "Bachaou", "sevilla"

print(nombre,apellido1,apellido2, sep=";")

a = 1
b = 5

a,b = b,a

print(a,b)

a += 5
b -= 3

print(a,b)

c = None

name = "Pepe"
edad = 30
print("La persona llamada "+name+" tiene "+str(edad)+" años.")

print("La persona llamada", name, "tiene", edad, "años.")

print(bool(-123))
print(bool(0))

num1 = 1.56234

num2 = 1.434

print(round(num1, 3)) #round() redondea hasta el digito que selecciones.
print(round(num2))

# Es necesario poner f antes de la frase a la que vamos a introducir variables entre llaves
frase = f"La persona llamada {name.upper()} tiene \
{edad+35} años";

print(frase)

# nombre_completo = input("Dime tu nombre completo: ")
# print(f"Tu nombre completo es {nombre_completo}")
#
# edad = int(input(f"Dime tu edad {nombre_completo}:"))
# print(f"El cuadrado de tu edad es {edad**2}")
