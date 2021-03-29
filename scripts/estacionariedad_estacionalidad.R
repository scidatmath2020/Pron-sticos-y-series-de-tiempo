library(tseries)
library(forecast)
library(zoo)

setwd("C:/Users/hp master/OneDrive/Escritorio/series tiempo")

wn_rw <- read.csv("wn_rw.csv")
tabla_df <- read.csv("Tabla_rp.csv")
serie_covid <- read.csv("muertes_covid.csv")

tabla_df <- tabla_df[-c(1:24),]

tiempo_wn_rw <- seq(as.Date("2021/1/1"),as.Date("2021/12/31"),"days")
tiempo_tabla_df <- seq(as.Date("2012/1/31"),as.Date("2019/12/31"),"months")

tiempo_tabla_df


ruido_blanco <- zoo(x=wn_rw$ruido,order.by = tiempo_wn_rw)
caminata_aleatoria <- zoo(x=wn_rw$caminata,order.by = tiempo_wn_rw)

total_delitos <- zoo(x=tabla_df$totales,order.by = tiempo_tabla_df,frequency=12)

muertes_covid <- zoo(serie_covid$Total,as.Date(serie_covid$Fecha))

plot(ruido_blanco)
plot(caminata_aleatoria)

plot(total_delitos)

plot(muertes_covid)

########################

adf.test(ruido_blanco)
adf.test(caminata_aleatoria)

adf.test(total_delitos, k = ceiling(12*(length(total_delitos)/100)^(1/4)))

adf.test(muertes_covid)

########################
