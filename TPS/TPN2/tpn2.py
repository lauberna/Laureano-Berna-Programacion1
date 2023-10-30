""" print("ejercicio 1")
anos_computadora = int(
    input("Ingrese el número de años que tiene la computadora: "))
if anos_computadora < 0:
    print("Error: Ingrese un número positivo.")
else:
    if anos_computadora <= 2:
        print("El computador es nuevo.")
    else:
        print("El computador es viejo.") """

""" print("ejercicio 2")
numero = input("ingresa un numero: ")
if numero < 0:
  print("error: numero menor a 0") """

""" print("ejercicio 3")
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1[0].lower() == nombre2[0].lower():
    print("Coincidencia")
else:
    print("No hay coincidencia") """

""" print("ejercicio 4")
candidato = input("Elija un candidato (A, B o C): ")

if candidato == "A":
    print("Usted ha votado por el partido rojo.")
elif candidato == "B":
    print("Usted ha votado por el partido verde.")
elif candidato == "C":
    print("Usted ha votado por el partido azul.")
else:
    print("Opción errónea.") """

""" print("ejercicio 5")
letra = input("Ingrese una letra: ")
if len(letra) == 1 and letra.lower() in "aeiou":
    print("Es vocal")
else:
    print("No se puede procesar el dato.") """
""" print("ejercicio 6")
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.") """

""" print("ejercicio 7")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
mayor = 0

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
elif numero2 < numero3:
    print(numero2)
else:
    print(numero3) """

""" print("ejercicio 8")
nombre_usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

if nombre_usuario == "Gwenevere" and contrasena == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.") """

""" print("ejercicio 9")
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

if (sexo.lower() == "m" and nombre[0].lower() > "n") or (sexo.lower() == "f" and nombre[0].lower() < "m"):
    print("Usted pertenece al grupo A.")
else:
    print("Usted pertenece al grupo B.") """

""" print("ejercicio 10")
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 500
else:
    precio = 1000
print("El precio de la entrada es:", precio) """

""" print("ejercicio 11")
tipo_pizza = input("¿Desea una pizza vegetariana (V) o no vegetariana (N)? ")

if tipo_pizza.lower() == "v":
    print("Ingredientes vegetarianos disponibles: Pimiento y Tofu.")
else:
    print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón.")
ingrediente = input("Elija un ingrediente adicional: ")

if tipo_pizza.lower() == "v":
    print("Pizza vegetariana con mozzarella, tomate y", ingrediente)
else:
    print("Pizza no vegetariana con mozzarella, tomate y", ingrediente) """

""" print("ejercicio 12")
anio_actual = int(input("Ingrese el año actual: "))
anio_objetivo = int(input("Ingrese un año cualquiera: "))

if anio_objetivo > anio_actual:
    print("Faltan", anio_objetivo - anio_actual, "años para llegar a", anio_objetivo)
elif anio_objetivo < anio_actual:
    print("Han pasado", anio_actual - anio_objetivo, "años desde", anio_objetivo)
else:
    print("Los años son iguales.") """

""" print("ejercicio 13")
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 <= 0 or numero2 <= 0:
    print("Por favor, ingrese números positivos.")
elif numero1 % numero2 == 0:
    print(numero1, "es múltiplo de", numero2)
elif numero2 % numero1 == 0:
    print(numero2, "es múltiplo de", numero1)
else:
    print("Ninguno de los números es múltiplo del otro.") """

""" print("ejercicio 14")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print("La solución de la ecuación es x =", x) """

""" print("ejercicio 15")
opcion = input("¿Desea calcular el área de un triángulo (T) o un círculo (C)? ")

if opcion.lower() == "t":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * altura
    print("El área del triángulo es:", area)
elif opcion.lower() == "c":
    radio = float(input("Ingrese el radio del círculo: "))
    from math import pi
    area = pi * radio**2
    print("El área del círculo es:", area)
else:
    print("Opción no válida.") """

""" print("ejercicio 16")
a = float(input("Ingrese el primer valor (a): "))
b = float(input("Ingrese el segundo valor (b): "))
operacion = int(input("Seleccione la operación:\n1. Suma\n2. Multiplicación\n3. Resta\n4. División\n"))

if operacion == 1:
    resultado = a + b
    print("Resultado de la suma:", resultado)
elif operacion == 2:
    resultado = a * b
    print("Resultado de la multiplicación:", resultado)
elif operacion == 3:
    resultado = a - b
    print("Resultado de la resta:", resultado)
elif operacion == 4:
    if b != 0:
        resultado = a / b
        print("Resultado de la división:", resultado)
    else:
        print("No se puede dividir por cero.")
else:
    print("Operación no válida.") """

""" print("ejercicio 17")
dia = input("Ingrese un día de la semana: ")

if dia.lower() == "lunes":
    print("Es lunes, ¡ánimo!")
elif dia.lower() == "viernes":
    print("¡Viernes, por fin!")
elif dia.lower() == "sabado" or dia.lower() == "domingo":
    print("Es fin de semana, disfruta.")
else:
    print("Día invalido.") """

""" print("ejercicio 18")
horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))

if horas_trabajadas >= 48:
    horas_extras = horas_trabajadas - 48
    salario_total = (48 * salario_por_hora) + (horas_extras * salario_por_hora * 1.10)
else:
    salario_total = horas_trabajadas * salario_por_hora

print("Horas extras trabajadas:", horas_extras)
print("Salario total:", salario_total) """

""" print("ejercicio 19")
cantidad_lapices = int(input("Ingrese la cantidad de lápices: "))

costo_por_lapiz = 60
costo_total = cantidad_lapices * costo_por_lapiz

if cantidad_lapices >= 1000:
    costo_total -= 0.07 * costo_total

print("Costo total de los lápices:", costo_total) """

""" print("ejercicio 20")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 6:
    print("El alumno aprueba el curso con un promedio de", promedio)
else:
    print("El alumno reprueba el curso con un promedio de", promedio) """
