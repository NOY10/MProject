import cv2

trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img=cv2.imread('try.png')

# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

webcam =cv2.VideoCapture(0)

while True:

    FrameS, Frame= webcam.read()
    grayscaled_img = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(Frame,(x,y),(x+w, y+h),(0,255,0), 2) 

    cv2.imshow('Face', Frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        False

print("helo")
