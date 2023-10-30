import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")
import Functions
""" ej 1 """
""" print(Functions.validar_dni(input("Ingresa tu dni: "))) """

""" ej 2 """
""" string = "hola como estas"
print(Functions.count_letters(string)) """

""" ej 3 """
""" while True:
    nombre_completo = input("Ingrese el nombre completo del socio (nombre apellido): ")
    if nombre_completo == "":
        break
    
    dni = input("Ingrese el número de DNI (7 u 8 dígitos): ")
    while not Functions.validar_dni(dni):
        print("Número de DNI inválido. Debe tener 7 u 8 dígitos.")
        dni = input("Ingrese el número de DNI nuevamente: ")

    palabras = nombre_completo.split()
    primer_nombre = palabras[0]
    apellido = palabras[-1]

    identificador = primer_nombre + str(len(apellido)) + dni[:3]
    print(f"ID -> {identificador}") """

""" ej 4 """
""" a = int(input("ingresa un numero: "))
b = int(input("ingresa otro numero: "))

print(f"alguno de ellos es multiplo del otro? {a % b == 0 or b % a == 0}")
print(f"el primero es multiplo del segundo? {Functions.mult(a, b)}") """
