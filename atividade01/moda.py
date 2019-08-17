# este programa calcula a moda de uma imagem digital
# feito por Isaius

import numpy as np
import cv2

img = cv2.imread('WashingtonDC_01.TIF', 0)
# img.shape retorna uma tupla com (altura, largura) ou (linhas, colunas)
dimensoes = img.shape
# guardando as dimensoes para serem usadas para percorrer a matriz
largura = dimensoes[1]
altura = dimensoes[0]
# frequencia ira ser um contador dos niveis de cinza
# onde cada indice representa um dos 256 valores, de 0 à 255
frequencia = []
# preenchendo os contadores de 0
for i in range(255+1):
    frequencia.append(0)
# percorrendo a matriz imagem
for i in range(altura):
    for k in range(largura):
        # incrementando o contador do nivel de intensidade atual em +1
        frequencia[img[i, k]] += 1

maior = 0
# agora procurando qual o maior contador
for i in range(255+1):
    if frequencia[i] >= frequencia[maior]:
        maior = i

print("O nivel de cinza com maior frequência é: " + str(maior))
