"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5, ordenado alfabéticamente.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    conteo_claves = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir columnas
            diccionario = columnas[4]  # Columna 5 contiene el "diccionario"
            pares = diccionario.split(",")  # Dividir los pares por coma

            # Paso 2: Extraer las claves y contar
            for par in pares:
                clave = par.split(":")[0]  # Extraer la clave antes de ":"
                if clave in conteo_claves:
                    conteo_claves[clave] += 1  # Incrementar conteo
                else:
                    conteo_claves[clave] = 1  # Inicializar conteo

    # Paso 3: Ordenar el diccionario por las claves alfabéticamente
    conteo_claves_ordenado = dict(sorted(conteo_claves.items()))

    return conteo_claves_ordenado

print(pregunta_09())
