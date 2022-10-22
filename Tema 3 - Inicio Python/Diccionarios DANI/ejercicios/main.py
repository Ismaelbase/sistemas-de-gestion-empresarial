#EJERCICIO 20

# lista1=["paco","pepino","hierba","perro"]
# lista2=["paco","pepino","platano","patata"]
#
# comunes=[]
# solo_primera=[]
# solo_segunda=[]
#
# unir_sin_repes=[*lista1]
# for palabra in lista2:
#     if palabra not in lista1:
#         unir_sin_repes.append(palabra)
#
# print(unir_sin_repes)
#
# for palabra in lista1:
#     if palabra in lista2:
#         comunes.append(palabra)
#
# print(comunes)
#
# for palabra in lista1:
#     if palabra not in lista2:
#         solo_primera.append(palabra)
# print(solo_primera)
#
# for palabra in lista2:
#     if palabra not in lista1:
#         solo_segunda.append(palabra)
# print(solo_segunda)

############################
#EJERCICIO 21
lista=[3,1,2,4,3,4,6,7,8,9,7,1,7,7,3,8]

nueva=[]
# for numero in lista:
#     if numero not in nueva:
#         nueva.append(numero)
# print(nueva)
# 
# for numero in lista:
#     veces_repetida=lista.count(numero)
#     if veces_repetida>1:
#         contador=0
#         while contador<veces_repetida-1:
#             lista.remove(numero)
#             contador+=1
# print(lista)
# for numero in lista:
#     if numero not in nueva:
#         nueva.append(numero)
# print(nueva)
# 
# for numero in lista:
#     veces_repetida=lista.count(numero)
#     if veces_repetida>1:
#         contador=0
#         while contador<veces_repetida-1:
#             lista.remove(numero)
#             contador+=1
# print(lista)


######################
#EJERCICIO 22
texto="Hola me llamo Manolo y quiero una piruleta"
#
# contador=0
# for letra in texto:
#     if letra.lower() in 'aeiou':
#         contador+=1
# print(contador)
#######################
#EJERCICIO 23
contadores={}
for letra in texto:
    if letra.lower() in "aeiou":
        veces=contadores.get(letra,0)+1
        contadores[letra]=veces;
print(contadores)
# contador_a=0
# contador_e=0
# contador_i=0
# contador_o=0
# contador_u=0
# vocales=['a','e','i','o','u']
# for vocal in vocales:
#     if vocal in texto:
#         print(f"Hay {texto.count(vocal)} {vocal}")
#
# for letra in texto:
#     if letra.lower()=='a':
#         contador_a+=1
#     elif letra.lower()=='e':
#         contador_e += 1
#     elif letra.lower()=='i':
#         contador_i += 1
#     elif letra.lower()=='o':
#         contador_o += 1
#     elif letra.lower()=='u':
#         contador_u += 1
#
# print(contador_a,contador_e,contador_i,contador_o,contador_u,sep=' ')


numero=input("Dime un número float:")

partes=numero.split(".")

if len(partes)==2 and partes[0].isnumeric() and partes[1].isnumeric():
    print("Es un número float")
    numero=float(numero)
else:
    print("No es un número float")






















