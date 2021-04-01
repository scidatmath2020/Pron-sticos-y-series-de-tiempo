# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:14:21 2021

@author: rodol
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:54:39 2021
@author: hp
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing


os.chdir("C:\\Users\\rodol\\Desktop\\Curso Modelos\\25-03-2021")

"pido que se lea del dato 25 en delante, para eliminar 2 años de errores metodológicos en ENVIPE"
delitos = pd.read_csv("Tabla_rp.csv")[24:]

delitos.head()
"puedo ver que faltan fechas..."

"debo añadir las fechas"
delitos["fecha"]  = pd.date_range(pd.datetime(2012,1,1), periods=96, freq="M")
"convierto a tipo fecha"
delitos.fecha = pd.to_datetime(delitos.fecha, dayfirst = False)
"coloco la columna como indices de la tabla"
delitos.set_index("fecha",inplace=True) 

"despliego tabla para verificar cambios"
delitos

"puedo verificar que fecha solo es índice"
delitos.columns

#%%

'''Promedio móvil simple'''

"en window se le asigna la ventana de datos que se usará para promediar" 
"hay que darle de comer nombre de columna nueva y columna de datos de feed"
delitos['6-month-SMA'] = delitos['totales'].rolling(window=6).mean()
delitos['12-month-SMA'] = delitos['totales'].rolling(window=12).mean()

"para ver cambios..."
delitos
delitos.head(10)

delitos.columns

"para eliminar columna Robo_pv o dicho de otra forma asignar las columnas que quiero ver cada que llame la tabla"
delitos = delitos[["totales","6-month-SMA","12-month-SMA"]]

"muestra la gráfica original en comparación con las 2 técnicas 6 y 12 meses de suavizdo"
delitos.plot()
"al observar el resultado podemos ver que se suavizo demasiado pues las gráficas original vs nuevas no se parecen"

#%%

'''Promedio móvil ponderado exponencial''' "ESTE MÉTODO FALLA PARA SUAVIZAR CUANDO HAY TENDENCIA ASC/DESCENDENTE"

"deberá probarse si el mejor ajuste es True o False, aunque ambos hacen ajuste fuerte-cerca o debil-lejos"
"hay diferentes métodos para darles peso al cálculo, el de span es de duración sabiendo la frecuencia"
"en el ejemplo se usa 12 debido a que el periodo es anual"
delitos["EWMA12"] = delitos["totales"].ewm(span=12,adjust=False).mean()
delitos
"muestra diferencia en la columna al ponderarlo de forma exponencial"
delitos.plot()
"puede verse que los representantes creados por promedios exponenciales móviles son mejores que los de promedio"
"simple"

"Comparar ambas formas de ajuste False/True"

delitos["EWMA12"] = delitos["totales"].ewm(span=12,adjust=False).mean()
delitos["EWMA12_adjT"] = delitos["totales"].ewm(span=12,adjust=True).mean()
delitos

delitos[["totales","EWMA12","EWMA12_adjT"]].plot()

"como se agrega cada columna, al imprimir todo se añaden nuevas iteraciones"
delitos.plot()

#"si quiero eliminar columnas de datos, para comparar ajustes...
#delitos = delitos[["totales","EWMA12","EWMA12_adjT"]]
#delitos.plot()
#%%

'''Suavizado exponencial simple con la función SimpleExpSmoothing'''

delitos.index
"puedo observar que no tienen frecuencia los índices, debo de decirle a Python que es mensual, pudiendo ser diaria"
"o anual si se requiere"
delitos.index.freq = "M"
delitos.index

span = 12
alpha = 2/(span+1)

"Esta línea debe mantenerse así para que pueda realizar el proceso"
delitos['SES12']=SimpleExpSmoothing(delitos['totales']).fit(smoothing_level=alpha,optimized=False).fittedvalues.shift(-1)
delitos.head()
"para ver igualdad de cálculo de suavizado"
delitos[["SES12","EWMA12"]].head(10)
#%%

"SE PUEDE UTILIZAR CUANDO HAY TENDENCIA"
'''Suavizado exponencial doble''' "Método de Holt - Con Beta"

"se usa trending o forma de cálculo additivo"
delitos['DESadd12'] = ExponentialSmoothing(delitos['totales'], trend = 'add').fit().fittedvalues.shift(-1)
delitos.head()
"se usa trendint o forma de cálculo multiplicativo"
delitos['DESmul12'] = ExponentialSmoothing(delitos['totales'], trend = 'mul').fit().fittedvalues.shift(-1)



delitos[["totales","EWMA12","DESadd12","DESmul12"]].plot()

#%%

"MEJOR MÉTODO PARA TENDENCIAS EN SERIES CON ESTACIONALIDAD"
'''Suavizado exponencial triple: Holt-Winters''' "+Beta (tendencia) +Gamma (estacionalidad)"

delitos['TESadd12'] = ExponentialSmoothing(delitos['totales'],trend='add',seasonal='add',seasonal_periods=12).fit().fittedvalues
delitos.head()

"Para ver todas las formas de suavizado comparadas"
delitos[['totales','EWMA12','DESadd12',"DESmul12","TESadd12"]].plot(figsize=(12,6)).autoscale(axis='x',tight=True)

"Para ver la comparación de la original con la representación de suavizado"
delitos[['totales',"DESmul12","TESadd12"]].plot()
"Y puedo comprobar que la función Holt-Winters fue la mejor para representar la distribución original"
"Esto prepara lo necesario para realizar futuras predicciones"

"Comparar con tendencia multiplicativa"
delitos['TESmul12'] = ExponentialSmoothing(delitos['totales'],trend='mul',seasonal='mul',seasonal_periods=12).fit().fittedvalues
delitos[['totales',"TESadd12","TESmul12"]].plot()
