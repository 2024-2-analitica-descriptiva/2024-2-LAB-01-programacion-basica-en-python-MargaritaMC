"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """

    # Paso 1: Mapeo (fase Map)
    pares = []  # Aquí almacenaremos los pares clave-valor generados
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividimos por tabulador
            letra = columnas[0]  # Primera columna es la clave
            pares.append((letra, 1))  # Agregamos el par clave-valor (letra, 1)

    # Paso 2: Reducción (fase Reduce)
    conteo = {}  # Diccionario para almacenar los resultados de la reducción
    for clave, valor in pares:
        if clave in conteo:
            conteo[clave] += valor  # Sumar los valores si ya existe la clave
        else:
            conteo[clave] = valor  # Crear una nueva clave si no existe

    # Paso 3: Ordenar los resultados
    resultado = sorted(conteo.items())  # Convertimos a lista de tuplas y ordenamos

    return resultado


