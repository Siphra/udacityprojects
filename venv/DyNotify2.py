# DyNotify Internship Task Assessment

#Library block
from functools import wraps
from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api, reqparse
import os

#Initialize API for use
app = Flask(__name__)
api = Api(app)

#API Key for Authentication
keys = ['KEY1FORTEST','KEY2FORTEST']

# create a decorator for flask to wrap the function
def app_keytest(view_function):
    @wraps(view_function)
    def decorate_function(*args,**kwargs):
        if request.args.get('APIKey') in keys:
            return view_function(*args,**kwargs)
        else:
            abort(401)
    return decorate_function


# API call for functioning:
@app.route('/imagecomp/', methods = ['GET'])
@app_keytest
def imagecomps():
    #static images for testing code:
    image = request.args.get('image')
    image2 = request.args.get('image2')
    with open(image, 'rb') as img1, open(image2, 'rb') as img2:
        file_bin = img1.read()
        bit_arry = bytearray(file_bin)
        file_bin2 = img2.read()
        bit_arry2 = bytearray(file_bin2)

        # compare the file sizes for iteration

    # if os.path.getsize(image) >= os.path.getsize(image2):
    if len(bit_arry) >= len(bit_arry2):
        max = len(bit_arry)
        min = len(bit_arry2)
    else:
        min = len(bit_arry)
        max = len(bit_arry2)

    counter = 0  # initialize counter for iteration
    bit_arry_bool = []  # initialize empty bit array for boolean construct
    while counter < min:
        if bit_arry[counter] == bit_arry2[counter]:
            bit_arry_bool.append(1)
        else:
            bit_arry_bool.append(0)
        counter += 1

    similarity = 100 * sum(bit_arry_bool) / max
    return jsonify({'% Similar' : similarity })

if __name__ == '__main__':
    app.run()