import cv2;
import numpy as np;
 
# abrindo imagem
im_in = cv2.imread("morfologia.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("morfologia.png") 

# Threshold invertido
 
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)

size = im_in.shape

# removendo os pontos pretos
for i in range(size[0]):
    for j in range(size[1]):
        if(im_in[i][j] == 0 and im_th[i][j] == 255):
            im_th[i][j] = 0

im_floodfill = im_th.copy()
 
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)


cv2.floodFill(im_floodfill, mask, (0,0), 255)
 
# invertendo o floodfill
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# realizando a interseção com o complemento
im_out = im_th | im_floodfill_inv

# aplicando o preenchimento na imagem colorida
for i in range(size[0]):
    for j in range(size[1]):
        # caso na imagem de saida seja branco e na imagem com buracos pretos: em um buraco
        if(im_out[i][j] == 255 and im_floodfill[i][j] == 0):
            # coletando os valores do pixel antes de entrar no buraco na imagem colorida
            green = img_color[i-1, j-1, 0]
            blue = img_color[i-1, j-1, 1]
            red = img_color[i-1, j-1, 2]
            
            in_hole = True
            
            for k in range(i, size[0]):
                for m in range(j, size[1]):
                    # os buracos na imagem colorida são branco
                    if(img_color[k, m, 0] == 255 and img_color[k, m, 1] == 255 and img_color[k, m, 2] == 255):
                        img_color[k, m, 0] = green
                        img_color[k, m, 1] = blue
                        img_color[k, m, 2] = red
                    elif(img_color[k, m, 0] == green and img_color[k, m, 1] == blue and img_color[k, m, 2] == red):
                        # caso isso for veradde, chegou ao outro lado do buraco
                        in_hole = False
                        break
                # caso tenha saido do buraco por ter chegado do outro lado
                if(not in_hole):
                    break

 
# Mostrando resultados

cv2.imshow("1 - Entrada em cinza", im_in)
cv2.imshow("2 - Thresholded Image", im_th)
cv2.imshow("3 - Floodfilled Image", im_floodfill)
cv2.imshow("4 - Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("5 - Foreground", im_out)
cv2.imshow("6 - Colored", img_color)
cv2.waitKey(0)

# salvando
cv2.imwrite('resultados/problema-2/1 - Gray scale entry.png', im_in)
cv2.imwrite("resultados/problema-2/2 - Thresholded.png", im_th)
cv2.imwrite("resultados/problema-2/3 - Floodfilled Image.png", im_floodfill)
cv2.imwrite("resultados/problema-2/4 - Inverted Floodfilled Image.png", im_floodfill_inv)
cv2.imwrite("resultados/problema-2/5 - Foreground.png", im_out)
cv2.imwrite("resultados/problema-2/6 - Colored.png", img_color)