"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import os
    import pandas as pd
    
    df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep = ";", index_col = 0)

    for column in df.select_dtypes(include = ["object"]).columns:
        df[column] = df[column].str.lower()
        df[column] = df[column].str.replace("_", " ")
        df[column] = df[column].str.replace("-", " ")
        df[column] = df[column].str.replace(",", "")
        df[column] = df[column].str.replace("$", "")
        df[column] = df[column].str.replace(".00", "")
        

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)    
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format = "%d/%m/%Y", errors = "coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format = "%Y/%m/%d", errors = "coerce"))

    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs("files/output", exist_ok=True)
    df.to_csv("files/output/solicitudes_de_credito.csv", sep = ";", index = False)