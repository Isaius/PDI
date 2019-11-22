import cv2
import math

img = cv2.imread("blobs.tif")
cv2.imshow("Imagem ruidosa", img)
cv2.waitKey()

# Filtro
imgf = cv2.GaussianBlur(img, (5, 5), 0, None, 10)
cv2.imshow("Aplicado o filtro gaussiano", imgf)
#imgf = cv2.medianBlur(img, 5)
#cv2.imshow("Aplicado o filtro da mediana", imgf)
cv2.waitKey()

# Limiarização
rel, img_lim = cv2.threshold(imgf, 145, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagem limiarizada", img_lim)

# Comparação
# Imagem original
orig = cv2.imread("imagem_original.png")
rel, orig_lim = cv2.threshold(orig, 172, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagem original", orig_lim)

pixel_total = math.pow(len(img_lim), 2)
eq_pixel = 0
for i in range(len(img_lim)):
    for j in range(len(img_lim[i])):
        if (img_lim[i,j].any() == orig_lim[i,j].any()):
            eq_pixel += 1

print((eq_pixel/pixel_total)*100)
cv2.waitKey()

cv2.imwrite("1_filtro_gaussiano.png", imgf)
cv2.imwrite("2_img_limiarizada.png", img_lim)
cv2.imwrite("3_img_original_limiarizada.png", orig_lim)