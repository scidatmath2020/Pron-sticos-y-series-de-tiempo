#install.packages("tseries")
#install.packages("forecast")
#install.packages("zoo")


library(lubridate)
library(tseries)
library(forecast)
library(zoo)
library(ggplot2)

setwd("C:\\Users\\hp master\\OneDrive\\Escritorio\\series tiempo")

####################
####  Uso de POSIXt
####################

fecha1 <- as.POSIXct("2020-03-23 16:00:00")
fecha2 <- as.POSIXlt("2020-03-23 16:00:00")

fecha1
fecha2

unclass(fecha1)
unclass(fecha2)

####################
####  Uso de Date
####################

fecha3 <- as.Date("23/03/2020",format="%d/%m/%Y")
fecha3
#format(as.Date("23/03/2020",format="%d/%m/%Y"),"%m/%d/%Y")

####################
####  Uso de lubridate
####################

ymd(20210323) # año/mes/día
dmy(23032021) # día/mes/año

#format(dmy(23032021),"%m/%d/%Y")

##### Fechas y tiempos


mi_fecha <- ymd_hm("2021-03-23 15:40",tz="Mexico/General")
#OlsonNames()
OlsonNames()
minute(mi_fecha)
second(mi_fecha)
hour(mi_fecha)
day(mi_fecha)
year(mi_fecha)
month(mi_fecha)
wday(mi_fecha)


with_tz(mi_fecha, tz = "Mexico/BajaNorte")

mi_fecha2 <- mi_fecha
day(mi_fecha2) <- 24

mi_fecha2

intervalo <- interval(mi_fecha,mi_fecha2)
intervalo

##################
##################
##################

set.seed(2021)
datos <- runif(50,1,20)

serie <- ts(datos,start = 2021,frequency = 4)

unclass(serie)

plot(serie)

time(serie) #tiempos

serie <- ts(datos,start = c(2021,2),frequency = 4)
time(serie)

#########################
#########################
#########################

mis_datos <- read.csv("Rmissing.csv")

serie <- ts(mis_datos$mydata)
serie
class(serie)

summary(serie)

plot(serie)

###### 
###### Tratamiento de faltantes con zoo (las funciones na pertencen a zoo y los
###### graficadores a ggplot2)
###### 

serie_na_locf <- na.locf(serie) #rellena NA con el último valor previo

autoplot(serie_na_locf, ts.colour="red") +
  autolayer(serie, ts.colour="blue") 

serie_na_fill <- na.fill(serie,250) #rellena NA con el último valor previo

autoplot(serie_na_fill, ts.colour="red") +
  autolayer(serie, ts.colour="blue") 

###### 
###### Tratamiento de atípicos y faltantes con forecast
###### 

tsoutliers(serie)

serie_copia <- serie

serie_copia[tsoutliers(serie)$index] <- tsoutliers(serie)$replacements

plot(serie_copia)

autoplot(serie_copia, ts.colour="red") +
  autolayer(serie, ts.colour="blue") 

####################

serie_na_interpol <- na.interp(serie)  # rellenar NA con interpolaciones

autoplot(serie_na_interpol, ts.colour="red") +
  autolayer(serie, ts.colour="blue") 

####################

serie_limpia <- tsclean(serie)

autoplot(serie_limpia, ts.colour="red") +
  autolayer(serie, ts.colour="blue") 