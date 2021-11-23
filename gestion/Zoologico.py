class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        
    def agregarZonas(self, nuevaZona):
        nuevaZona.setZoo(self)
        self._zonas.append(nuevaZona)
        
    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for i in self._zonas:
            totalAnimales += i.cantidadAnimales()
        return totalAnimales