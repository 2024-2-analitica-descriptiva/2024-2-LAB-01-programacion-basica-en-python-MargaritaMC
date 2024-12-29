"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    valores_por_letra = {}

    # Paso 1: Leer el archivo y agrupar los valores
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir columnas
            letra = columnas[0]  # Columna 1 (letra)
            valor = int(columnas[1])  # Columna 2 (número convertido a entero)

            # Agregar el valor a la lista correspondiente a la letra
            if letra in valores_por_letra:
                valores_por_letra[letra].append(valor)
            else:
                valores_por_letra[letra] = [valor]

    # Paso 2: Calcular máximo y mínimo para cada letra
    resultado = []
    for letra, valores in valores_por_letra.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((letra, maximo, minimo))

    # Paso 3: Ordenar el resultado alfabéticamente por letra
    resultado_ordenado = sorted(resultado)

    return resultado_ordenado


