numero: int = float(input("Introduce un número\n"))

if numero%2==0:
    print(F"EL NÚMERO {numero} ES PAR!!")
else:
    print(f"El número {numero} es impar")

palabra = input("Introduce una palabra\n")

if palabra.startswith("A"):
    print(f"La palabra {palabra} empieza por la letra A en mayuuusculas ")
elif palabra.startswith("a"):
    print(f"La palabra {palabra} empieza por la letra a en mayuuusculas ")
else:
    print("La palabra no tengo condicion de naa")

match list(palabra):
    #case x if x.startswith("A") and x.endswith("o"):
    #    print(f"La palabra empieza por la letra A y acaba por la o")
    #case "A":
     #   print("La palabra empieza por la letra A")
       case ["A",*tail]:
        print(f"La palabra empieza por la letra A y termina en {tail}")
       case "a":
        print("La palabra empieza por la letra {}")
       case[a , b, c, d, *tail]:
        print(f"La palabra empieza por la letra {a} y termina en {'-'.join(tail)}")
       case _:
        print("No tengo condii")