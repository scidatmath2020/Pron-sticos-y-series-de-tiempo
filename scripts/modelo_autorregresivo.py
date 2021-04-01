# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:08:58 2021

@author: hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats.distributions import chi2
import statsmodels.tsa.stattools as sts
import seaborn as sns
import os
sns.set()

os.chdir("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

#%%

delitos = pd.read_csv("Tabla_rp.csv")[24:]
delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")
delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
delitos.set_index("fecha",inplace=True) 

del delitos["Robo_pv"]

#%%

sgt.plot_pacf(delitos["totales"], zero = False, lags=40,method="ols")

#%%

'''
#########################################################
########   Prueba chi2   ################################
#########################################################
'''

def prueba_chi2(modelo1,modelo2,DF=1):
    L1 = modelo1.llf
    L2 = modelo2.llf
    LR = (2*(L2 - L1))
    p = chi2.sf(LR,DF).round(3)
    return p

def juicio(p):
    if p<0.05:
        return "Como el p-valor es menor que 0.05, los dos modelos son significativamente diferentes. Nos quedamos con el segundo"
    else:
        return "Como el p-valor no es menor que 0.05, los dos modelos son significativamente iguales. Nos quedamos con el primero"

#%%


'''Modelo AR(p)

De los resultados obtenidos, nos interesará enfocarnos en los coeficientes
y sus p-valores: 

############################################################
############################################################
    
SI EL P-VALOR ES GRANDE (MAYOR A 0.05 O 0.1) ENTONCES EL 
COEFICIENTE ASOCIADO NO ES SIGNIFICATIVAMENTE DIFERENTE DE 0. POR LO TANTO
BUSCAMOS QUE EL P-VALOR SEA PEQUEÑO

############################################################
############################################################

'''

model_ar1 = ARIMA(delitos["totales"],order=(1,0,0))
resultados_ar1 = model_ar1.fit()
print(resultados_ar1.summary())

model_ar2 = ARIMA(delitos["totales"],order=(2,0,0))
resultados_ar2 = model_ar2.fit()
print(resultados_ar2.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar1,resultados_ar2)}.\n{juicio(prueba_chi2(resultados_ar1,resultados_ar2))}")

model_ar3 = ARIMA(delitos["totales"],order=(3,0,0))
resultados_ar3 = model_ar3.fit()
print(resultados_ar3.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar2,resultados_ar3)}.\n{juicio(prueba_chi2(resultados_ar2,resultados_ar3))}")

model_ar4 = ARIMA(delitos["totales"],order=(4,0,0))
resultados_ar4 = model_ar4.fit()
print(resultados_ar4.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar3,resultados_ar4)}.\n{juicio(prueba_chi2(resultados_ar3,resultados_ar4))}")

model_ar5 = ARIMA(delitos["totales"],order=(5,0,0))
resultados_ar5 = model_ar5.fit()
print(resultados_ar5.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar4,resultados_ar5)}.\n{juicio(prueba_chi2(resultados_ar4,resultados_ar5))}")

model_ar6 = ARIMA(delitos["totales"],order=(6,0,0))
resultados_ar6 = model_ar6.fit()
print(resultados_ar6.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar5,resultados_ar6)}.\n{juicio(prueba_chi2(resultados_ar5,resultados_ar6))}")


model_ar7 = ARIMA(delitos["totales"],order=(7,0,0))
resultados_ar7 = model_ar7.fit()
print(resultados_ar7.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar6,resultados_ar7)}.\n{juicio(prueba_chi2(resultados_ar6,resultados_ar7))}")

model_ar8 = ARIMA(delitos["totales"],order=(8,0,0))
resultados_ar8 = model_ar8.fit()
print(resultados_ar8.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar7,resultados_ar8)}.\n{juicio(prueba_chi2(resultados_ar7,resultados_ar8))}")


model_ar9 = ARIMA(delitos["totales"],order=(9,0,0))
resultados_ar9 = model_ar9.fit()
print(resultados_ar9.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar8,resultados_ar9)}.\n{juicio(prueba_chi2(resultados_ar8,resultados_ar9))}")

model_ar10 = ARIMA(delitos["totales"],order=(10,0,0))
resultados_ar10 = model_ar10.fit()
print(resultados_ar10.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar9,resultados_ar10)}.\n{juicio(prueba_chi2(resultados_ar9,resultados_ar10))}")


model_ar11 = ARIMA(delitos["totales"],order=(11,0,0))
resultados_ar11 = model_ar11.fit()
print(resultados_ar11.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar10,resultados_ar11)}.\n{juicio(prueba_chi2(resultados_ar10,resultados_ar11))}")

model_ar12 = ARIMA(delitos["totales"],order=(12,0,0))
resultados_ar12 = model_ar12.fit()
print(resultados_ar12.summary())
print(f"El p-valor es {prueba_chi2(resultados_ar11,resultados_ar12)}.\n{juicio(prueba_chi2(resultados_ar11,resultados_ar12))}")

#%%

print(f"El p-valor es {prueba_chi2(resultados_ar1,resultados_ar12)}.\n{juicio(prueba_chi2(resultados_ar1,resultados_ar12))}")






 















