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

# Función principal
def principal():
    r1 = RecetaVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    r2 = RecetaNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(r1)
    Utilidades.imprimir_receta(r2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in r1.ingredientes:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in r2.ingredientes:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
