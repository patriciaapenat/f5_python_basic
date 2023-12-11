# test_diccionarios.py

from src._05diccionarios import agregar_par_clave_valor, eliminar_par_clave_valor, obtener_valor, combinar_diccionarios

def test_agregar_par_clave_valor():
    diccionario = {'a': 1, 'b': 2}
    assert agregar_par_clave_valor(diccionario, 'c', 3) == {'a': 1, 'b': 2, 'c': 3}

def test_eliminar_par_clave_valor():
    diccionario = {'a': 1, 'b': 2, 'c': 3}
    assert eliminar_par_clave_valor(diccionario, 'b') == {'a': 1, 'c': 3}
    assert eliminar_par_clave_valor(diccionario, 'd') == {'a': 1, 'c': 3}  # 'd' no existe en el diccionario

def test_obtener_valor():
    diccionario = {'a': 1, 'b': 2}
    assert obtener_valor(diccionario, 'a') == 1
    assert obtener_valor(diccionario, 'c') == None  # 'c' no existe en el diccionario

def test_combinar_diccionarios():
    diccionario1 = {'a': 1, 'b': 2}
    diccionario2 = {'b': 3, 'c': 4}
    assert combinar_diccionarios(diccionario1, diccionario2) == {'a': 1, 'b': 3, 'c': 4}
