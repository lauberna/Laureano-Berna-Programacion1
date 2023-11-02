from functions import is_mutant
def main():
  print("Ingresa las cadenas de ADN (ATGC):")
  print("Cada secuencia contiene 6 caracteres, un total de 6 secuencias")
  dna = []
  #bucle de rango 6, para ingresar las se secuencias de adn
  for i in range(6):
      print("Secuencia nro", i + 1, ":")
      while True:
          sequence = input().upper()
          #Verifico si cada caracter de sequence se encuentra en la scuencia de ATGC para verificar si es una secuencia valida
          if all(character in "ATGC" for character in sequence):
            #Si es valida la agrego al array de dna
              dna.append(sequence)
              break
          else:
              print("Secuencia incorrecta")

  #Llamo a la funcion para verificar si es mutante
  print("---------------")
  print("Es mutante?", is_mutant(dna))
  print("---------------")
main()