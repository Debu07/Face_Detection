import cv2

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image=cv2.imread("barney.jpg",0)
cv2.imshow("find face in this picture",image)
cv2.waitKey(0)
faces=face_classifier.detectMultiScale(image,1.3,5)
if faces is ():
    print("no face found")
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,222,222),4)
    cv2.imshow("face found",image)
    cv2.waitKey(0)
cv2.destroyAllWindows()