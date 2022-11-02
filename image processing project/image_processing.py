import cv2
img1 = cv2.imread("C:/Users/haarv/OneDrive/Desktop/AMS-INDIA/testimg1.jpg")
#edges = cv2.Canny(img1, 100, 200)
#cv2.imwrite("i1.jpg",edges)
#cv2.imshow("edge one is ",img1)
#cv2.waitKey(0)
x = width1 = img1.shape[1]
y = height1 = img1.shape[0]
img2 = cv2.imread("C:/Users/haarv/OneDrive/Desktop/AMS-INDIA/testimg2.jpg")
#edges = cv2.Canny(img2, 100, 200)
#cv2.imwrite("i2.jpg",edges)
x2 = width2 = img2.shape[1]
y2 = height2 = img2.shape[0]

if x == x2 and y == y2:
    cv2.imshow('GIVEN IMAAGES ARE SAME')
    cv2.waitKey(0)
else :
    if x>x2 or y>y2:

        cv2.imshow("THIS IMAGE HAS MORE IMAGES",img1)
        cv2.waitKey(0)
    else:
        cv2.imshow('THIS IMAGE HAS MORE PIXELS',img2)
        ###
        
cv2.destroyAllWindows()  

