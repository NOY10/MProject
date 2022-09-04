import cv2

trained_eye_data=cv2.CascadeClassifier("haarcascade_eye.xml")
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
trained_smile_data=cv2.CascadeClassifier("haarcascade_smile.xml")

# img=cv2.imread('try.png')

# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

webcam =cv2.VideoCapture(0)

while True:

    FrameS, Frame= webcam.read()
    
    grayscaled_img = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    
    face = trained_face_data.detectMultiScale(grayscaled_img)
    
    for (x,y,w,h) in face:
        cv2.rectangle(Frame,(x,y),(x+w, y+h),(0,255,0), 2)
        face_coordinates=Frame[y:y+h,x:x+w]
        
        grayscaled_img = cv2.cvtColor(face_coordinates, cv2.COLOR_BGR2GRAY)
       
        # eye_coordinates = trained_eye_data.detectMultiScale(grayscaled_img)
        smile_coordinates = trained_smile_data.detectMultiScale(grayscaled_img,1.7,20)
        # for (x_,y_,w_,h_) in eye_coordinates:
            
        #     cv2.rectangle(face_coordinates,(x_,y_),(x_+w_, y_+h_),(0,255,0), 2)

        for (x_,y_,w_,h_) in smile_coordinates:
            
            cv2.rectangle(face_coordinates,(x_,y_),(x_+w_, y_+h_),(0,255,0), 2)

    cv2.imshow('Face', Frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        False

print("helo")