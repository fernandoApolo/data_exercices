from python.src.clases.Persona_POO import Persona_POO
from python.src.clases.Persona_Funcional import Persona_Funcional

Emad:Persona_POO= Persona_POO(nombre="Emad",edad=29,profesion="maquinista")
print(f"Hola, mi nombre es {Emad.get_mi_nombre()}")
print(f"Hola, mi edad es {Emad.get_mi_edad()}")
print(f"Hola, mi curro es {Emad.get_mi_profesion()}")

print(f"{Emad.get_mi_nombre()} va a cambiar de profesión")
Emad.set_mi_profesion(profesion_en_funcion="Parado")
print(f"La profesión de {Emad.get_mi_nombre()} es {Emad.get_mi_profesion()}")
print("******************************************************************")

Emad:Persona_Funcional= Persona_Funcional(nombre="Emad",
                                          edad=29,
                                          profesion="maquinista")
print(f"Hola, mi nombre es {Emad.get_mi_nombre()}")
print(f"Hola, mi edad es {Emad.get_mi_edad()}")
print(f"Hola, mi curro es {Emad.get_mi_profesion()}")

print(f"{Emad.get_mi_nombre()} va a cambiar de profesión")
Emad:Persona_Funcional= Emad.set_mi_profesion(profesion_en_funcion="Parado")
print(f"La profesión de {Emad.get_mi_nombre()} es {Emad.get_mi_profesion()}")


