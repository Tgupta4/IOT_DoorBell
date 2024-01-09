# # //https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348
import numpy as np
import cv2
import os
# from PIL import Image
# known_faces = ["", "Daisy", "Brother","Mumma","4"]
# #person name font
# font = cv2.FONT_HERSHEY_SIMPLEX
# #
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
FACE_DATA_PATH="faceData/person2/"
# # Create Data set
# path = 'faceData'
# # gets all the directories in training_data folder
# directories = os.listdir(path)


# # Dataset ends here

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
count = 0
isExist = os.path.exists(FACE_DATA_PATH)
if isExist:
    print("Folder Exists, Please delete the forder first--["+FACE_DATA_PATH+"]")
    exit()
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(FACE_DATA_PATH)
   print("The new directory is created!")


while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces__ = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.1,
        minNeighbors=6,     
        minSize=(25, 25)
    )
    for (x,y,w,h) in faces__:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        count += 1
        print("Capture Image ", count)
        folder_name = FACE_DATA_PATH
        cv2.imwrite( "./"+folder_name+"User"+'.'+str(count)+".jpg", gray)
    cv2.imshow('capture-image',frame)

    k = cv2.waitKey(150) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    elif count >= 30: # Take 30 face sample and stop video
        break
cap.release()
cv2.destroyAllWindows()