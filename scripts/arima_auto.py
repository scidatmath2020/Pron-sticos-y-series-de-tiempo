# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:40:05 2021

@author: hp
"""

import pandas as pd
import numpy as np
#import scipy
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from scipy.stats.distributions import chi2
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose

import pmdarima
#import seaborn as sns
import os

#sns.set()

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

#%%

delitos = pd.read_csv("Tabla_horarios.csv")

delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")
delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
delitos.set_index("fecha",inplace=True) 

delitos.columns

horarios = delitos[["manana","tarde","noche","madrugada"]]

#%%

model_auto = pmdarima.auto_arima(delitos["totales"], exogenous = delitos[["manana","tarde","noche","madrugada"]])

model_auto

model_auto.summary()

modelo_ex = ARIMA(delitos["totales"],exog=delitos[["manana","tarde","noche","madrugada"]],order=(0,1,2))
resultados_ex = modelo_ex.fit()

plt.plot(delitos["totales"])
plt.plot(resultados_ex.fittedvalues,color="red")

#%%

descomposicion_aditiva_delitos_totales = seasonal_decompose(delitos["totales"],model="additive")
descomposicion_aditiva_delitos_totales.plot()

model_auto2 = pmdarima.auto_arima(delitos["totales"],exogenous = delitos[["manana","tarde","noche","madrugada"]],
                                  seasonal = True, max_order = None, max_p = 7, max_q = 7, max_d = 2, max_P = 4, max_Q = 4, max_D = 2,
                                  maxiter = 50, alpha = 0.05, n_jobs = -1, information_criterion = 'aic')


model_auto2.summary()

modelo_ex2 = SARIMAX(delitos['totales'],exog=delitos[["manana","tarde","noche","madrugada"]],
                     order=(0,1,2),seasonal_order=(0,0,0,0))

resultados_ex2 = modelo_ex2.fit()

plt.plot(delitos["totales"])
plt.plot(resultados_ex2.fittedvalues,color="red")

#%%

modelo_ex3 = SARIMAX(delitos['totales'],exog=delitos[["manana","tarde","noche","madrugada"]],
                     order=(0,1,2),seasonal_order=(1,0,1,12))

resultados_ex3 = modelo_ex3.fit()

resultados_ex3.summary()

plt.plot(delitos["totales"])
plt.plot(resultados_ex3.fittedvalues,color="red")

