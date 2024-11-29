entero: int = 1
string: str = "hola que tal soy un string"
boolean: bool = True
float_var: float = 5.2

print(type(entero))
print(type(string))
print(type(boolean))
print(type(float_var))

# aplicamos tipado dinamico para transformar
# el booleano en string y ademas guardarlo
# en su propia variable
boolean: bool = str(boolean)
print(type(boolean))
