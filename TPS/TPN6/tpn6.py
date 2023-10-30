""" ej 1, 2, 3, 4"""
number_list = []
while True:
  number = int(input("Ingresa un numero(0 para salir): "))
  if number == 0:
    break
  number_list.append(number)
print(number_list)

delete = int(input("ahora ingrese un numero a eliminar: "))
if delete in number_list:
  number_list.remove(delete)
  print("eliminado")
else:
  print("no se encontro el numero a eliminar")
print(number_list)

total = 0;
for number in number_list:
  total += number
print(f"El total de la suma de todos los numeros del array es: {total}")

ocurrencias = {}
tuple_list = []
for numero in number_list:
    if numero in ocurrencias:
        ocurrencias[numero] += 1
    else:
        ocurrencias[numero] = 1

for item in ocurrencias.items():
  tuple_list.append(item)

# Imprimir la lista de tuplas
print(tuple_list)