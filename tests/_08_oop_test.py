import math
from src._08_oop import Libro, Coche, CuentaBancaria, Circulo, Cuadrado


def test_libro():
    libro = Libro("1984", "George Orwell")
    assert libro.mostrar_informacion() == "Título: 1984, Autor: George Orwell"

def test_coche():
    coche = Coche("Toyota", "Corolla", "1.8L")
    assert coche.marca == "Toyota"
    assert coche.modelo == "Corolla"
    assert coche.cilindrada == "1.8L"

def test_cuenta_bancaria():
    cuenta = CuentaBancaria("Juan", 100)
    assert cuenta.depositar(50) == True
    assert cuenta.retirar(20) == True
    assert cuenta.ver_saldo() == 130

def test_circulo():
    circulo = Circulo(5)
    assert circulo.area() == math.pi * 5 ** 2

def test_cuadrado():
    cuadrado = Cuadrado(5)
    assert cuadrado.area() == 5 * 5