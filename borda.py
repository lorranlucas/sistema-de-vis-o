import cv2
from cv2 import Canny
 

img = cv2.imread('imagem/3.png',1)
img = cv2.resize(img, [400,400])
ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

edged = cv2.Canny(thresh1, 40, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, 255, 3)

    # encontrar o maior contorno
c = max(contours, key = cv2.contourArea)

print(len(c))


x,y,w,h = cv2.boundingRect(c)
print(cv2.boundingRect(c))

    # Desenhar o maior contorno
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

centroid = [int((x+(x+w))/2),int((y+(y+h))/2)]
print(centroid)
cv2.circle(img,centroid,3,(2,255,255),3)




cv2.imshow('image',img)
cv2.imshow('image1',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()