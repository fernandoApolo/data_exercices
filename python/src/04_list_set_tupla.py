lista_numeros:[int]=[1,2,3,4,5,6,7]
lista_cuadrado:[int]=[]

for elemento in lista_numeros:
    if elemento%2==0:
        print(f"El número {elemento} es parr!")
        lista_cuadrado.append(elemento**2)
    else:
        print(f"El número {elemento} es imparr!")
print(f"Voy por el número {elemento}")

print(f"La lista de cuadrados es {lista_cuadrado}")

nueva_lista=[elemento**2 for elemento in lista_numeros if elemento%2==0]
print(nueva_lista)

lista_de_lista =[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4,4]]

nueva_lista=[elemento**3 for lista in lista_de_lista for elemento in lista if elemento**2%2==0]

print(nueva_lista)