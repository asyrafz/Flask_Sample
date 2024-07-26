
import cv2
import base64
import io
from PIL import Image
import numpy as np
from flask_socketio import emit, SocketIO
from flask import Flask, render_template


import torch
from ultralytics import YOLO



app = Flask(__name__, template_folder="templates")
sio = SocketIO(app)

@sio.on('image')

def image(data_image):

    sbuf = io.StringIO()

    sbuf.write(data_image)

    b = io.BytesIO(base64.b64decode(data_image))

    pimg = Image.open(b)


    frame_batch = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


    imgencode = cv2.imencode('.jpg', frame)[1]


    stringData = base64.b64encode(imgencode).decode('utf-8')

    b64_src = 'data:image/jpeg;base64,'

    stringData = b64_src + stringData

    emit('response_back', stringData)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    	sio.run(app, debug=True, port=5003)
