library(factoextra)
library(tidyverse)
library(ggpubr)
data("USArrests")
head(USArrests)
str(USArrests)
USArrests

#datos <- read.csv("libro2.csv", sep=",", encoding = "utf-8")
datos <-USArrests
datos <- scale(datos )
fviz_nbclust(x = datos, FUNcluster = kmeans, method = "wss", k.max = 15, 
             diss = get_dist(datos, method = "euclidean"), nstart = 50)
