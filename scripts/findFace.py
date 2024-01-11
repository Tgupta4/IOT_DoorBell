import cv2
import os
import numpy as np
import datetime
from PIL import Image
from picamera2 import Picamera2, Preview
import time


picam2 = Picamera2()
# camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
# picam2.configure(camera_config)
picam2.start()

cascPath = "scripts/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#recognize face from image
recognizer = cv2.face.LBPHFaceRecognizer_create()

#person name font
font = cv2.FONT_HERSHEY_SIMPLEX

# Create Data set
path = 'scripts/faceData'

# [0,1,2,3,4,5,6]
KNOWN_FACES = ["", "Daisy", "Tanish","md","ad"]
# if os.path.exists("test"):
#     os.remove("test")

COUNT_REF=0

def prepare_training_data(data_folder_path):
    # gets all the directories in training_data folder
    directories = os.listdir(data_folder_path)
    # Defined two lists ones for faces and other labels corresponding to each person
    faces = []
    labels = []
    for directory_name in directories:
        # our subject directories start with letter 'person' so
        # ignore any non-relevant directories if any
        if directory_name.startswith("person"):
            print('I am working on folder:'+directory_name)
            # to get the label corresponding to each image we perform: Replace "person1" with "1"
            label = int(directory_name.replace("person", ""))

            # to build the path of directory containing images like "training-data/s1"
            subject_directory_path = data_folder_path + "/" + directory_name
            # Get images names using os.listdir
            subject_images_names = os.listdir(subject_directory_path)

            for image_name in subject_images_names:
                # to avoid unwanted files
                if not image_name.startswith("."):
                    photo_path = subject_directory_path + "/" + image_name
                    # reading image through cv2
                    PIL_img = Image.open(photo_path).convert('L') # to read image grayscale
                    img_numpy = np.array(PIL_img,'uint8')
                    # cv2.imshow("title",img_numpy)
                    
                    # display an image window to show the image
                    
                    # detect face
                    faces_coordinates = faceCascade.detectMultiScale(img_numpy)
                    print(str(len(faces_coordinates))+"--"+photo_path)
                    # if len(faces_coordinates) == 1:
                    # cv2.imshow("Training on image...", img_numpy)
                    for (x,y,w,h) in faces_coordinates:
                        print('..Processed Image..'+photo_path)
                        faces.append(img_numpy[y:y+h,x:x+w])
                        labels.append(label)
                    # recognizer.update(faces, np.array(labels))
                        cv2.rectangle(img_numpy, (x, y), (x+w, y+h), (255, 0, 0), 10)
                        # cv2.imshow("Training on image...", img_numpy)
                        global COUNT_REF
                        COUNT_REF=COUNT_REF+1
                        if not os.path.exists("test"):
                            os.makedirs("test")
                        cv2.imwrite("test/image_"+str(COUNT_REF)+image_name,img_numpy)
                        cv2.waitKey(10)
                        # k = cv2.waitKey(1000) & 0xff
                        # if k == 27:
                            # exit() 
    return faces, labels


def find_Face_Name(img):
    # initiate id counter
    id = 0
    canSave = False
    # image in laptops is flipped automatically
    img = cv2.flip(img, 1, 0)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces__coordinaes = faceCascade.detectMultiScale(
        gray_image,     
        scaleFactor=1.3,
        minNeighbors=3,     
        minSize=(30, 30)
    )
    
    for(x, y, w, h) in faces__coordinaes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray_image[y:y+h, x:x+w])
        canSave = True
        # If confidence is less them 100 ==> "0" : perfect match 
        print(confidence)
        
        if (confidence < 60):
            id = KNOWN_FACES[id]
            FaceAnswer['yes']['name'] = id
            FaceAnswer['yes']['len'] += 1
            confidence = " {0}%".format(round(100-confidence))

        else:
            FaceAnswer['not'] += 1
            id = "I Don't Know You"
            confidence = " {0}%".format(round(100-confidence))
        print(confidence + "::"+ id)
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

    window_name='Capturing Image::'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow(window_name, img)

    return canSave

# # Preperation Start ####

# print("Preparing data...")
faces, labels = prepare_training_data(path)
print("Data prepared")
# create our LBPH face recognizer
recognizer.train(faces, np.array(labels))
recognizer.write('scripts/trainer/trainer.yml') 
print("Total faces: & labels ", len(faces),len(labels))
# Preperation Done ####


print("Traing modal done...")
FaceAnswer = {
    "not": 0,
    "yes": {
        "name": "",
        "len": 0
    }
}

max_conf=0
def Capture_Face():
    # Initialize real-time video capture
    filename = 'face\IMG-'+str(datetime.datetime.now().microsecond)+'.jpg'
    # cam = cv2.VideoCapture(0)
    # cam.set(3, 640)  # set video-width
    # cam.set(4, 480)  # set video-height
 
    
    count_photo_before_exit = 0
    FaceAnswer['not'] = 0
    FaceAnswer['yes']['len'] = 0
    notSaved = True
    while True:
        count_photo_before_exit += 1
        if(count_photo_before_exit > 100):
            break
        print("A11")
        # # picam2.start_preview(Preview.QTGL)
        # # print("A12") 
        # # picam2.start()
        # # print("A13") 
        # # time.sleep(2)
        # # print("A14")
        # # fileLocation="check.jpg"
        # # print("A15")
        # # picam2.capture_file(fileLocation)
        # # print("A16")
        # # picam2.stop_preview()
        # # print("A17")
        # # picam2.stop()
        # # print("A18")
        # # time.sleep(2)
        # # print("Image is captured")
        # # exit()
        # img = cv2.imread(fileLocation)
        img = picam2.capture_array()
        # img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # ret, img = cam.read()
        print("Below image form camera")
        # cv2.imwrite(filename, img)
        # k = cv2.waitKey(50) & 0xff

        # exit()
        # print(img)
        if(img is None):
            print("Unable to read image form camera")
            exit()
        #     break
        canSave = find_Face_Name(img) or False
        if(canSave):
            notSaved = False
            cv2.imwrite(filename, img)
        k = cv2.waitKey(50) & 0xff
        if k == 27:         # Press 'ESC' for exiting the program
            break
    print(">> is-saved",not(notSaved))
    if(notSaved):
        im = picam2.capture_array()
        img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        # # ret, img = cam.read()
        # picam2.start_preview(Preview.QTGL)
        # picam2.start()
        # time.sleep(2)
        # fileLocation="check.jpg"
        # picam2.capture_file(fileLocation)
        # img = cv2.imread(fileLocation)
        if (img is None):
            print("Unable to read image form camera")
        else: 
            cv2.imwrite(filename, img)
    print("I am Cleaning up now",filename)
    # cam.release()
    cv2.destroyAllWindows()
    if(FaceAnswer['not'] > FaceAnswer['yes']['len']):
        return [filename, False]
    return [filename, FaceAnswer['yes']['name']]