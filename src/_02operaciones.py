# Ejercicio 1: Sumar dos números
def sumar(a, b):
    return a + b

# Ejercicio 2: Restar dos números
def restar(a, b):
    return a - b

# Ejercicio 3: Multiplicar dos números
def multiplicar(a, b):
    return a * b

# Ejercicio 4: Dividir dos números
def dividir(a, b):
    if b == 0:
        return "Error: División por cero."
    else:
        return a / b

# Ejercicio 5: Concatenar dos cadenas de texto
def concatenar(cadena1, cadena2):
    return cadena1 + cadena2

# Ejercicio 6: Calcular la longitud de una cadena de texto
def longitud(cadena):
    return len(cadena)
    
# Ejercicio 7: Convertir una cadena de texto a mayúsculas
def a_mayusculas(cadena):
    return cadena.upper()

# Ejercicio 8: Convertir una cadena de texto a minúsculas
def a_minusculas(cadena):
    return cadena.lower()
