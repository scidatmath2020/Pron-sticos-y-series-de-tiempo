#install.packages("tseries")
#install.packages("forecast")

library(lubridate)
library(tseries)
library(forecast)

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