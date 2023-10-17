# input para ingresar el nombre y capitalize para darle mayus a la primer letra
name = input("Ingresa tu nombre: ").capitalize()
print(f"Bienvenido {name}, elija una de las siguientes opciones: ")
# bucle while siempre en true para que siempre se repita salvo que elija las opciones existentes para luego de la ejecucion finalizar con un break
while True:
    # se solicita que ingrese la opcion que desea, para luego abrir una estructura condicional para verificar si las opciones existen
    option = input("Juego de numeros(1), Juego de palabras(2): ")
    if option == "1":
        # declaro variables necesarias
        numbers = []
        total = 0
        counter = 0
        even_number = 0
        # bucle while true para que el usuario ingrese cuantos numeros quiera y al ingresar 0 romper bucle con break
        while True:
            num = float(input(
                f"{name}, ingresa un numero. ingresa 0 para finalizar: "))
            if num == 0:
                break
            else:
                # en caso de que el numero sea mayor a 0, se va almacenando la suma total de los numeros ingresados, ademas de ir contando la cantidad de numeros ingresados
                # para ir calculando en tiempo de ejecucion el promedio y a su vez el mayor numero par
                total += num
                counter += 1
                average = total/counter
                # si el numero ingresado por el usuario es mayor al valor de la variable even_number(es decir al valor anterior) y ademas es par
                # sobreescribo el valor de even_number para almacenar el mayor numero par encontrado
                if num > even_number and num % 2 == 0:
                    even_number = num
        # finalmente muestro los resultados, y uso un formateo en el caso del promedio para mostrar hasta 2 decimales
        print(f"{name}, el promedio de los numeros ingresados es: {average:.2f}")
        if even_number == 0:
            print(f"{name}, no se ingreso ningun numero par")
        else:
            print(f"{name}, el mayor numero par es: {even_number}")
        # se rompe el bucle principal al finalizar
        break
    elif option == "2":
        # se solicita una palabra, se pasa a lower case y se remplazan los espacios
        word = input(f"{name}, ingrese una frase: ").lower().replace(' ', '')
        # almaceno las vocales
        vowels = ['a', 'e', 'i', 'o', 'u']
        # con word.count itero la palabra por cada vocal en vowels, para ir contando todas las ocurrencias y luego sumarlas
        count = sum([word.count(vowel) for vowel in vowels])
        # muestro los resultados
        print(
            f"{name}, la cantidad de vocales que posee la palabra: {word}, es: {count}")
        # finaliza la ejecucion
        break
    else:
        # en caso de ingresar opciones invalidas
        print(f"{name}, ingresaste una opcion invalida")
