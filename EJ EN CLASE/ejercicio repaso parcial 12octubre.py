import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos = 0
print("Bienvenido al juego de adivina el numero secreto entre 0 y 50, tienes 5 intentos.")

while intentos < 5:
    intentos += 1
    print(f"Intento nro {intentos}")
    intento = int(
        input("ingresa un numero: "))

    if intento == numero_secreto:
        print(f"Felicidades, adivinaste el número en {intentos} intentos")
        break
    elif intentos == 5:
        print(
            f"Te quedaste sin intentos, el numero secreto era: {numero_secreto}.")
        break
    elif intento < numero_secreto:
        print("El número es mayor. Sigue intentando")
    else:
        print("El número es menor. Sigue intentando")
