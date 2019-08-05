import cv2

cap=cv2.VideoCapture(0) #0 is for default webcam
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:

    ret,frame=cap.read() #ret is a bool value that tells whether the image is captured or not
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        continue

    faces=face_cascade.detectMultiScale(frame,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Video Frame",frame)
    #cv2.imshow("Gray Frame",gray_frame)

    #wait for user input q then you will stop the loop
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    
        
                                             
