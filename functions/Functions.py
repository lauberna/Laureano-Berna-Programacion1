import random


def count_digits(number, extNum=0, sumDigit=0):
    while number != 0:
        extNum = number % 10
        number //= 10
        sumDigit += extNum
    return sumDigit


""" FUNCIONES AHORCADO """


def random_word(words):
    return random.choice(words)


def guessed_word(word, letter, current_word):
    # bucle para recorrer todas las posiciones de la palabra original
    for i in range(len(current_word)):
        # comparo la palabra original en la posicion i con la letra, si son iguales, la letra original se agrega al array en su debida posicion
        # utilizo un bucle para que se recorra toda la palabra para buscar tantas ocurrencias como se pueda
        if word[i].lower() == letter:
            current_word[i] = word[i]
    return current_word

# funcion para verificar si una letra ya se encuentra o no en la palabra actual


def found_letters(letter, current_word):
    if letter in current_word:
        return True
    else:
        return False


""" FUNCIONES BINGO """


def validar(num, carton):
    if num > 0 and num <= 75:
        for i in range(0, len(carton)):
            for j in range(0, len(carton)):
                if carton[i][j] == num:
                    return True
        return False
    else:
        raise ValueError("Dato ingresado incorrecto")


def replace(carton, num):
    for i in range(len(carton)):
        for j in range(len(carton)):
            if carton[i][j] == num:
                carton[i][j] = "X"
    return carton


numeros_generados = set()
def random_num():
    while True:
        numero = random.randint(1, 75)
        if numero not in numeros_generados:
            numeros_generados.add(numero)
            return numero


def show(carton):
    print("---------------------")
    for i in range(len(carton)):
        for j in range(len(carton[i])):
            print(f"{carton[i][j]:<2}", end="  ") 
        print()
    print("---------------------")


def win_line(carton):
    for i in range(len(carton)):
        line_true = 0
        for j in range(len(carton)):
            if carton[i][j] == "X":
                line_true += 1
            if line_true == 5:
                return i

def win_col(carton):
    for i in range(len(carton)):
        col_true = 0
        for j in range(len(carton)):
            if carton[j][i] == "X":
                col_true += 1
            if col_true == 5:
                return i

def win_main_diagonal(carton):
    diagonal_true = 0
    for i in range(len(carton)):
        if carton[i][i] == "X":
            diagonal_true += 1
        if diagonal_true == 5:
            return True
    return False

def win_second_diagonal(carton):
    diagonal_true = 0
    for i in range(len(carton)):
        if carton[i][len(carton) - 1 - i] == "X":
            diagonal_true += 1
        if diagonal_true == 5:
            return True
    return False



                

