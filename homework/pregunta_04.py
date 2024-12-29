"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    conteo_por_mes = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir la línea en columnas
            fecha = columnas[2]  # Columna 3 contiene la fecha
            mes = fecha.split("-")[1]  # Extraer el mes (segundo componente de la fecha)

            # Contar registros por mes
            if mes in conteo_por_mes:
                conteo_por_mes[mes] += 1
            else:
                conteo_por_mes[mes] = 1

    # Convertir el diccionario a lista de tuplas y ordenar por mes
    resultado = sorted(conteo_por_mes.items())

    return resultado

