import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")
import Functions



# Variables necesarias para el juego
words = ["Python", "lenguaje", "juego", "cadena", "escuela", "soledad", "programa", "alegría", "teclado", "ciencia", "Laureano Berna", "JavaScript", ]
word = Functions.random_word(words)
lives = 10

# utilizo un array para ir almacenando la palabra letra por letra, pero al principio cada letra se convierte en un _ y si la palabra tiene espacios se agrega un espacio
current_word = []
for caracter in word:
    if caracter == " ":
        current_word.append(" ")  # Mantener el espacio
    else:
        current_word.append("_")  # Reemplazar letras por guion bajo

print(current_word)

print(
    f"Bienvenido al juego del ahorcado, tienes {lives} vidas para adivinar la palara")
while True:
    # si las vidas llegan a 0 el juego se detiene
    if lives == 0:
        print("Perdiste, ya no te quedan mas vidas")
        break
    print(f"vida nro {lives}")
    # se ingresa una letra, y se verifica si esa letra ya ha sido agregada, sino, se agrega
    guessed = input("Ingrese una letra: ").lower()
    if (Functions.found_letters(guessed, current_word)):
        print("Ya has elegido esa letra")
    else:
        current_word = Functions.guessed_word(word, guessed, current_word)
        print("".join(current_word))
    # unifico el array en una cadena, y la comparo con la palabra original, si son iguales, el jugador gano
    if "".join(current_word) == word:
        print(f"Ganaste! La palabra era: {word}")
        break
    lives -= 1
