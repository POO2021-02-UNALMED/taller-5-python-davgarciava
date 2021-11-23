from gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio

class Animal:
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1
        
    def movimiento():
        return "desplazarse"
	
    @classmethod
    def totalPorTipo():
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios()
        
    def toString(self):
        if self._zona != None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
            
    def getNombre(self):
        return self._nombre
        
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getEdad(self):
        return self._edad
        
    def setEdad(self, edad):
        self._edad = edad
        
    def getHabitat(self):
        return self._habitat
        
    def setHabitat(self, habitat):
        self._habitat = habitat
        
    def getGenero(self):
        return self._genero
        
    def setGenero(self, genero):
        self._genero = genero
        
    def getZona(self):
        return self._zona
        
    def setZona(self, zona):
        self._zona = zona
	
    @classmethod
    def getTotalAnimales(cls):
        return cls.totalAnimales