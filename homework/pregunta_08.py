"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    agrupaciones = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir columnas
            letra = columnas[0]  # Columna 1 (letra)
            valor = int(columnas[1])  # Columna 2 (convertir a entero)

            # Paso 2: Agrupar las letras por el valor de la columna 2
            if valor in agrupaciones:
                agrupaciones[valor].add(letra)  # Usar un conjunto para evitar duplicados
            else:
                agrupaciones[valor] = {letra}  # Crear un conjunto con la letra

    # Paso 3: Ordenar las letras y convertir a lista de tuplas
    resultado = []
    for valor, letras in agrupaciones.items():
        letras_ordenadas = sorted(letras)  # Ordenar las letras alfabéticamente
        resultado.append((valor, letras_ordenadas))

    # Paso 4: Ordenar la lista de tuplas por el valor de la columna 2
    resultado_ordenado = sorted(resultado)

    return resultado_ordenado

