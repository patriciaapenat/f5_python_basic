import math


import math

# Ejercicio 1: Clase Libro
# Crea una clase `Libro` que tiene dos atributos: `titulo` y `autor`.
# Además, debe tener un método `mostrar_informacion` que imprima "Título: [titulo], Autor: [autor]"
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Ejercicio 2: Herencia
# Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
# Luego crea una clase `Coche` que herede de `Vehiculo` y añade un atributo `cilindrada`.
class Vehiculo:
    def __init__(self, marca, modelo):
        # Constructor que inicializa los atributos `marca` y `modelo`
        self.marca = marca
        self.modelo = modelo

# Clase `Coche` que hereda de `Vehiculo` y añade un atributo `cilindrada`
class Coche(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        # Llamada al constructor de la clase base `Vehiculo`
        super().__init__(marca, modelo)
        # Añade el atributo adicional `cilindrada`
        self.cilindrada = cilindrada

# Ejercicio 3: Encapsulación
# Crea una clase `CuentaBancaria` que tiene dos atributos privados: `_saldo` y `_titular`.
# Implementa métodos para depositar y retirar dinero, además de un método para ver el saldo actual.
# Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        # Constructor: inicializa la cuenta con un titular y saldo opcional
        self._titular = titular
        self._saldo = saldo
    
    def depositar(self, cantidad):
        # Método para depositar dinero en la cuenta
        self._saldo += cantidad
        return True  # Devuelve True para indicar que la operación fue exitosa
    
    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            return True  # Devuelve True para indicar que la operación fue exitosa
        else:
            print("Fondos insuficientes")
            return False  # Devuelve False para indicar que la operación no fue exitosa
    
    def ver_saldo(self):
        # Método para ver el saldo actual de la cuenta
        return self._saldo

# Ejercicio 4: Polimorfismo
# Crea una clase base `Forma` con un método `area`.
# Luego, crea dos clases derivadas, `Circulo` y `Cuadrado`, que implementen el método `area`.
class Forma:
    def area(self):
        # Método base para calcular el área (a implementar en clases derivadas)
        pass

# Clase `Circulo` que hereda de `Forma` e implementa el método `area`
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        # Método para calcular el área de un círculo
        return math.pi * self.radio**2

# Clase `Cuadrado` que hereda de `Forma` e implementa el método `area`
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        # Método para calcular el área de un cuadrado
        return self.lado**2