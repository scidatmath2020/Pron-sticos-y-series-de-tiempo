# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:54:53 2021

@author: hp
"""


import pandas as pd
import numpy as np
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf # (p,q) orders
from statsmodels.tsa.seasonal import seasonal_decompose      # ETS Plots
                            


import warnings
warnings.filterwarnings("ignore")

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")



#%%

# Dataset
data = pd.read_csv("contaminacion.csv")

data.head()

#%%

data['fecha']=pd.to_datetime(dict(year=data['year'], month=data['month'], day=1))
data.set_index('fecha',inplace=True)
data.index.freq = 'MS'
data.head()

#%%

title = 'Promedio mensual de niveles de CO2 en Mauna Loa, Hawaii'
ylabel='Partes por millón'
xlabel='' 

ax = data['interpolated'].plot(figsize=(12,6),title=title)
ax.autoscale(axis='x',tight=True)
ax.set(xlabel=xlabel, ylabel=ylabel)

#%%

'''Descomposición en estaciones'''

result = seasonal_decompose(data['interpolated'], model='add')
result.plot()

#%%

'''Dividir en datos de entrenamiento y prueba'''

len(data)

entrenamiento = data.iloc[:717]
prueba = data.iloc[717:]

#%%
'''
######################################
################### SARIMAX
######################################
'''

modelo = SARIMAX(entrenamiento['interpolated'],order=(0,1,1),seasonal_order=(1,0,1,12))
resultados = modelo.fit()
resultados.summary()

# Obtener predicciones

inicio=len(entrenamiento)
final=len(entrenamiento)+len(prueba)-1
predicciones = resultados.predict(start=inicio, end=final).rename('SARIMA(0,1,1)(1,0,1,12) Predicciones')

# Comparar predicciones con los valores observados

for i in range(len(predicciones)):
    print(f"predicción={predicciones[i]:<11.10}, observado={prueba['interpolated'][i]}")
    
# Gráficas
title ='Promedio mensual de nivles de CO2 (ppm) sobre Mauna Loa, Hawaii'
ylabel='partes por millón'
xlabel=''

ax = prueba['interpolated'].plot(legend=True,figsize=(12,6),title=title)
predicciones.plot(legend=True)
ax.autoscale(axis='x',tight=True)
ax.set(xlabel=xlabel, ylabel=ylabel);


#%%

'''
####################
#############  Reentrenar el modelo con todos los datos y predecir el futuro
####################
'''

modelo = SARIMAX(data['interpolated'],order=(0,1,1),seasonal_order=(1,0,1,12))
resultados = modelo.fit()
pred = resultados.predict(len(data),len(data)+36).rename('SARIMA(0,1,1)(1,0,1,12) Futuro')

title ='Promedio mensual de nivles de CO2 (ppm) sobre Mauna Loa, Hawaii'
ylabel='partes por millón'
xlabel=''

ax = data['interpolated'].plot(legend=True,figsize=(12,6),title=title)
pred.plot(legend=True)
ax.set(xlabel=xlabel, ylabel=ylabel)
