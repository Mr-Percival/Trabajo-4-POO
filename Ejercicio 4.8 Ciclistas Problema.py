class Ciclista:
    def __init__(self, identificador, nombre):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado = 0

    def get_identificador(self):
        return self.__identificador

    def set_identificador(self, identificador):
        self.__identificador = identificador

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tiempo_acumulado(self):
        return self.__tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo_acumulado):
        self.__tiempo_acumulado = tiempo_acumulado

    def imprimir(self):
        print(f"Identificador = {self.__identificador}")
        print(f"Nombre = {self.__nombre}")
        print(f"Tiempo Acumulado = {self.__tiempo_acumulado}")

    def imprimir_tipo(self):
        raise NotImplementedError("Subclasses should implement this method")


class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self.__velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.__velocidad_maxima = velocidad_maxima

    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima = {self.__velocidad_maxima}")

    def imprimir_tipo(self):
        return "Es un contrarrelojista"


class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa

    def get_aceleracion_promedio(self):
        return self.__aceleracion_promedio

    def set_aceleracion_promedio(self, aceleracion_promedio):
        self.__aceleracion_promedio = aceleracion_promedio

    def get_grado_rampa(self):
        return self.__grado_rampa

    def set_grado_rampa(self, grado_rampa):
        self.__grado_rampa = grado_rampa

    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio = {self.__aceleracion_promedio}")
        print(f"Grado de rampa = {self.__grado_rampa}")

    def imprimir_tipo(self):
        return "Es un escalador"


class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self):
        return self.__potencia_promedio

    def set_potencia_promedio(self, potencia_promedio):
        self.__potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self):
        return self.__velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio):
        self.__velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio = {self.__potencia_promedio}")
        print(f"Velocidad promedio = {self.__velocidad_promedio}")

    def imprimir_tipo(self):
        return "Es un velocista"


class Equipo:
    def __init__(self, nombre, pais):
        self.__nombre = nombre
        self.__pais = pais
        self.__total_tiempo = 0
        self.__lista_ciclistas = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_pais(self):
        return self.__pais

    def set_pais(self, pais):
        self.__pais = pais

    def anadir_ciclista(self, ciclista):
        self.__lista_ciclistas.append(ciclista)

    def listar_equipo(self):
        for ciclista in self.__lista_ciclistas:
            print(ciclista.get_nombre())

    def buscar_ciclista(self, nombre_ciclista):
        for ciclista in self.__lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                print(ciclista.get_nombre())
                return
        print(f"Ciclista {nombre_ciclista} no encontrado")

    def calcular_total_tiempo(self):
        self.__total_tiempo = sum(ciclista.get_tiempo_acumulado() for ciclista in self.__lista_ciclistas)

    def imprimir(self):
        print(f"Nombre del equipo = {self.__nombre}")
        print(f"País = {self.__pais}")
        print(f"Total tiempo del equipo = {self.__total_tiempo}")


# Prueba de las clases

def main():
    equipo = Equipo("Team Sky", "Reino Unido")
    ciclista1 = Velocista(1, "Chris Froome", 400, 45)
    ciclista2 = Escalador(2, "Nairo Quintana", 2.5, 8)
    ciclista3 = Contrarrelojista(3, "Tom Dumoulin", 50)

    equipo.anadir_ciclista(ciclista1)
    equipo.anadir_ciclista(ciclista2)
    equipo.anadir_ciclista(ciclista3)

    equipo.listar_equipo()
    equipo.buscar_ciclista("Nairo Quintana")

    equipo.calcular_total_tiempo()
    equipo.imprimir()

if __name__ == "__main__":
    main()
