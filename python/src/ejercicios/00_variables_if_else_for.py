'''
"""
5)Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el precio habitual
 de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
"""
print("**********EJERCICIO 5**********")
bvqnsdd=int(input("Ingresa el numero de barras vendidas que no son del día\n"))
precio_pan_normal:float=3.49
descuento:float = 0.60
precio_con_descuento:float = precio_pan_normal*0.60

print(f"El precio habitual del pan que has comprado es de {precio_pan_normal*bvqnsdd},"
      f" el descuento que se te aplica porque el pan esté chungo es de {descuento*bvqnsdd},"
      f" y el precio total de lo que tienes que pagar es {precio_con_descuento*bvqnsdd} ")

"""
6)Escriba un programa que pida dos números enteros y que calcule su división, escribiendo 
si la división es exacta o no.
"""
print("********** EJERCICIO 6**********")
numero_1= int(input("Introduce el primer número\n"))
numero_2: int = int(input("Introduce el segundo número\n "))
resultado: float = numero_1/numero_2
print(resultado)
if numero_1%numero_2==0:
      print("Esta división es exacta!")
else :  print("Esta división no es exacta!!")

"""
7)Escriba un programa que pida dos números y que conteste cuál 
es el menor y cuál el mayor o que escriba que son iguales
"""
print("********** EJERCICIO 7**********")
numero_1:int = int(input("Introduce el primer número "))
numero_2: int = int(input("Introduce el segundo número "))
if numero_1<numero_2:
      print(f"El número {numero_1} es menor que el número {numero_2}.")
elif numero_1>numero_2:
      print(f"El número {numero_1} es mayor que el número {numero_2}.")
else:
      print("Son numeros iguales supapa")

"""
8)Escriba un programa que pida el año actual y un año cualquiera 
y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
"""
print("********** EJERCICIO 8*********")
año_actual:int = int(input("Introduce el año actual "))
año_dicho: int = int(input("Introduce el año a calcular "))
if año_actual>año_dicho:
      años_a_mostrar=año_actual-año_dicho
      print(f"Han pasado {años_a_mostrar} años vale")
elif año_dicho>año_actual:
      años_a_mostrar=año_dicho-año_actual
      print(f"Quedan {años_a_mostrar} años para ese año")
else:
      print("No queda na de na")

"""
9)Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla si es mayor de edad o no.
"""
print("********** EJERCICIO 9 **********")

edad:int = int(input("Introduce tu edad y te diré si eres mayor de edad o no\n"))
if edad>17:
      print("Eres mayor de edad")
else:
      print("No eres mayor tronco")
"""
10) Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
  por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
"""

print("********** EJERCICIO 10 **********")

contraseña = input("Introduce una contraseña\n")
print("¿Qué jodida contraseña has pouesto macho?")
contraseña_preguntada = input()
contraseña.islower()
contraseña_preguntada.islower()
if contraseña_preguntada==contraseña:
      print(f"La contraseña que has metido era la de {contraseña}.")

"""
11)Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
"""
nunmero = int(input("Introduce un número entero y te diré si es par o impar"))

match nunmero % 2:
    case 0:
        print("El número es par")
    case 1:
        print("El número es impaar!!")

"""
12)Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
 o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
 ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no
"""
edad:int =int(input("Me podrías decir cuál es tu edad??\n"))
ingresos_mensuales:int =int(input("y tu sueldo mensual??\n"))

match (edad,ingresos_mensuales):
    case (a,b) if a>16 and b>=1000:
        print(f"Usted si que debe tributar, dado que tiene {edad} y gana al mes {ingresos_mensuales}")
    case (c,d) if c<=16 and d>=1000:
        print(f"Usted no debería tributar, dado que tiene {edad} y gana al mes {ingresos_mensuales}")
    case (e,f) if e>16 and f<1000:
        print(f"Usted si que debe tributar por su edad de {edad} años, pero gana al mes {ingresos_mensuales}, y eso no es na")
    case (g,h) if g>16 and h<1000:
        print(f"Usted por edad si que debería tributar, dado que tiene {edad}, pero gana al mes {ingresos_mensuales} y no ")

"""
13)Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""
edad_preguntada: int = int(input("Dime cuantos años tienes para decirte la pasta a pagar\n"))

match edad_preguntada:
    case a if a < 4:
        print(f"El precio de la entrada debe ser gratuito dado que tienes {edad_preguntada} años")
    case b if b > 3 and b < 19:
        print(f"El precio de la entrada debe ser de 5€ dado que tienes {edad_preguntada} años")
    case c if c > 18:
        print(f"El precio de la entrada debe ser de 10€ dado que tienes {edad_preguntada} años")

"""
14)Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
palabra_pedida : str = input("Escribe una palabra y te la imprimo 10 veces\n")
contador:int=1

while contador<11:
    print(f"La palabra {palabra_pedida} se está imprimiendo por {contador} vez")
    contador=contador+1

"""
15)Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
edad:int = int(input("Quiero que me digas tu edad y ya verás klk"))
contador:int= 1
while contador<=edad:
    print(f"Han pasado {contador} años ")
    contador=contador+1


"""
16)Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 todos los números impares desde 1 hasta ese número separados por comas.
"""
numero_pedido: int = int(input("Introduce un número positivo y mostraré los impares desde el 1 hasta ese número\n"))
contador: int = 0
while contador <= numero_pedido:
    if contador % 2 != 0:
        print(f"El número {contador} es impar")
    contador = contador + 1
'''
"""
17)Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas
"""
respuesta : int = int(input("Introduce un número entero y haré la cuenta atrás hasta el 0"))
lista_numeros : dict = input("Introduce un número entero y haré la cuenta atrás hasta el 0")
if respuesta<0:
    print("INTRODUCE UN NÚMERO ")
"""
18)Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
 rectángulo como el de más abajo, de altura el número introducido.
"""

"""
19)Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
"""
contraseña: str = input("Introduce una contraseña y después la vas a tener que poner tal cual\n")
contraseña_pedida:str = input("Mete la contraseña aver si es tal cual\n")
while contraseña!=contraseña_pedida:
    contraseña_pedida=input("Introduce la contraseña bien que sino na\n")
print("Eso es, contraseña correcta")
"""
20)Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no
"""
numero_pedido : int = int(input("Introduce un número y te digo si es primo o no"))
if numero_pedido%numero_pedido==0 and numero_pedido%2!=0
"""
21)Escribir un programa que pida al usuario una palabra y luego muestre
 por pantalla una a una las letras de la palabra introducida empezando por la última
"""

"""
22)Escribir un programa en el que se pregunte al usuario por una frase 
y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase
"""

"""
23)Escribir un programa que muestre el eco de todo lo que
 el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
