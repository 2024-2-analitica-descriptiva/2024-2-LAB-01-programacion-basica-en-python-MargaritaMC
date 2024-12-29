"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    min_max_por_clave = {}

    # Paso 1: Leer el archivo
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir la línea en columnas
            diccionario = columnas[4]  # Columna 5 contiene el "diccionario"
            pares = diccionario.split(",")  # Dividir los pares por coma

            # Paso 2: Procesar cada par clave:valor
            for par in pares:
                clave, valor = par.split(":")  # Separar clave y valor
                valor = int(valor)  # Convertir el valor a entero

                # Actualizar mínimos y máximos en el diccionario
                if clave in min_max_por_clave:
                    min_max_por_clave[clave][0] = min(min_max_por_clave[clave][0], valor)  # Actualizar mínimo
                    min_max_por_clave[clave][1] = max(min_max_por_clave[clave][1], valor)  # Actualizar máximo
                else:
                    min_max_por_clave[clave] = [valor, valor]  # Inicializar mínimo y máximo con el mismo valor

    # Paso 3: Convertir a lista de tuplas y ordenar
    resultado = [(clave, minimo, maximo) for clave, (minimo, maximo) in min_max_por_clave.items()]
    resultado_ordenado = sorted(resultado)

    return resultado_ordenado

