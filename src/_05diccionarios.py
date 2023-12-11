# diccionarios.py

def agregar_par_clave_valor(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

def eliminar_par_clave_valor(diccionario, clave):
    diccionario.pop(clave, None)
    return diccionario

def obtener_valor(diccionario, clave):
    return diccionario.get(clave)

def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_combinado = diccionario1.copy()
    diccionario_combinado.update(diccionario2)
    return diccionario_combinado