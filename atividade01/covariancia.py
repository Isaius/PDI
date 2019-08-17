# este programa calcula a covariancia de uma imagem digital
# feito por Isaius

import numpy as np
import cv2

img1 = cv2.imread('WashingtonDC_01.TIF', 0)
# img.shape retorna uma tupla com (altura, largura) ou (linhas, colunas)
dimensoes1 = img1.shape
# guardando as dimensoes para serem usadas para percorrer a matriz
largura1 = dimensoes1[1]
altura1 = dimensoes1[0]

img2 = cv2.imread('WashingtonDC_02.TIF', 0)
# img.shape retorna uma tupla com (altura, largura) ou (linhas, colunas)
dimensoes2 = img2.shape
# guardando as dimensoes para serem usadas para percorrer a matriz
largura2 = dimensoes2[1]
altura2 = dimensoes2[0]

if(largura1 == largura2 and altura1 == altura2):
    print("imagens de mesma dimensao")
    altura = altura1
    largura = largura1

somatorio = 0
media1 = 0
# percorrendo a matriz pixel por pixel e somando o valor de cinza
for i in range(altura):
    for k in range(largura):
        somatorio += img1[i, k]
# media da imagem
media1 = somatorio/img1.size

media2 = 0
somatorio = 0
# percorrendo a matriz pixel por pixel e somando o valor de cinza
for i in range(altura):
    for k in range(largura):
        somatorio += img2[i, k]
# media da imagem
media2 = somatorio/img2.size

somatorio = 0
# algora calculando a covariancia entre as duas imagens
for i in range(altura):
    for k in range(largura):
        # desvio de cinza da imagem 1
        desvio1 = img1[i, k] - media1
        # desvio de cinza da imagem 2
        desvio2 = img2[i, k] - media2
        #somatorio do produto entre os dois desvios
        somatorio += desvio1*desvio2

covariancia = somatorio/(img1.size-1)
print("A covariancia entre as duas imagens é: " + str(covariancia))