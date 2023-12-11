'''
Test para el módulo _04bucles_for.py
'''
from _06bucles_for import suma_numeros, producto_numeros, contar_ocurrencias, crear_lista_cuadrados

def test_suma_numeros():
    '''
    Test para la función suma_numeros().
    '''
    assert suma_numeros([1, 2, 3, 4, 5]) == 15
    assert suma_numeros([]) == 0

def test_producto_numeros():
    '''
    Test para la función producto_numeros().
    '''
    assert producto_numeros([1, 2, 3, 4, 5]) == 120
    assert producto_numeros([]) == 1

def test_contar_ocurrencias():
    '''
    Test para la función contar_ocurrencias().
    '''
    assert contar_ocurrencias(['a', 'b', 'c', 'b', 'b'], 'b') == 3
    assert contar_ocurrencias([1, 2, 3, 4, 5], 6) == 0

def test_crear_lista_cuadrados():
    '''
    Test para la función crear_lista_cuadrados().
    '''
    assert crear_lista_cuadrados(3) == [1, 4, 9]
    assert crear_lista_cuadrados(5) == [1, 4, 9, 16, 25]
