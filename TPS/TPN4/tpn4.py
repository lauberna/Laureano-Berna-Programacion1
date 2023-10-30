""" ej 1 """
""" x = 0
while (x <= 30):
    x += 1
    if x == 15:
        print(f"The execution of the loop was broken when x was {x}")
        break
    elif x in (4, 6, 10):
        print(f"The value {x} of x was skipped.")
        continue
    else:
        print(f"The value of the loop is: {x}.") """


""" ej 2 """

""" lineas = []
while True:
    linea = input("ingresa una linea, nada para finalizar: ")
    if linea.strip() == "":
        break
    lineas.append(linea.upper())

print(lineas) """

""" ej 3 """
""" cuenta = 0
while True:
    entrada = input(
        "D MONTO(para depositar), R MONTO(para retirar), nada para finalizar: ").upper()
    if not entrada:
        break
    tipo, monto = entrada.split(" ")
    monto = int(monto)

    if tipo == "D":
        cuenta += monto

    elif tipo == "R":
        if monto < cuenta:
            cuenta -= monto
        else:
            print("no tiene suficiente saldo")
print(f"el total de la cuenta es de: {cuenta}") """

""" ej 4 """
""" cant_primos = 0

while True:
    num = int(input('Ingrese un numero o 0 para terminar: '))
    if num == 0:
        break
    aux = 0
    for i in range(1, num+1):
        if num % i == 0:
            aux += 1
    if (aux == 2):
        cant_primos += 1
        print("numero primo")
print(f"Cantidad de numeros primos: {cant_primos}") """

""" 5 """
""" anio1 = int(input("Ingrese el año 1"))
anio2 = int(input("Ingrese el año 2"))
inicio = min(anio1, anio2)
fin = max(anio1, anio2)
for anio in range(inicio, fin+1):
    if (((anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0) and anio % 10 == 0):
        print(f"año: {anio} es biciesto y multiplo de 10") """

""" ej 6 """
""" for i in range(1, 21):
    if (i % 2 != 0):
        continue
    print(f"{i}, es un numero par") """

""" ej 7 """
""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
buscar = int(input("Ingresa el numero a buscar: "))
for i in numeros:
    if buscar == i:
        print(f"Numero encontrado")
        break """

""" ej 8 """
while True:
    opcion = int(input("ingresa una opcion 1,2 o 3: "))
    if opcion == 0:
        break
    elif opcion == 1:
        print("opcion 1")
    elif opcion == 2:
        print("opcion 2")
    elif opcion == 3:
        print("opcion 3")
