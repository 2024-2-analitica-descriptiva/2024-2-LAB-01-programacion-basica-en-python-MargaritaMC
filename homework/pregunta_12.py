"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo, ordenado
    alfabéticamente por las claves.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    sumas_por_letra = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir columnas
            letra = columnas[0]  # Columna 1 (letra)
            valores_columna_5 = columnas[4].split(",")  # Columna 5 (dividir por comas)

            # Paso 2: Sumar los valores de la columna 5
            suma_valores = sum(int(par.split(":")[1]) for par in valores_columna_5)

            # Paso 3: Actualizar el diccionario
            if letra in sumas_por_letra:
                sumas_por_letra[letra] += suma_valores  # Sumar al total existente
            else:
                sumas_por_letra[letra] = suma_valores  # Inicializar con la suma actual

    # Paso 4: Ordenar el diccionario alfabéticamente por las claves
    sumas_por_letra_ordenado = dict(sorted(sumas_por_letra.items()))

    return sumas_por_letra_ordenado

