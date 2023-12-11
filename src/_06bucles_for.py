"""
Ejercicios de bucles for.
"""

def suma_numeros(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma

def producto_numeros(lista_numeros):
    producto = 1
    for numero in lista_numeros:
        producto *= numero
    return producto

def contar_ocurrencias(lista_items, item_buscado):
    contador = 0
    for item in lista_items:
        if item == item_buscado:
            contador += 1
    return contador

def crear_lista_cuadrados(n):
    lista_cuadrados = []
    for i in range(1, n + 1):
        lista_cuadrados.append(i ** 2)
    return lista_cuadrados