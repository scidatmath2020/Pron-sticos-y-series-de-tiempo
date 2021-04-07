# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:12:34 2021

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats.distributions import chi2
import statsmodels.tsa.stattools as sts
import statsmodels.api as sm
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

'''Diferenciar todas las series'''

sts.adfuller(delitos["totales"])[1]
sts.adfuller(horarios["manana"])[1]
sts.adfuller(horarios["tarde"])[1]
sts.adfuller(horarios["noche"])[1]
sts.adfuller(horarios["madrugada"])[1]

sgt.plot_acf(delitos["totales"].diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["manana"].diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["tarde"].diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["noche"].diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["madrugada"].diff().dropna(), zero = False, lags=40)

sgt.plot_acf(delitos["totales"].diff().dropna().diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["manana"].diff().dropna().diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["tarde"].diff().dropna().diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["noche"].diff().dropna().diff().dropna(), zero = False, lags=40)
sgt.plot_acf(horarios["madrugada"].diff().dropna().diff().dropna(), zero = False, lags=40)


delitos["totales"].diff().dropna().std()
delitos["totales"].diff().dropna().diff().dropna().std()

horarios["manana"].diff().dropna().std()
horarios["manana"].diff().dropna().diff().dropna().std()

horarios["tarde"].diff().dropna().std()
horarios["tarde"].diff().dropna().diff().dropna().std()

horarios["noche"].diff().dropna().std()
horarios["noche"].diff().dropna().diff().dropna().std()

horarios["madrugada"].diff().dropna().std()
horarios["madrugada"].diff().dropna().diff().dropna().std()

d=1  # en todos los casos

#%%
'''
##################################
##################################
########### Construímos las diferenciadas
##################################
##################################
'''

delitos_diff = delitos["totales"].diff()[1:]
horarios_diff = pd.DataFrame({"manana":horarios["manana"].diff()[1:],"tarde":horarios["tarde"].diff()[1:],"noche":horarios["noche"].diff()[1:],"madrugada":horarios["madrugada"].diff()[1:]})

modelo = sm.OLS(delitos_diff,sm.add_constant(horarios_diff))

resultados = modelo.fit()

nva_data = delitos_diff-resultados.predict()

nva_data.plot()
#%%

'''ARIMA'''
sts.adfuller(nva_data)

d=0

#####################
##### Autorregresivo
sgt.plot_pacf(nva_data, zero = False, lags=40,method="ols")
p=4

#####################
##### Medias móviles

sgt.plot_acf(nva_data, zero = False, lags=40)
q=1


#%%

'''ARIMAX'''

modelo_ex = ARIMA(nva_data,order=(p,d,q))
resultados_ex = modelo_ex.fit()
plt.plot(nva_data)
plt.plot(resultados_ex.fittedvalues,color="red")

resultados_ex.summary()

#%%

modelo_ex2 = ARIMA(delitos["totales"],exog=delitos[["manana","tarde","noche","madrugada"]],order=(4,0,1))
resultados_ex2 = modelo_ex2.fit()

plt.plot(delitos["totales"])
plt.plot(resultados_ex2.fittedvalues,color="red")