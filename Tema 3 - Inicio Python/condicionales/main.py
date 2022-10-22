edad = int(input("Dime la edad que tienes: "))
#
# if edad >= 18:
#     print("Correcto, puede pasar.")
#     #pass se usa para ignorar un bloque
# else:
#     print("No tiene permitted el paso.")

print("Hasta luego.")

if 0 <= edad < 18:
    print("Usted es joven todavía.")
elif 18 <= edad < 65:
    print("Usted está en edad de trabajar.")
elif edad < 0:
    print("Introduce un valor positivo.")
else:
    print("Usted podría jubilarse.")
# Control + Alt + L -> Ordenar codigo

