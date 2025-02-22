from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, sonido, alimentos, habitat, nombre_cientifico):
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat
        self.nombre_cientifico = nombre_cientifico

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    pass


class Felino(Animal):
    pass


class Perro(Canido):
    def __init__(self):
        super().__init__("Ladrido", "Carnívoro", "Doméstico", "Canis lupus familiaris")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Lobo(Canido):
    def __init__(self):
        super().__init__("Aullido", "Carnívoro", "Bosque", "Canis lupus")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Leon(Felino):
    def __init__(self):
        super().__init__("Rugido", "Carnívoro", "Praderas", "Panthera leo")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Gato(Felino):
    def __init__(self):
        super().__init__("Maullido", "Ratones", "Doméstico", "Felis silvestris catus")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


# Prueba de las clases

def main():
    animales = [Gato(), Perro(), Lobo(), Leon()]
    for animal in animales:
        print(animal.get_nombre_cientifico())
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print()

if __name__ == "__main__":
    main()
