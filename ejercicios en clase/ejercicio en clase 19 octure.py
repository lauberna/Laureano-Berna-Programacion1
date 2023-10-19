import Functions
import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")


total = 0
while True:
    number = int(input("Ingresa un numero: "))
    if number == 0:
        break
    print(f"La suma de los digitos es: {Functions.count_digits(number)}")
    total += number
print(
    f"La suma de los digitos de la suma de los numeros ingresados({total}) es: {Functions.count_digits(total)}")


