from random import choice
numeros=[1,2,3,4,5]
operacion=input("Que operacion quieres realizar?")

if operacion == "sum":
    res=0
    for num in numeros:
        res+=num
elif operacion == "multi":
    res=1
    for num in numeros:
        res*=num
elif operacion == "ale":
    res=choice(numeros)
else:
    res="No existe"