library(tidyverse)
library(ggpubr)
library(factoextra)
library(gridExtra)

#set.seed(123)
#datos <- read.csv("archivo.csv", sep=",", encoding = "utf-8")
datosSP <- USArrests
datosSP <- scale(datosSP)

km_clustersSP <- kmeans(x = datosSP, centers = 4, iter.max = 10, 
 nstart = 50)

p1 <- fviz_cluster(object = km_clustersSP, geom = "point",  data = datosSP ) + ggtitle("k = P")

grid.arrange(p1, nrow = 2)