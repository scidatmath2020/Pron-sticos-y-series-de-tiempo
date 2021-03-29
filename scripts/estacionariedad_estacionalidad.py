# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:32:54 2021

@author: hp
"""
#pip install statsmodels

import pandas as pd
import numpy as np
from datetime import datetime 
import os
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

#%%

# Recordemos que Python empieza las numeraciones desde 0

delitos = pd.read_csv("Tabla_rp.csv")[24:]
delitos.totales.plot(figsize=(20,5),title="Total de delitos mes a mes por 8 años")

delitos


delitos.head()

delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")

delitos.head()

delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
delitos.set_index("fecha",inplace=True)

delitos.head()

delitos.totales
delitos.columns
#%%
delitos.totales.plot(figsize=(20,5),title="Robo parcial de vehículo")

sts.adfuller(delitos.totales,regression="ct"maxlag=???,autolag=None)

#%%

wn_rw = pd.read_csv("wn_rw.csv")
wn_rw["fecha"] = pd.date_range(pd.datetime(2021,1,1),periods=365,freq="d")


wn_rw.set_index("fecha",inplace=True)
sts.adfuller(delitos["totales"],regression="ct",maxlag=12,autolag=None)

delitos

#%%

'''Estacionalidad'''

descomposicion_aditiva_delitos_totales = seasonal_decompose(delitos["totales"],model="additive")
descomposicion_aditiva_delitos_totales.plot()

descomposicion_aditiva_ruido = seasonal_decompose(wn_rw["ruido"],model="additive")
descomposicion_aditiva_ruido.plot()

descomposicion_aditiva_caminata = seasonal_decompose(wn_rw["caminata"],model="additive")
descomposicion_aditiva_caminata.plot()



