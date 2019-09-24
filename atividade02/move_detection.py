import cv2
import numpy as np
import matplotlib.pyplot as plt

def histograma(img, dimensoes):
    altura = dimensoes[0]
    largura = dimensoes[1]

    hist_img = list(0 for i in range(255+1))

    for i in range(altura):
        for k in range(largura):
            hist_img[img[i, k]] += 1
    return hist_img

def realce(img, dimensoes):
    altura = dimensoes[0]
    largura = dimensoes[1]

    for i in range(altura):
        for k in range(largura):
            if img[i, k] >= 90:
                img[i, k] = 255
    return img

def colorir_diff(img1, img2, img_alvo, dimensoes):
    altura = dimensoes[0]
    largura = dimensoes[1]

    for i in range(altura):
        for k in range(largura):
            if(img2[i, k] == 255 and img1[i, k] <= 90):
                img_alvo[i, k, 0] = 0
                img_alvo[i, k, 1] = 0
                img_alvo[i, k, 2] = 255


img_B_01 = cv2.imread('imagens/Img_C_01.jpg', 0)
img_B_02 = cv2.imread('imagens/Img_C_02.jpg', 0)
img_B_02_color = cv2.imread('imagens/Img_C_02.jpg')
dimensoes = img_B_01.shape

hist = histograma(img_B_01, dimensoes)

plt.plot(hist)
plt.title("Histograma Img_C_01.jpg em gray scale")
plt.show()

hist = histograma(img_B_02, dimensoes)

plt.plot(hist)
plt.title("Histograma Img_C_02 em gray scale.jpg")
plt.show()

img_B_01_realcada = realce(img_B_01, dimensoes)
img_B_02_realcada =  realce(img_B_02, dimensoes)

colorir_diff(img_B_01_realcada, img_B_02_realcada, img_B_02_color, dimensoes)

cv2.imshow('Movimento', img_B_02_color)
cv2.imwrite('imagens/img_result_mov.jpg', img_B_02_color)
cv2.imwrite('imagens/img_C_01_grayscale.jpg', img_B_01)
cv2.imwrite('imagens/img_C_02_grayscale.jpg', img_B_02)
cv2.waitKey()
