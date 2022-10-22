print("Hola mundo.")

cadena = "Python"
# print(cadena[3])
# print(cadena[-1])
# print(cadena[7]) No permitido ya que sale del rango de la cadena por la derecha.
# print(cadena[-7]) No permitido ya que sale del rango de la cadena por la izquierda.

# print(cadena[::2]) -> Pto
# print(cadena[::-2]) -> nhy
# print(cadena[:-cadena.__sizeof__():-2]) -> Esto sirve para el length de la cadena.
# print(cadena[:-len(cadena):-2]) -> Esto también sirve para el length de la cadena.

# print(cadena*3)
#
# emoji = "😉"
# linea = emoji*5
# cuadrado = f"{linea}\n"*5
# print(cuadrado)

# print("P" in cadena) # -> Devuelve un booleano si contiene "P"
# print("tho" in cadena) # -> Devuelve un booleano si contiene "tho"
# print("yn" not in cadena) # -> Devuelve un booleano si NO contiene "yn"

cadena == "python" # Devuelve un booleano diciendo si es igual a cadena: "Python".
cadena < "python" # Devuelve un booleano diciendo si cadena es menor que "python" en ASCII.


# print(cadena.lower())
# print(cadena.upper())
# frase = "hoy es lunes y es por la tarde."
# print(frase.capitalize())

print("45.5".isnumeric())