gbf#install.packages("TTR")
library(tseries)
library(TTR)
library(forecast)

setwd("C:/Users/hp master/OneDrive/Escritorio/series tiempo")

delitos <- read.csv("Tabla_rp.csv")
delitos <- delitos[-c(1:24),]

delitos_ts <- ts(delitos$totales,start=2012,freq=12)

#################################################
###########                          ############  
###########  Medias móviles simple   ############
###########                          ############
#################################################

delitos_month_SMA <- SMA(delitos_ts,n=12)

delitos_suavizados <- cbind(delitos_ts,delitos_month_SMA)

plot(delitos_suavizados,plot.type = "single",
     col=c("blue","red"),
     lwd=1:1, 
     lty=1:1, 
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Suavizados")
legend(x="topleft",legend=c("Original","SMA"),col=c("blue","red"),lty=1:1)

######################################################
###########                               ############  
###########  Medias móviles exponencial   ############
###########                               ############
######################################################

modelo_ets = ets(delitos_ts,model="ZZZ") #error, tendencia y estacionalidad
modelo_ets
plot(delitos_ts)
lines(modelo_ets$fitted,col="red")

######################################
###########               ############  
###########  Predicción   ############
###########               ############
######################################

plot(forecast(modelo_ets,h=12,level=90))

