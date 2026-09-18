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
# 4. Usamos met|odo de clase
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
# from abc import ABC, abstractmethod

# class Dado(ABC):
#     @abstractmethod
#     def lanzar(self):
#         pass


# class DadoComun(Dado):
#     def lanzar(self):
#         print("El dado muestra una cara del 1 al 6")


# dado = DadoComun()
# dado.lanzar()

# Protocol
# from typing import Protocol

# class ObjetoLanzable(Protocol):
#     def lanzar(self):
#         ...

# ---------------------------------------------
# Herencia
# class Dado:
#     def __init__(self, caras):
#         self.caras = caras

#     def lanzar(self):
#         print(f"Lanzando dado de {self.caras} caras")


# class DadoEspecial(Dado):
#     def mostrar_premio(self):
#         print("¡Ganaste un premio!")


# dado = DadoEspecial(6)

# dado.lanzar()
# dado.mostrar_premio()

# Herencia con super()
# class Dado:
#     def __init__(self, caras):
#         self.caras = caras


# class DadoEspecial(Dado):
#     def __init__(self, caras, premio):
#         super().__init__(caras)
#         self.premio = premio


# dado = DadoEspecial(6, "Premio")

# ---------------------------------------------
# Polimorfismo + method overriding
class Dado:
    def lanzar(self):
        print("Lanzando dado")

class DadoComun(Dado):
    def lanzar(self):  # sobrescribe
        print("Dado común: 1 al 6")

class DadoEspecial(Dado):
    def lanzar(self):  # sobrescribe
        print("Dado especial: número + premio")


for dado in [DadoComun(), DadoEspecial()]:
    dado.lanzar()
