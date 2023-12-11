
# test_bucles_while.py

from _07bucles_while import encontrar_primer_negativo, cuenta_regresiva, sumar_hasta_limite

def test_encontrar_primer_negativo():
    assert encontrar_primer_negativo([3, 5, -1, 7]) == -1
    assert encontrar_primer_negativo([1, 2, 3]) == None

def test_cuenta_regresiva():
    assert cuenta_regresiva(5) == [5, 4, 3, 2, 1, 0]

def test_sumar_hasta_limite():
    assert sumar_hasta_limite(12) == 10  # 1+2+3=6, el siguiente número 4 sobrepasa el límite
    assert sumar_hasta_limite(3) == 3  # 1+2=3, el siguiente número 3 sobrepasa el límite
