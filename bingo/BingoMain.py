import random
import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")
import Functions

def main():
    while True:
        carton = [[0]*5 for _ in range(5)]
        for i in range(len(carton)):
            for j in range(len(carton)):
                while True:
                    try:
                        num = int(input("Ingrese un numero entre 1-75: "))
                        if not Functions.validar(num, carton):
                            print("numero agregado.")
                            carton[i][j] = num
                            break
                        else:
                            print("el numero ya ha sido ingresado previamente")
                    except ValueError as error:
                        print(f"Ocurrio un error: {error}")
                        continue
        print("-----TABLERO-----")
        Functions.show(carton)
        print("Empieza el juego, se va a sacar un total de 50 numeros!")
        win = False
        for k in range(1, 51):
            ran_n = Functions.random_num()
            print(f"numero {k} = {ran_n} ")
            if Functions.validar(ran_n, carton):
                carton = Functions.replace(carton, ran_n)
                Functions.show(carton)
                if Functions.win_line(carton) in range(0,5):
                    win = True
                    print(f"Ganaste por linea horizontal (linea:{Functions.win_line(carton)+1})")
                    break
                elif Functions.win_main_diagonal(carton):
                    win = True
                    print(f"Ganaste por diagonal principal")
                    break
                elif Functions.win_col(carton) in range(0,5):
                    win = True
                    print(f"Ganaste por linea vertical (linea:{Functions.win_col(carton)+1})")
                    break
                elif Functions.win_second_diagonal(carton):
                    win = True
                    print(f"Ganaste por diagonal secundaria")
                    break
            else:
                continue
        if not win:
            print("Lo siento, no has ganado!")
        opcion = input("Desea jugar otra vez? s/n: ").lower()
        if opcion == 'n':
            break
main()
