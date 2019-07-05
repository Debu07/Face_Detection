import cv2
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('haarcascade_eye.xml')
image=cv2.imread("barney.jpg",0)
cv2.imshow("find face and Eyes in this picture",image)
cv2.waitKey(0)
faces=face_classifier.detectMultiScale(image,1.3,5)
if faces is ():
    print("Nothing  found")
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,222,222),4)
    cv2.imshow("Face found",image)
    cv2.waitKey(0)
    color=image[y:y+h,x:x+w]
    eyes = eye_classifier.detectMultiScale(color, 1.3, 5)
    for ex,ey,ew,eh in eyes:
        cv2.rectangle(color, (ex, ey), (ex + ew, ey + eh), (0, 127, 222), 4)
        cv2.imshow("Eyes found", image)
        cv2.waitKey(0)

cv2.destroyAllWindows()