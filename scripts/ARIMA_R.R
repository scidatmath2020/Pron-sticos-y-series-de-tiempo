### ARIMA 
library(forecast)
library(tseries)
# Lynx: Número anual de linces atrapados entre 1821-1934 en Canadá
plot(lynx)

tsdisplay(lynx) # autoregresion

### DF test

adf.test(lynx) #la serie es estacionaria


### AR(2) 

mi_arima = arima(lynx, order = c(2,0,0))
mi_arima

tail(lynx)
plot(residuals(mi_arima))


### MA(2) 
mi_arima = arima(lynx, order = c(0,0,2))
mi_arima

plot(residuals(mi_arima))



### Arima del paquete forecast 
myarima <- Arima(lynx, order = c(4,0,0))
myarima

checkresiduals(myarima)


### ARIMA Forecast

# Forecast de 10 años
arimafore <- forecast(myarima, h = 10)

?forecast()

plot(arimafore)

# Valores estimados del futuro
arimafore$mean

# Ultimas observaciones y forecast
plot(arimafore, xlim = c(1930, 1944))

