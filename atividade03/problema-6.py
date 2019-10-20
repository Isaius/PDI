import cv2
import numpy as np

IMG_SIZE = 200
RED = (36, 28, 237)

def show(winname, img):
    cv2.imshow(winname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("morfologia.png")
show("Imagem original", img)

# Se livrar dos elementos desnecessarios
for i in range(IMG_SIZE):
    for j in range(IMG_SIZE):
        if img[i][j][2] != 237:
            img[i][j] = (255, 255, 255)

cv2.imwrite("resultados/problema-6/grascale.png", img)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show("Escala de cinza", cinza)
cv2.imwrite("resultados/problema-6/grascale-filtred.png", cinza)

ret, lim = cv2.threshold(cinza, 200, 255, cv2.THRESH_BINARY)
show("Limiarizado", lim)

cont, hierarchy = cv2.findContours(lim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

fecho = []
for i in range(len(cont)):
    fecho.append(cv2.convexHull(cont[i], False))

res = np.zeros((lim.shape[0], lim.shape[1], 3), np.uint8)
for i in range(len(cont)):
    cor_fecho = (0, 255, 0)
    cv2.drawContours(res, fecho, i, cor_fecho, 1, 8)


for i in range(IMG_SIZE):
    for j in range(IMG_SIZE):
        if i == 0 or j == 0 or i == IMG_SIZE-1 or j == IMG_SIZE-1:
            res[i, j, 0] = 0
            res[i, j, 1] = 0
            res[i, j, 2] = 0

in_hole = True

cv2.imwrite("resultados/problema-6/fecho.png", res)
show("Fecho convexos", res)

cinza = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

ret, lim = cv2.threshold(cinza, 100, 255, cv2.THRESH_BINARY_INV)
show("Limiarização inversa", lim)

cv2.imwrite("resultados/problema-6/inv_lim_grayscale.png", lim)

tam = np.size(lim)
esq = np.zeros(lim.shape, np.uint8)
elem = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
done = False

while not done:
    erodido = cv2.erode(lim, elem)
    temp = cv2.dilate(erodido, elem)
    temp = cv2.subtract(lim, temp)
    esq = cv2.bitwise_or(esq, temp)
    lim = erodido.copy()

    zeros = tam - cv2.countNonZero(lim)
    if zeros == tam:
        done = True

show("Esqueleto", esq)

cv2.imwrite("resultados/problema-6/esqueleto-fecho.png", esq)