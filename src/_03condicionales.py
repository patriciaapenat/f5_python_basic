# condicionales.py

# Escribe una función que tome dos números y devuelva el mayor de ellos.
def mayor_de_dos_numeros(a, b):
    if a > b:
        return a
    else:
        return b

# Crea una función que determine si un número es par o no.
def es_numero_par(num):
    return num % 2 == 0

# Desarrolla una función que, dada una calificación numérica, devuelva 'Aprobado' si la calificación es 
# 60 o más y 'Reprobado' en caso contrario.
def calificacion_examenes(calificacion):
    if calificacion >= 60:
        return 'Aprobado'
    else:
        return 'Reprobado'

# Ejercicio 2: Determinar si un número es par o no
def es_numero_par(num):
    return num % 2 == 0


