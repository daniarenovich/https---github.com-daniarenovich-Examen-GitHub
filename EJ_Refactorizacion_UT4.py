from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos


# Clase para recetas vegetarianas
class RecetaVegetariana(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)


# Clase para recetas no vegetarianas
class RecetaNoVegetariana(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)


# Clase con utilidades del restaurante
class Utilidades:

    def mostrar(receta):
            print(f"Receta: {receta.nombre}")
            print("Ingredientes:")
            for ing in receta.ingredientes:
                print(f"- {ing}")
            print("Pasos:")
            for paso in receta.pasos:
                print(f"{paso}")

    def crear_receta():
        nombre1 = input("Dime el nombre de la receta: ")
        ingredientes1 = []

        print("Introduce los ingredientes, escribe fin para terminar.")
        while True:
            ing = input(" ")
            if ing.lower() == "fin":
                break
            ingredientes1.append(ing)
        pasos1 = []
        print("Introduce los pasos, escribe fin para terminar: ")
        while True:
            paso = input (" ")
            if paso.lower() == "fin":
                break
            pasos1.append(paso)
        return nombre1, ingredientes1, pasos1

# Función principal
def principal():
    pass

# Ejecutar el programa
if __name__ == "__main__":
    principal()
