# test_listas.py

from src._04listas import agregar_elemento, eliminar_elemento, obtener_elemento, concatenar_listas

def test_agregar_elemento():
    lista = [1, 2, 3]
    assert agregar_elemento(lista, 4) == [1, 2, 3, 4]

def test_eliminar_elemento():
    lista = [1, 2, 3, 2]
    assert eliminar_elemento(lista, 2) == [1, 3, 2]
    assert eliminar_elemento(lista, 5) == [1, 3, 2]  # No elimina nada porque 5 no está en la lista

def test_obtener_elemento():
    lista = [1, 2, 3]
    assert obtener_elemento(lista, 1) == 2
    assert obtener_elemento(lista, 3) == None  # Índice fuera de rango

def test_concatenar_listas():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    assert concatenar_listas(lista1, lista2) == [1, 2, 3, 4, 5, 6]
