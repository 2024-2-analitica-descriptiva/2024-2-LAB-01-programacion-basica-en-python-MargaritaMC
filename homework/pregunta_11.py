"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    sumas_por_letra = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir columnas
            valor_columna_2 = int(columnas[1])  # Columna 2 (convertir a entero)
            letras_columna_4 = columnas[3].split(",")  # Columna 4 (dividir por comas)

            # Paso 2: Actualizar el diccionario
            for letra in letras_columna_4:
                if letra in sumas_por_letra:
                    sumas_por_letra[letra] += valor_columna_2  # Sumar el valor
                else:
                    sumas_por_letra[letra] = valor_columna_2  # Inicializar con el valor

    # Paso 3: Ordenar el diccionario por las claves alfabéticamente
    sumas_por_letra_ordenado = dict(sorted(sumas_por_letra.items()))

    return sumas_por_letra_ordenado

