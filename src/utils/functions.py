import pandas as pd
import os 

def replace_string(df, col, string_list, replacement):
    '''
    Recorre una lista de strings para reemplazarlos por un mismo valor
    df: pandas Dataframe
    col: la columna a reemplazar
    string_list: lista de strings a recorrer
    replacement: el valor por el que se va a reemplazar
    '''

    for pos, val in enumerate(string_list):
        df[col] = df[col].str.replace(string_list[pos], replacement)
    
    return f'Ya se han sustituido los siguientes valores {string_list} por {replacement}'

#def cargar_datos(data_path, separador):
    '''
    Esta función sirve para cargar los datos de una ruta en particular
    Argumentos:
        - data_path: el path en el que se encuentran nuestros datos
        - sep: el separador que se va a emplear
    Retorna:
        - None
    '''
    #df = pd.read_csv(data=data_path, sep=separador)
    #return df

## A partir de aquí, todo el código tiene que ir en el jupyter notebook

#DATA_PATH = '../data/raw/Cleaned_2018_Flights.csv'
#separador=','

#df = cargar_datos(data_path=DATA_PATH, separador=separador)