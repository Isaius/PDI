import cv2

img = cv2.imread("morfologia.png")
cv2.imshow("Imagem original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = cv2.dilate(img, None, iterations=1)
cv2.imshow("Imagem dilatada...", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.erode(img1, None, iterations=1)
cv2.imshow("... depois erodida", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output\problema-1.png", img2)