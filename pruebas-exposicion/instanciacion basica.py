# 1. Definimos una clase
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# 2. Instanciamos la clase
persona1 = Persona("Willian")

# 3. Usamos el objeto creado
print(persona1.nombre)
# 4. Usamos metodo de clase
persona1.saludar()

# --------------------------------------------

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# Instanciación
mi_cuenta = CuentaBancaria("Ana", 1000)

# --------------------------------------------
# Encapsulamiento Python
# class Dado:
#     def __init__(self):
#         self.__cara = 1

#     @property
#     def cara(self):
#         return self.__cara

#     @cara.setter
#     def cara(self, valor):
#         if 1 <= valor <= 6:
#             self.__cara = valor

# dado = Dado()
# print(dado.cara)   # Output: 1

# dado.cara = 6
# print(dado.cara)   # Output: 6


# ---------------------------------------------
# Encapsulamiento modo java
# class Dado:
#     def __init__(self):
#         self.__cara = 1

#     def getCara(self):
#         return self.__cara

#     def setCara(self, valor):
#         if 1 <= valor <= 6:
#             self.__cara = valor

# dado = Dado()
# print(dado.getCara())  # 1

# dado.setCara(6)
# print(dado.getCara())  # 6

# ---------------------------------------------
# Abstraccion
from abc import ABC, abstractmethod

class Dado(ABC):
    @abstractmethod
    def lanzar(self):
        pass


class DadoComun(Dado):
    def lanzar(self):
        print("El dado muestra una cara del 1 al 6")


dado = DadoComun()
dado.lanzar()

# Protocol
# from typing import Protocol

# class ObjetoLanzable(Protocol):
#     def lanzar(self):
#         ...