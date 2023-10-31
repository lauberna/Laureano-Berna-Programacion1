""" ej1 """
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

numero = 12345
cantidad_de_digitos = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad_de_digitos} dígitos.")

""" ej2 """
def es_potencia_de(n, b):
    if n == 1:
        return True
    if n % b != 0 or n < b:
        return False
    return es_potencia_de(n // b, b)

n = 64
b = 4
resultado = es_potencia_de(n, b)
if resultado:
    print(f"{n} es una potencia de {b}.")
else:
    print(f"{n} no es una potencia de {b}.")

""" ej3 """
def encontrar_maximo(lista):
    if not lista:
        return None
  
    if len(lista) == 1:
        return lista[0]
    mitad = len(lista) // 2
    max_izquierda = encontrar_maximo(lista[:mitad])
    max_derecha = encontrar_maximo(lista[mitad:])
    
    return max(max_izquierda, max_derecha)

mi_lista = [3, 7, 2, 8, 5, 1, 9]
resultado = encontrar_maximo(mi_lista)
print("El elemento más grande de la lista es:", resultado)
