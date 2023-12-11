def encontrar_primer_negativo(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return numero
    return None

def cuenta_regresiva(n):
    cuenta_regresiva_lista = []
    while n >= 0:
        cuenta_regresiva_lista.append(n)
        n -= 1
    return cuenta_regresiva_lista

def sumar_hasta_limite(limite):
    suma_total = 0
    contador = 0
    while suma_total + contador <= limite:
        suma_total += contador
        contador += 1
    return suma_total