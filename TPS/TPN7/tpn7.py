""" 1 """
list_in = [62,3,5,2,7,10,22,1]

for i in range(len(list_in)):
  for j in range(len(list_in)-1):
    if(list_in[j] > list_in[j+1]):
      temp = list_in[j]
      list_in[j] = list_in[j+1]
      list_in[j+1] = temp
print(list_in)

""" 3 """

dict_list = [
    {
        "titulo": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año_publicacion": 1925
    },
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "año_publicacion": 1949
    },
    {
        "titulo": "Matar a un ruiseñor",
        "autor": "Harper Lee",
        "año_publicacion": 1960
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año_publicacion": 1605
    },
    {
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "año_publicacion": 1813
    },
    {
        "titulo": "Ulises",
        "autor": "James Joyce",
        "año_publicacion": 1922
    },
    {
        "titulo": "Moby-Dick",
        "autor": "Herman Melville",
        "año_publicacion": 1851
    },
    {
        "titulo": "Los juegos del hambre",
        "autor": "Suzanne Collins",
        "año_publicacion": 2008
    },
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año_publicacion": 1997
    }
]

for i in range(len(dict_list)):
  for j in range(len(dict_list)-1):
    if(dict_list[j]["año_publicacion"] > dict_list[j+1]["año_publicacion"]):
      temp = dict_list[j]
      dict_list[j] = dict_list[j+1]
      dict_list[j+1] = temp
print(dict_list)



""" 5 """
list_in = [62,3,5,2,7,10,22,1]

for i in range(len(list_in)):
  for j in range(len(list_in)-1):
    if(list_in[j] < list_in[j+1]):
      temp = list_in[j]
      list_in[j] = list_in[j+1]
      list_in[j+1] = temp
print(list_in)


""" 4 """
cadenas = ["manzana", "banana", "pera", "uva", "kiwi", "naranja", "fresa"]
for i in range(len(cadenas)):
    for j in range(len(cadenas)-1):
        if len(cadenas[j]) > len(cadenas[j+1]):
            cadenas[j], cadenas[j+1] = cadenas[j+1], cadenas[j]
print("Cadenas ordenadas por longitud:")
for cadena in cadenas:
    print(cadena)