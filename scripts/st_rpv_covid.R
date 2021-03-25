library(lubridate)
library(tseries)
library(forecast)
library(zoo)
library(ggplot2)

setwd("C:/Users/hp master/OneDrive/Escritorio/series tiempo")

tabla_df <- read.csv("Tabla_rp.csv")

View(tabla_df)

total_st <- ts(tabla_df$totales,frequency = 12,start=c(2010,1),end=c(2019,12))
rp_st <- ts(tabla_df$Robo_pv,frequency = 12,start=c(2010,1),end=c(2019,12))

start(total_st)
end(total_st)
frequency(total_st)

plot(total_st,
     col="blue",
     lwd=2,
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Serie temporal delitos 2010-2019")

########### Series multivariantes

delitos_multi <- cbind(total_st,rp_st)
class(delitos_multi)

plot(window(delitos_multi,start=c(2019,1),end=c(2019,12)))

######### Subconjunto de la serie

sub_total <- total_st[5:14]
sub_total
class(sub_total)

sub_total <- window(total_st,start=c(2010,5),end=c(2011,2))
sub_total
class(sub_total)

plot(sub_total,
     col="blue",
     lwd=2,
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Serie temporal delitos MAY10-FEB11")

### Plot multivariante en gráficos diferentes

plot(delitos_multi,
     col="blue",
     lwd=1,
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Serie temporal mensual total y rpv (2010-2011)")

### Plot multivariante en el mismo gráfico

plot(delitos_multi,plot.type = "single",
     col=c("blue","red"),
     lwd=1:2, #controla los grosores
     lty=1:2, #controla el tipo de línea
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Serie temporal mensual total y rpv (2010-2011)")
legend(x="topleft",legend=c("Total","RPV"),col=c("blue","red"),lty=1:2)

########################
########################
### paquetería zoo
###
### Los objetos zoo son series de tiempo con ciertas ventajas, como el uso de 
### fechas como nombres de las filas
########################
########################

library(zoo)

tiempo <- seq(as.Date("2010/1/1"),as.Date("2019/12/1"),"months")
tiempo
class(tiempo)
head(tiempo)

### Combinar el índice con la serie de tiempo

total_zoo <- zoo(x=tabla_df$totales,order.by = tiempo)
rp_zoo <- zoo(x=tabla_df$Robo_pv,order.by = tiempo)

class(total_zoo)
str(total_zoo)
head(total_zoo)

### Extraer el índice de tiempo y los datos

index(total_zoo)  #devuelve las fechas (los índices)
coredata(total_zoo) #devuelve los datos

# inicio y final

start(total_zoo)
end(total_zoo)

# Extraer subconjunto indexado por fechas; esto no se puede con ts

total_zoo_junio <- total_zoo[as.Date(c("2010/06/01",
                                       "2011/06/01",
                                       "2012/06/01",
                                       "2013/06/01",
                                       "2014/06/01",
                                       "2015/06/01",
                                       "2016/06/01",
                                       "2017/06/01",
                                       "2018/06/01",
                                       "2018/06/01"))]

plot(total_zoo_junio)

# ventanas

total_zoo_13_15 <- window(total_zoo,start=as.Date("2013/01/01"),end=as.Date("2015/12/1")))
total_zoo_13_15
plot(total_zoo_13_15)

# Combinando series

delitos_multi_zoo <- cbind(total_zoo,rp_zoo)
class(delitos_multi_zoo)
head(delitos_multi_zoo)

plot(delitos_multi_zoo,plot.type = "single",
     col=c("blue","red"),
     lwd=1:2,
     ylab="Total de delitos",
     xlab="Tiempo (meses)",
     main="Serie temporal mensual total y rpv (2010-2011)")
legend(x="topleft",legend=c("Total","RPV"),col=c("blue","red"),lty=1:1)

######
###### Graficador dygraphs
######
# install.packages("dygraphs")

library(dygraphs)

dygraph(total_zoo,main="Serie temporal mensual total (2010-2019)")
dygraph(delitos_multi_zoo,main="Serie temporal mensual total (2010-2019)")

#########
######### Manejo de datos diarios
#########

covid19 <- zoo(serie_covid$Total,as.Date(serie_covid$Fecha))
dygraph(covid19)
plot(covid19)