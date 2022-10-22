ejemplo={
    'A':45,
    "B":78
}
print(ejemplo['B'])

datos_persona={
    "nombre":"Juan",
    "apellido1":"Lopez",
    "apellido2":"Garcia",
    "edad":45,
    "sueldo":1900.67
}
print(datos_persona["sueldo"])

tienda={
    'patatas':20.5,
    'cocacola':2.5,
    'lechuga':5,
    'melon':4.3
}

print(tienda["patatas"])
print(tienda.get("sandia","No hay en la tienda"))
tienda["sandia"]=3.6
tienda["patatas"]=18
print(tienda["patatas"])
print(tienda.get("sandia","No hay en la tienda"))

copia=dict(tienda)
ofertas=dict([["jamon",12],["limon",0.6],["queso",2.3]])

del tienda["sandia"]#Elimina la clave que le pongamos
tienda.update(ofertas) #Añade el diccionario ofertas al diccionario tienda

print(ofertas)
print(copia)
print("patatas" in tienda)
print("cerezas" in tienda)

print(max(tienda,key=tienda.get))
print(min(tienda,key=tienda.get))

tienda.clear()

