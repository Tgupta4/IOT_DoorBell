import subprocess
from findFace import *
from uploadToCloudinary import UploadPhoto
from sendMessage import sendSMS
import requests
import time
from flask import Flask, request, Response, jsonify
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    print("request recieved--post")
    filename = 'face/IMG-SERVER-'+str(datetime.datetime.now().microsecond)+'.jpg'
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(filename, img)
    # cv2.imshow("showinf here",img)
    img = cv2.imread(filename)
    [path,username]=Capture_Face_server(img,filename)
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0]),'username':username
                }
    print(filename)
    print(username)
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# route http posts to this method
@app.route('/api/getest', methods=['GET'])
def test22():
    print("request recieved")
    # build a response dict to send back to client
    response = {'message': 'sample received. '}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=47947)
print('*****************************EXIT********************************')
