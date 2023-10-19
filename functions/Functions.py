import random


def count_digits(number, extNum=0, sumDigit=0):
    while number != 0:
        extNum = number % 10
        number //= 10
        sumDigit += extNum
    return sumDigit


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

#funcion para verificar si una letra ya se encuentra o no en la palabra actual
def found_letters(letter, current_word):
    if letter in current_word:
        return True
    else:
        return False
