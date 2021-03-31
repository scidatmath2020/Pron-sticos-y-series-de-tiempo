# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:19:19 2021

@author: hp
"""
import pandas as pd
import numpy as np
import os

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")
os.listdir()

#%%

indices = pd.read_csv('Index2018.csv') #tiene 6269 filas

nva_tabla = indices.copy()

indices.columns

indices.head()

#%%
'''
###################################################
###################    Transformación de datos
###################################################
'''

'''Convertimos la columna date en tipo fecha'''

indices.describe()

indices.date.describe()

indices.date = pd.to_datetime(indices.date, dayfirst = True)

indices.head()

indices.date.describe()

#%%

'''Indexando la tabla con fechas
En series de tiempo, es importante que los índices de las tablas sean las fechas.
'''

'''Reemplaza la tabla indices con el resultado de colocar la columna date
como nombre de las filas'''
indices.set_index("date",inplace=True) 

indices.head()

#%%

'''Establecemos la frecuencia
Recordemos que la frecuencia en las series de tiempo debe mantenerse constante
'''

indices.head(10)

indices = indices.asfreq("d")

indices.head(10)

indices

indices = indices.asfreq("b") # business days

indices.head(10)

#%%

''' Manejo de valore faltantes
Veremos que el manejo de faltantes en series de tiempo es un problema ligeramente
diferente al caso de tablas no temporales
'''

indices.isna()

indices.isna().sum()

nan_rows = indices[indices.isnull().any(1)]
nan_rows

######################################

indices.spx = indices.spx.fillna(method="ffill") # frontfill
indices.dax = indices.dax.fillna(method="bfill") # backfill
indices.ftse = indices.ftse.fillna(method="ffill")
indices.nikkei = indices.nikkei.fillna(value=indices.nikkei.mean())

indices.isna().sum()

nan_rows = indices[indices.isnull().any(1)]
nan_rows

# Eliminación de columnas

# del tabla["nombre_columna"]; 
# del indices["nikkei"]



























#%%