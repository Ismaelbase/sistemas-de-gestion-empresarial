# Ejercicio 28 - MCM

def min_comun_multiplo(n1, n2):
    if n1 == n2:
        resultado = f"El minimo común multiplo es : {n1}"
        return resultado
    else:
        mayor = 0
        if n1 > n2:
            mayor = n1
        else:
            mayor = n2


    while (True):
        if ((mayor % n1 == 0) and (mayor % n2 == 0)):
            mcm = mayor
            break
        mayor += 1
    return mcm

print(min_comun_multiplo(10, 111))


# Ejercicio 28 - MCD

def min_comun_divisor(n1,n2):
    if n1 == n2:
        return f"El minimo común divisor es {n1}"
    else:
        minimo = min(n1,n2)

        while minimo > 0:
            if n1 % minimo == 0 and n2 % minimo == 0:
                return minimo
                break
            minimo -= 1

print(min_comun_divisor(60,12))
