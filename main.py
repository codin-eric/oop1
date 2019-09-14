"""Video 1

Clases y objetos
"""


class Perro:
    def __init__(self, nombre, color, tamaño):
        self.nombre = nombre
        self.color = color
        self.tamaño = tamaño

    def dormir(self):
        print("Estoy durmiendo")

    def hablar(self):
        print(
            f"Hola mi nombre es{self.nombre}. Tengo el pelo {self.color} y soy de tamaño {self.tamaño}"
        )

    def dar_pata(self):
        print("Toma mi patita")


p1 = Perro("Framir", "Amarillo y negro", "mediano")

p1.hablar()

p2 = Perro("Tai", "negro", "mediano")

p2.hablar()
