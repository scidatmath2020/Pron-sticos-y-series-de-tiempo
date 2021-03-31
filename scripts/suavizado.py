# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:54:39 2021

@author: hp
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing


os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

delitos = pd.read_csv("Tabla_rp.csv")[24:]
delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")
delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
delitos.set_index("fecha",inplace=True) 

delitos

delitos.columns

#%%

'''Promedio móvil simple'''

delitos['6-month-SMA'] = delitos['totales'].rolling(window=6).mean()
delitos['12-month-SMA'] = delitos['totales'].rolling(window=12).mean()

delitos
delitos.head(10)

delitos.columns

delitos = delitos[["totales","6-month-SMA","12-month-SMA"]]

delitos.plot()

#%%

'''Promedio móvil ponderado exponencial'''

delitos["EWMA12"] = delitos["totales"].ewm(span=12,adjust=False).mean()
delitos.plot()

#%%

'''Suavizado exponencial simple con SimpleExpSmoothing'''

delitos.index.freq = "M"
delitos.index

span = 12
alpha = 2/(span+1)

delitos['SES12']=SimpleExpSmoothing(delitos['totales']).fit(smoothing_level=alpha,optimized=False).fittedvalues.shift(-1)
delitos.head()
#%%

'''Suavizado exponencial doble'''

delitos['DESadd12'] = ExponentialSmoothing(delitos['totales'], trend = 'add').fit().fittedvalues.shift(-1)
delitos.head()
delitos['DESmul12'] = ExponentialSmoothing(delitos['totales'], trend = 'mul').fit().fittedvalues.shift(-1)



delitos[["totales","EWMA12","DESadd12","DESmul12"]].plot()

#%%

'''Suavizado exponencial triple: Holt-Winters'''

delitos['TESadd12'] = ExponentialSmoothing(delitos['totales'],trend='add',seasonal='add',seasonal_periods=12).fit().fittedvalues
delitos.head()

delitos[['totales','EWMA12','DESadd12',"TESadd12"]].plot(figsize=(12,6)).autoscale(axis='x',tight=True)

