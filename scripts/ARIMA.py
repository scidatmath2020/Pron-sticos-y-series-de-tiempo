# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:39:06 2021

@author: hp
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats.distributions import chi2
import statsmodels.tsa.stattools as sts
#import seaborn as sns
import os

#sns.set()

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

#%%

delitos = pd.read_csv("Tabla_rp.csv")[24:]

delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")
delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
delitos.set_index("fecha",inplace=True) 

del delitos["Robo_pv"]

delitos

delitos["media_movil"] = delitos.rolling(window=12).mean()
delitos.plot()

#%%

'''
###########################################
###########################################
######## Analizamos la estacionariedad
###########################################
###########################################
'''

sts.adfuller(delitos["totales"])  # Se observa que no es estacionaria

sgt.plot_acf(delitos["totales"].diff().dropna(), zero = False, lags=40)
sgt.plot_acf(delitos["totales"].diff().dropna().diff().dropna(), zero = False, lags=40)

sts.adfuller(delitos["totales"].diff().dropna())
sts.adfuller(delitos["totales"].diff().dropna().diff().dropna())

delitos["totales"].diff().dropna().std()
delitos["totales"].diff().dropna().diff().dropna().std()

delitos["totales"].plot()
delitos["totales"].diff().dropna().plot()
delitos["totales"].diff().dropna().diff().dropna().plot()

d=1
'''Concluímos que d=1'''

#%%

'''Autorregresivo: función de autocorrelación parcial'''

sgt.plot_pacf(delitos["totales"].diff().dropna(), zero = False, lags=40,method="ols")

p=12

#%%

'''Medias móviles: función de autocorrelación'''

sgt.plot_acf(delitos["totales"].diff().dropna(), zero = False, lags=40)

q=12

#%%

modelo = ARIMA(delitos["totales"],order=(p,d,q))
resultados = modelo.fit()
plt.plot(delitos["totales"])
plt.plot(resultados.fittedvalues,color="red")


print(resultados.summary())

#%%

'''Análisis de los residuos'''

resultados.resid

residuals = pd.DataFrame(resultados.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])

#%%

resultados.predict(0,108).plot()
delitos["totales"].plot()

#%%



