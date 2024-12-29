"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    agrupaciones = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir las columnas
            letra = columnas[0]  # Columna 1 (letra)
            valor = int(columnas[1])  # Columna 2 (convertir a entero)

            # Paso 2: Agrupar las letras por el valor de la columna 2
            if valor in agrupaciones:
                agrupaciones[valor].append(letra)  # Agregar letra a la lista existente
            else:
                agrupaciones[valor] = [letra]  # Crear nueva lista con la letra

    # Paso 3: Convertir a lista de tuplas y ordenar por valor de la columna 2
    resultado = sorted(agrupaciones.items())

    return resultado

