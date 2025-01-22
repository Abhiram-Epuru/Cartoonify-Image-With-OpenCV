import cv2
print('imported')

img=cv2.imread('Mahesh-Babu-4.jpg')

cv2.imshow("Output",img)
gratIMg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blrImg=cv2.medianBlur(gratIMg,7)
edges = cv2.adaptiveThreshold(gratIMg,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color=cv2.bilateralFilter(img,7,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("output2",gratIMg)
cv2.imshow("output3",blrImg)


cv2.imshow("output4",edges)
cv2.imshow("output5",cartoon)





cv2.waitKey(0)
cv2.destroyAllWindows()