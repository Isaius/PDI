import numpy as np
import cv2

# abrindo a imagem 1 em forma de matriz
img = cv2.imread('WashingtonDC_01.TIF', 0)
# img.shape retorna uma tupla com (altura, largura) ou (linhas, colunas)
dimensoes = img.shape
# guardando as dimensoes para serem usadas para percorrer a matriz
largura = dimensoes[1]
altura = dimensoes[0]
# variaveis resultados
media = 0
somatorio = 0
# percorrendo a matriz pixel por pixel e somando o valor de cinza
for i in range(altura-1):
    for k in range(largura-1):
        somatorio += img[i, k]

print("Somatorio niveis decinza: " str(somatorio))
media = somatorio/img.size
print("Media da imagem: " str(media))