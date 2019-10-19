import cv2
import numpy as np

IMG_SIZE = 200
PURPLE = (164, 73, 163)

def show(winname, img):
    cv2.imshow(winname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("morfologia.png")
show("Imagem original", img)

# Se livrar dos elementos desnecessarios
for i in range(IMG_SIZE):
    for j in range(IMG_SIZE):
        if np.all(img[i][j] == 0) or np.any(img[i][j] == PURPLE[0]):
            img[i][j] = (255, 255, 255)

show("Elimina elementos desnecessários", img)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show("Escala de cinza", cinza)

ret, lim = cv2.threshold(cinza, 200, 255, cv2.THRESH_BINARY)
show("Limiarizado", lim)

cont, hierarchy = cv2.findContours(lim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

fecho = []
for i in range(len(cont)):
    fecho.append(cv2.convexHull(cont[i], False))

res = np.zeros((lim.shape[0], lim.shape[1], 3), np.uint8)
for i in range(len(cont)):
    cor_contorno = (0, 0, 255)
    cor_fecho = (0, 255, 0)
    cv2.drawContours(res, cont, i, cor_contorno, 1, 8, hierarchy)
    cv2.drawContours(res, fecho, i, cor_fecho, 1, 8)

show("Fechos convexos", res)

cv2.imwrite("output\problema-3.png", res)