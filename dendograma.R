library(factoextra)
#datos <- read.csv("credit_card_datalNorXY.csv", sep=",", encoding = "utf-8")
datos <- USArrests
datos <- scale(datos)
#set.seed(101)

hc_euclidea_completo <- hclust(d = dist(x = datos, method = "euclidean"),
                               method = "complete")

fviz_dend(x = hc_euclidea_completo, k = 4, cex = 0.6) +
  geom_hline(yintercept = 5.5, linetype = "dashed") +
  labs(title = "Herarchical clustering",
       subtitle = "Distancia euclídea, Lincage complete, K=2")

