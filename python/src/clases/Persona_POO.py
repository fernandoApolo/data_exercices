class Persona_POO():
    def __init__(self, nombre: str, edad: int, profesion: str):
        self.mi_nombre = nombre
        self.mi_edad = edad
        self.mi_profesion = profesion

    def get_mi_nombre(self) -> str:
        return self.mi_nombre

    def set_mi_nombre(self, nombre_en_funcion: str) -> None:
        self.mi_nombre = nombre_en_funcion

    def get_mi_edad(self) -> int:
        return self.mi_edad

    def set_mi_edad(self, edad_en_funcion: int) -> None:
        self.mi_edad = edad_en_funcion

    def get_mi_profesion(self) -> str:
        return self.mi_profesion

    def set_mi_profesion(self, profesion_en_funcion: str) -> None:
        self.mi_profesion = profesion_en_funcion


