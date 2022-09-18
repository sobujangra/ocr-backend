from cgitb import text
import string
from unittest import result
import requests
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import json
import base64
import imageio
import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

ip_BE = "192.168.46.155"
ip_front = "http://192.168.46.245:3000/api/hello"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/files'


# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Upload File")
data = {"result": ""}


@app.route('/', methods=['GET'])
def index():

    req = requests.get(ip_front)
    result = json.loads(req.text)

    # original code \\
    image_64_encode = str(result["base64"])
    print(image_64_encode)
    image_64_decode = base64.b64decode(image_64_encode)

    # # create a writable image and write the decoding result
    # image_result = open('temp_decode.jpg', 'wb')
    # image_result.write(image_64_decode)
    # decodeit = open('temp_decode.jpg','rb')
    # decodeit.write(base64.b64decode((result)))

    # form = 'Income.jpeg'
    # form = req. `  # Decoded Image Link`
    # if form.validate_on_submit():
    #     file = form.file.data  # First grab the file
    #     file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
    #               app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
    #     return "File has been uploaded."

    # img_path = 'temp_decode.jpg'

    result = recognize_text(image_64_decode)

    print(result)

    data['result'] = result[0]
    return render_template('index.html')


def recognize_text(img_path):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path, detail=0)


@app.route('/home', methods=['GET'])
def returnJson():
    return json.dumps(data, indent=4)


if __name__ == '__main__':
    app.run(host=ip_BE, port=5000, debug=True, threaded=False)
