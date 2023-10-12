""" ej 1 """

""" base = 12
altura = 33
print(f"el perimetro del rectangulo es: {base*2 + altura*2}")
print(f"el area del rectangulo es: {base*altura}") """

""" ej 2 """

""" cateto1 = 30
cateto2 = 25
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f"la hipotenusa es: {hipotenusa}") """

""" ej 3 """

"""
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print("Suma:", suma)
print("Resta:", resta)
print("División:", division)
print("Multiplicación:", multiplicacion) """

""" ej 4 """

""" fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.") """

""" ej 5 """

""" 
a) no encuentro error
b) el precio se almacenaria en string
c) al momento de mostrar la edad no esta utilizando comillas
d) para comparar se utiliza doble == no un solo =
 """

""" nombre = "Lau"
A = input(f"{nombre} ¿Cuál es tu canción favorita?")
precio = float(input("Precio: "))
total = precio + (precio * 0.1)
edad = int(input("Edad: "))
print("Tu edad es", edad)
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad == 18) """


""" ej 6 """

""" num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

media = (num1 + num2 + num3) / 3

print("La media de los tres números es:", media) """

""" ej 7 """

""" minutos = int(input("Ingresa la cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.") """


""" ej 8 """

""" sueldo_base = float(input("Ingresa el sueldo base del vendedor: "))
ventas = float(input("Ingresa el total de ventas del vendedor en el mes: "))

comision = ventas * 0.10
sueldo_total = sueldo_base + comision

print("El vendedor obtendrá ${:.2f} en comisiones y un sueldo total de ${:.2f} en el mes.".format(comision, sueldo_total)) """


""" ej 9 """

""" total_compra = float(input("Ingresa el total de la compra: "))

descuento = total_compra * 0.15
total_pagar = total_compra - descuento

print("El descuento aplicado es de ${:.2f} y el cliente deberá pagar ${:.2f} finalmente.".format(descuento, total_pagar)) """

""" ej 10 """

""" parcial1 = float(input("Ingresa la calificación del primer parcial: "))
parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial3 = float(input("Ingresa la calificación del tercer parcial: "))
examen_final = float(input("Ingresa la calificación del examen final: "))
trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("La calificación final del alumno en Algoritmos es:", calificacion_final) """

""" ej 11 """

""" numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
distancia = abs(numero1 - numero2)
print("La distancia entre los dos números es:", distancia) """

""" ej 12 """

""" numero = float(input("Ingresa un número: "))
print(f"La raíz cuadrada de {numero} es {numero ** 0.5}")
print(f"La raíz cúbica de {numero} es {numero ** (1/3)}") """

""" ej 13 """

""" numero = int(input("Ingresa un número de dos cifras: "))
unidades = numero % 10
decenas = numero // 10
numero_invertido = unidades * 10 + decenas
print("El número invertido es:", numero_invertido) """

""" ej 14 """
""" print("forma 1")
A = input("Ingresa el valor de A: ")
B = input("Ingresa el valor de B: ")
print("Valores iniciales: A =", A, "y B =", B)
A, B = B, A
print("Valores intercambiados: A =", A, "y B =", B) """

""" print("forma 2")
A = input("Ingresa el valor de A: ")
B = input("Ingresa el valor de B: ")
print("Valores iniciales: A =", A, "y B =", B)
aux = A
A = B
B = aux
print("Valores intercambiados: A =", A, "y B =", B) """

""" ej 15 """

""" ej 16 """

""" nombre = input("Ingresa tu nombre: ")
apellido1 = input("Ingresa tu primer apellido: ")
apellido2 = input("Ingresa tu segundo apellido: ")
iniciales = nombre[0] + apellido1[0] + apellido2[0]
print("Las iniciales son:", iniciales.upper()) """

""" ej 17 """

""" usuario = input("Ingresa tu nombre: ")
print(f"Ahora estás en la matrix, {usuario}.") """

""" ej 18 """

""" costo_cena = float(input("Ingresa el costo de la cena: "))
servicio = costo_cena * 0.062
propina = costo_cena * 0.10
monto_final = costo_cena + servicio + propina
print(f"Monto final a pagar: ${monto_final}") """

""" ej 19 """

""" dia = int(input("Ingresa el día de tu nacimiento: "))
mes = int(input("Ingresa el mes de tu nacimiento: "))
año = int(input("Ingresa el año de tu nacimiento: "))
fecha_nacimiento = f"{dia:02d}/{mes}/{año}"
print("Fecha de nacimiento:", fecha_nacimiento) """

""" ej 20 """

""" dia = int(input("Ingresa el día de tu nacimiento: "))
mes = int(input("Ingresa el mes de tu nacimiento: "))
año = int(input("Ingresa el año de tu nacimiento: "))
fecha_nacimiento = f"{dia:02d}{mes}{año}"
print("Fecha de nacimiento en formato DDMMAAAA:", fecha_nacimiento) """

""" ej 21 """

""" kilometros_por_litro = float(
    input("Cuántos kilómetros por litro recorre la moto: "))
capacidad_tanque_litros = float(input("Capacidad del tanque en litros: "))
distancia_total_kilometros = float(
    input("Cuántos kilómetros recorrerán en total: "))

kilometros_por_tanque = kilometros_por_litro * capacidad_tanque_litros
tanques_necesarios = distancia_total_kilometros / kilometros_por_tanque
print(
    f"Necesitarán {tanques_necesarios:.1f} tanques de combustible para el viaje.") """
