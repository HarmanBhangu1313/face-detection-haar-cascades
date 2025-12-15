import cv2


face_cascade =cv2.CascadeClassifier('/Users/harmansingh/AI Engineering/Open CV/Basic Open CV/DATA/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade =cv2.CascadeClassifier('/Users/harmansingh/AI Engineering/Open CV/Basic Open CV/DATA/haarcascades/haarcascade_eye.xml')


def face_detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle( frame, (x,y) ,(x+w,y+h), color=[255,255,255],thickness=2)
       
        # TO make faster detection of eye
        roi_gray= gray[ y:y+h, x:x+w]
        roi_frame= frame[ y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle( roi_frame, (ex,ey) ,(ex+ew,ey+eh), color=[0,255,0],thickness=2)
    
    return frame
    

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
    canvas = face_detect(gray,frame)
    cv2.imshow("Face Detection", canvas)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()