#Ejercicio 1

peso = float(input("Dime tu peso en kg:"))
altura = float(input("Dime tu altura en metros:"))

indice = round(peso/(altura**2), 2)

print(f"Tu indice de masa corporal es {indice}.")

#Ejercicio 2

dias = int(input("Dime un número de dias:"))

horas = dias*24
minutos = horas*60
segundos = minutos*60

print(f"{dias} dias son {horas} horas, {minutos} minutos y {segundos} segundos.")

#Ejercicio 3

cm = float(input("Dime una longitud en centimetros:"))
shaku = round(cm/30.3,2)
ken = round(shaku*6,2)

print(f"{cm} centimetros son {ken} kens y {shaku} shakus.")

#Ejercicio 4

binario = "1010101"
decimal = int(binario,2)
print(decimal)
