""" ej 1 """
""" word = input("Ingresa una palabra: ")
for i in range(1, 11):
    print(word) """
""" ej 2 """
""" edad = int(input("Ingresa tu edad: "))
for i in range(edad + 1):
    print(i) """
""" ej 3 """
""" num = int(input("Ingresa un numero entero positivo: "))
for i in range(num+1):
    if i % 2 != 0:
        print(i, end=", ") """
""" ej 4 """
""" num1 = int(input("Ingresa un numero entero positivo: "))
for i in range(num1, 0, -1):
    print(i, end=", ") """
""" ej 5 """
""" inversion = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingrese el interes anual en porcentaje (%): "))
years = int(input("Cuantos años desea calcular? "))
ganancia = 0
total = inversion
for i in range(1, years+1):
    total += total * (interes/100)
print(f"El total seria de: {total:.2f}") """

""" ej 6 """
""" large = int(input("ingresa la altura del triangulo: "))
for i in range(1,large+1):
    print(i*"x") """

""" ej 7 """
""" for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print() """

    
""" ej 8 """
""" n = int(input("Introduce un numero entero positivo: "))
n = abs(n)
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("") """

""" ej 9 """
""" while True:
    password = "abc123"
    guess = input("Ingresa la contraseña: ")
    if guess == password:
        print("Acertaste")
        break
    else:
        print("Fallaste") """

""" ej 10 """
""" number = int(input("Ingrese un número entero: "))

if number <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{number} es un número primo.")
else:
    print(f"{number} no es un número primo.") """

""" ej 11 """
""" word = input("ingresa una palabra")
for letter in word[::-1]:
    print(letter) """

""" ej 12 """
""" frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

conteo = 0
for caracter in frase:
    if caracter == letra:
        conteo += 1

print(f"La letra '{letra}' aparece {conteo} veces en la frase.") """

""" ej 13 """
""" while True:
    entrada_usuario = input("Ingrese texto (escriba 'salir' para salir): ")
    if entrada_usuario == "salir":
        break
    print(entrada_usuario) """

""" ej 14 """
""" inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

print("Números pares:")
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)

print("Números impares:")
for num in range(inicio, fin + 1):
    if num % 2 != 0:
        print(num) """

""" ej 15 """
""" numero = int(input("Ingrese un número entero positivo: "))
print(f"Divisores de {numero}:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i) """

""" ej 16 """
""" count = int(input("Enter the number of integers to input: "))
negative_count = 0

for i in range(count):
    number = int(input("Enter a number: "))
    if number < 0:
        negative_count += 1

print(f"Ha ingresado {negative_count} número(s) negativo(s).") """

""" ej 17 """
""" phrase = input("Ingrese una frase: ").lower()
vowels = "aeiou"
found_vowels = []

for letter in phrase:
    if letter in vowels and letter not in found_vowels:
        found_vowels.append(letter)

print("Vocales en la frase:")
for vowel in found_vowels:
    print(vowel) """

""" ej 18 """
""" n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b """

""" ej 19 """
""" goal = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))
total_saved = 0

while total_saved < goal:
    amount = float(input("Ingrese la cantidad a ahorrar: "))
    if amount < 0:
        print("La cantidad debe ser positiva.")
    else:
        total_saved += amount

print(f"¡Ha alcanzado su objetivo de ahorro de ${goal}!") """

""" ej 20 """
""" sum = 0
while True:
    number = int(input("Ingrese un número (0 para terminar): "))
    if number == 0:
        break
    sum += number

print(f"La sumatoria de los números ingresados es {sum}.") """

""" ej 21 """
""" max_number = None

while True:
    number = int(input("Ingrese un número positivo (0 para salir): "))
    if number == 0:
        break
    if number < 0:
        print("El número debe ser positivo.")
        continue
    if max_number is None or number > max_number:
        max_number = number

if max_number is not None:
    print(f"El número más grande ingresado fue: {max_number}")
else:
    print("No se ingresaron números positivos.") """

""" ej 22 """
""" num = int(input("Ingrese números enteros positivos, o -1 para detenerse: "))
count_pares = 0

while num != -1:
    if num < 0:
        print("Número negativo, intente nuevamente.")
    else:
        suma_digitos = sum(map(int, str(num)))
        print(f"La suma de los dígitos de {num} es {suma_digitos}.")
        if suma_digitos % 2 == 0:
            count_pares += 1
    num = int(input("Ingrese otro número o -1 para detenerse: "))

print(f"Se ingresaron {count_pares} número(s) con suma de dígitos par.") """

""" ej 23 """
""" total_compras = 0

while True:
    monto_compra = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    if monto_compra < 0:
        print("El monto de la compra debe ser no negativo.")
    elif monto_compra == 0:
        break
    total_compras += monto_compra

if total_compras > 1000:
    total_compras -= total_compras * 0.10

print(f"Total a pagar: ${total_compras:.2f}") """

""" ej 24 """
""" n = int(input("Ingrese un número entero positivo: "))
factorial = 1

if n < 0:
    print("El número debe ser positivo.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}.") """

""" ej 25 """
""" n = int(input("Ingrese un número entero positivo: "))
factorial = 1

if n < 0:
    print("El número debe ser positivo.")
elif n == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}.")
 """