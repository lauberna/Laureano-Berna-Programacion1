# EJERCICIO 1
""" correr_mensaje = int(input("ingrese la cantidad de caracteres a correr: "))
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for index in range(4):
    mensaje = input(f"ingrese el msj {index+1}: ").lower()
    nuevo_mensaje = ""
    for letra in mensaje:
        if letra in alfabeto:
            posicion = alfabeto.index(letra)
            nuevo_mensaje += alfabeto[(posicion+correr_mensaje) % 26]
        else:
            nuevo_mensaje += letra
    print(nuevo_mensaje) """

# EJERCICIO 2
""" totalP = 0
totalI = 0
while True:
    num = input("ingrese un numero entero positivo, 0 para finalizar: ")
    par = 0
    impar = 0
    if int(num) == 0:
        break
    for dig in num:
        if int(dig) % 2 == 0:
            par += 1
            totalP += 1
        else:
            impar += 1
            totalI += 1
    print(f"pares: {par}, impares: {impar}")
print(f"pares totales: {totalP}, impares totales: {totalI}") """
