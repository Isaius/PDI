import cv2
import numpy as np

def hitOrMiss(img, size_x, size_y):
    kernel = np.zeros((size_x+2, size_y+2), dtype=int)
    print("X: " +str(size_x) + " Y: " +str(size_y))
    for i in range(0, size_x+2):
        for j in range(0, size_y+2):
            if (i == 0 or j == 0 or i == size_x + 1 or j == size_y + 1):
                kernel[i, j] = -1
            else:
                kernel[i, j] = 1

    img_result = cv2.morphologyEx(im_th, cv2.MORPH_HITMISS, kernel)
    return img_result

# abrindo imagem
im_in = cv2.imread("morfologia.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("morfologia.png") 

# Threshold invertido
 
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)

size = im_in.shape


KERNEL_size_x = 27
KERNEL_size_y = 29  

img_result1 = hitOrMiss(im_th, KERNEL_size_x, KERNEL_size_y)

KERNEL_size_x = 20
KERNEL_size_y = 19

img_result2 = hitOrMiss(im_th, KERNEL_size_x, KERNEL_size_y)

KERNEL_size_x = 14   
KERNEL_size_y = 13

img_result3 = hitOrMiss(im_th, KERNEL_size_x, KERNEL_size_y)

img_comb = img_result1 | img_result2 | img_result3

# dilatando os 3 pontos
img_dilated = cv2.dilate(img_comb, None, iterations=18)

# realizando a interseção com a imagem original e colocando tudo que não
# seja branco (pontos dilatados) para branco
for i in range(size[0]):
    for j in range(size[1]):
        if(img_dilated[i, j] == 0):
            img_color[i, j, 0] = 255
            img_color[i, j, 1] = 255
            img_color[i, j, 2] = 255

cv2.imshow("1 Thresholded", im_th)
cv2.imshow("2 Result", img_result1)
cv2.imshow("3 Result", img_result2)
cv2.imshow("4 Result", img_result3)
cv2.imshow("5 Combination", img_comb)
cv2.imshow("6 Dilatada ", img_dilated)
cv2.imshow("7 Colorida Final", img_color)

cv2.waitKey(0)

cv2.imwrite("resultados/problema-4/1 - threshold.png", im_th)
cv2.imwrite("resultados/problema-4/2 - large_square.png", img_result1)
cv2.imwrite("resultados/problema-4/3 - medium_square.png", img_result2)
cv2.imwrite("resultados/problema-4/4 - tiny_square.png", img_result3)
cv2.imwrite("resultados/problema-4/5 - combination.png", img_comb)
cv2.imwrite("resultados/problema-4/6 - dilatated.png", img_dilated)
cv2.imwrite("resultados/problema-4/7 - color-final.png", img_color)