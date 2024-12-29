"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    resultado = []

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir la línea en columnas
            letra = columnas[0]  # Columna 1 (letra)
            cantidad_columna_4 = len(columnas[3].split(","))  # Contar elementos de la columna 4
            cantidad_columna_5 = len(columnas[4].split(","))  # Contar elementos de la columna 5

            # Crear la tupla y agregarla al resultado
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))

    return resultado

