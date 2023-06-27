"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np
import re


def ingest_data():

    #
    # Inserte su código aquí
    #
    df_copy=pd.read_fwf("clusters_report.txt", skiprows=4, names=['1', '2', '3', '4'])
    df = pd.DataFrame(columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    for ind in range(len(df_copy)):
        if not (np.isnan(df_copy.iloc[ind]['1'])):
            df.loc[len(df.index)] = [df_copy.iloc[ind]['1'], df_copy.iloc[ind]['2'], df_copy.iloc[ind]['3'], df_copy.iloc[ind]['4']]
        else:
            df.at[len(df.index)-1, 'principales_palabras_clave'] += " " + df_copy.iloc[ind]['4']

    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: re.sub('\s+', ' ', x))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: re.sub(',\s*', ', ', x))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x.rstrip('.'))
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(lambda x: float(re.sub(',', '.', re.findall('\d+,\d+', x)[0])))
    df['cluster'] = df['cluster'].apply(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].apply(int)


    return df
