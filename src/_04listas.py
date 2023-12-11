# listas.py

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None

def concatenar_listas(lista1, lista2):
    return lista1 + lista2