"""1
a)valido
b)no valido, comienza con numero
c)valido pero no es buena practica
d)no valido, comienza con caracter especial
e)valido
f)no valido, palabra reservada
g)no valido, caracteres especiales
h) no valido, palabra reservada
i) vaido
j)valido
k)no valido, caracter eespecial
l)no valido, caracter especial
m)invalido, comienza con numeros
n)invalido, palabra reservada
o)invalido, caracter especial
p)invalido, caracter especial
q)valido
r)valido
s)valido
t)invalido, ñ
u)valido
v)invalido, caracter especial
w)invalido, comienza con numero
x)invalido, carateres especiales
 """

"""2
a) 30
b) 30
c) 25
d) 8
e) 13
f)8
 """

"""3
a)int
b)float
c)int
d)int
e)str
f)str
g)str
h)int
i)int
j)float
k)float
l)str
m)complex
n)bool
o)bool
 """

"""4
a)valido
b)valido
c)invalido
d)es valido, pero en este caso da error pq la palabra hola tiene 4  caracteres y no existe  la posicion 4 en la cadena
e)inivalido
f)valido
g)valido
h)valido
i)invalido
j)invalido
k)invalido
l)invalido, para realizar comparaciones usamos ==
 """

"""5
"""
vint = 1
vfloat = 2.4
vcomplex = 3+4j
vstring = "hola"
vlist = [1, 2, 3, 4]
vtuple = (1, 2, 3, 4)
vdict = {
    "abc": 1,
    "def": 2,
}
vnull = None

"""6
a) a
b) .
c) Caminant
d) Cnn ,ay,as nra.
"""

print("ejercio 7")
frase = "Caminante, no hay camino, se hace camino al andar."
print("a) ", frase[::-1])
print("b) ", frase[29:33])

print("ejercio 8")
print("lucas mauricio barros".title())
print("El qUe No arRiesGa, nO gANa".lower())
print("El qUe No arRiesGa, nO gANa".upper())


"""9 
a) (b/2)-4*a*c
b)3*x*y-5*x+12*x-17
c)(b+d)/(c+4)
d)(x*y)/y+2
e)1/y + (3*x)/z + 1
f)1/(y+3)+x/y+1
g)a**2 + b**2
h)(a+b)**2
i)b**(1/3)+34
j)(x/y)*(z+w)*3.14
k)(x+y)/u+w/b
 """

"""10 - he remplazado los simolos de potencia por ^ y de raiz por la palara raiz, para poder escribirlos aca.
a) x = (-b + raíz(b^2 - 4ac)) / (2a)
b) (x^2 + y^2) / (2^2)
c) 4x^2 - 2x + 7
d) raíz(b^2) - 4ac
e) (a - b)^2 + (c - d)^3
f) (x + y) / y - (3x / 5)
g) raíz(a^2 + b^2) = c^(1/3)
h) (3x^2 / 3x^3) / raíz(4v + 6)
 """

print("ejercicio 11")
calculo = 5+2*(5-(6/2))+(7-(-6))/(4+4)
print("el resultado es: " + str(calculo))

""" 12 """
# a)
resultado_a = 5 + 3

# b)
resultado_b = (4 + 7 + 9) / 3

# c)
base = 8
altura = 5
area = base * altura

# d)
numero = 10
es_par = numero % 2 == 0

# e)
resultado_e = 16 * 2

# f)
resultado_f = 6 * (8 - 3)

# g)
resultado_g = (2 * 6) - (4 + 3)

# h
numero = 12
es_multiplo_de_2_y_3 = numero % 2 == 0 and numero % 3 == 0

# i)
precio = 25
cumple_condicion = precio >= 15 and precio < 90

# j
N = 20
N += 12

# k
N = 30
N -= 5

# l)
N = 10
N *= 3

# m)
N = 50
N /= 2

"""13
a) False
b) True
c) False
d) False, da error debido a q x no esta declarado, pero de estar declarada seria true
e) false
f) True
g) True
h) True, pero da error igual debido a q x no esta declarada
i) True, pero da error porque edad no existe
 """

"""14
a) se mostrara 6
b) se mostrara 3
c) se mostrara 25
d) se mostrara 1
 """

print("ejercicio 15")
# a) en la posicion 3 esta el color amarillo
# b) el color rojo esta en la posicion 0 y el rosa en la 7
# c)
listacolores = ["tres", "dos", "cinco", "cuatro", "uno"]

# d)
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón',
           'lila', 'negro', 'rosa', 'blanco', 'naranja')
print("d) " + colores[2])

# e)
numeros = (10, 1, 5, 11)
print("e) ", numeros[0] + numeros[2]+numeros[3]-numeros[1])

# f)
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
print("f) ", len(diccionario))
print("g) ", diccionario["c"])

print("ejercicio 16")
# a)
num1 = input("ingresa un numero: ")
num2 = input("ingrese otro numero: ")
print("a) ", int(num1)+int(num2))
# b)
edad = input("ingresa tu edad: ")
print("b) ", 100-int(edad))

print("ejercicio 17")
# a)
numero = 10
resultado = "Par" if numero % 2 == 0 else "Impar"
print("a) ", resultado)
# b)
numero = -5
valor_absoluto = numero if numero >= 0 else -numero
print("b) ", valor_absoluto)
# c)
numero1 = 15
numero2 = 20
mayor = numero1 if numero1 > numero2 else numero2
print("c) El número mayor es:", mayor)
