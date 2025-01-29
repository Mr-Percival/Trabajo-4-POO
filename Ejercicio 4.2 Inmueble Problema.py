class Inmueble:
    def __init__(self, identificador_inmobiliario, area, direccion):
        self._identificador_inmobiliario = identificador_inmobiliario
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Área = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta}")


class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._numero_habitaciones = numero_habitaciones
        self._numero_banos = numero_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_banos}")


class Casa(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self._numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")


class CasaUrbana(Casa):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        super().imprimir()


class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos, valor_administracion, tiene_piscina, tiene_campos_deportivos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self._valor_administracion = valor_administracion
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion}")
        print(f"Tiene piscina? = {self._tiene_piscina}")
        print(f"Tiene campos deportivos? = {self._tiene_campos_deportivos}")


class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        super().imprimir()


class CasaRural(Casa):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos, distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia la cabecera municipal = {self._distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros")


class Local(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self._tipo_local}")


class Oficina(Local):
    valor_area = 3500000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, es_gobierno):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self._es_gobierno}")


class LocalComercial(Local):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, centro_comercial):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self._centro_comercial}")


class Apartamento(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)

    def imprimir(self):
        super().imprimir()


class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion):
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()


class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, valor_administracion):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self._valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion}")


# Prueba de las clases

def main():
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcular_precio_venta(ApartamentoFamiliar.valor_area)
    apto1.imprimir()

    print("Datos apartaestudio")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    aptestudio1.calcular_precio_venta(Apartaestudio.valor_area)
    aptestudio1.imprimir()

if __name__ == "__main__":
    main()
