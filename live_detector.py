import cv2
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detector(image,size=1):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(image,1.3,5)
    if faces is ():
        return image

    for x,y,w,h in faces:
        x=x-50
        w=w+50
        y=y-50
        h=h+50
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,222,222),4)
        color=image[y:y+h,x:x+w]
        eyes = eye_classifier.detectMultiScale(color, 1.3, 5)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(color, (ex, ey), (ex + ew, ey + eh), (0, 127, 222), 4)
        #color=cv2.flip(color,1)
        return color
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("displaying...",face_detector(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
