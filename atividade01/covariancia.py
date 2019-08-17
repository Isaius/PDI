# este programa calcula a covariancia de uma imagem digital
# feito por Isaius

import numpy as np
import cv2

img = cv2.imread('WashingtonDC_01.TIF', 0)
# img.shape retorna uma tupla com (altura, largura) ou (linhas, colunas)
dimensoes = img.shape
# guardando as dimensoes para serem usadas para percorrer a matriz
largura = dimensoes[1]
altura = dimensoes[0]