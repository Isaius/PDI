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

show("Elimina elementos desnecessários", img)
cv2.imwrite("resultados/problema-5/1-Eliminar-elem-desnecessarios.png", img)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show("Escala de cinza", cinza)
cv2.imwrite("resultados/problema-5/2-Graus-de-cinza.png", cinza)

ret, lim = cv2.threshold(cinza, 100, 255, cv2.THRESH_BINARY_INV)
show("Limiarização inversa", lim)
cv2.imwrite("resultados/problema-5/3-Limiarizado.png", lim)

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

cv2.imwrite("resultados/problema-5/4-Resultado.png", esq)