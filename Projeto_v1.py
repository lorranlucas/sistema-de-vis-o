
import cv2
from cv2 import Canny

class Projeto:
    
    def  __init__(self,x1,x2,x3,x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        Projeto.inter(self)


    def inter(self,p1 = 0,p2 = 0):

        y1 = 10
        y2 = 400
        y3 = 324
        y4 = 324

        d = (self.x1-self.x2)*(y3-y4)-(y1-y2)*(self.x3-self.x4)

        self.p1 = int(((self.x1*y2 - y1*self.x2)*(self.x3 - self.x4) - (
            self.x1 - self.x2)*(self.x3*y4 - y3*self.x4))/d)

        self.p2 = int(((self.x1*y2 - y1*self.x2)*(y3 - y4) - (y1 - y2)*(
            self.x3*y4 - y3*self.x4))/d)

        Projeto.todo(self)

    def todo(self):

        y1 = 10
        y2 = 400
        y3 = 324
        y4 = 324

        img = cv2.imread('imagem/3.png',1) #Foto NOK
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

        cv2.line(thresh1,[self.x1,y1],[self.x2,y2],[20,60,255],2)
        cv2.line(thresh1,[self.x3,y3],[self.x4,y4],[20,60,255],2)
        print(self.p1,self.p2)
        cv2.circle(thresh1,[self.p1,self.p2],3,(2,255,255),3)

        print(centroid[0] - self.p1 ,self.p2 - centroid[1])

        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (40,40)
        fontScale              = 1
        fontColor              = (255,255,255)
        thickness              = 1
        lineType               = 2

        soma_x = (centroid[0] - self.p1)-116
        soma_y = (self.p2 - centroid[1])-127

        if soma_x  == 0 and soma_y == 0:
            cv2.putText(thresh1,f'OK',   
    (300,360), 
    font, 
    1,
    (0,255,0),
    thickness)
        else:
            cv2.putText(thresh1,f'NOK',   
    (300,360), 
    font, 
    1,
    (0,0,255),
    thickness)



        cv2.putText(thresh1,f'Distancia X: {soma_x}',   
    (40,25), 
    font, 
    1,
    fontColor,
    thickness)

        cv2.putText(thresh1,f'Distancia Y: {soma_y}',   
    (40,55), 
    font, 
    1,
    fontColor,
    thickness)

       

        cv2.imshow('image',img)
        cv2.imshow('image1',thresh1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        



def main():
    casa = []
    casa.append(Projeto(40,90,10,400)) #x1 = 40 // x2 = 90
    


if __name__ == '__main__':
   main()
    