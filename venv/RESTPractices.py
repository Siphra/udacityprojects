from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)           # creates an app object from Flask

@app.route("/")
def hello():
    return "Hello World"

empDB = [
    {
        'id':'101',
        'name':'Saravanan S',
        'title':'Tech lead'
    },
    {
        'id':'201',
        'name':'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
]

@app.route('/empdb/employee', methods = ['GET'])   # gets call
def getAllEmp():
    print('all clear')
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>', methods = ['GET'])
def getEmp(empId):
    usr = [emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp': usr})

@app.route('/empdb/employee/<empId>', methods = ['PUT'])  # puts update
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId)]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'title' in request.json :
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})


@app.route('/empdb/employee', methods = ['POST'])   # posts create new data
def createEmp():
    dat = {
        'id' : request.json['id'],
        'name': request.json['name'],
        'title': request.json['title']
    }
#@app.route('/imagecomp', methods = ['GET'])
#def imagecomp1():
    #static images for testing code:
#    image = (r'I:\Python\PycharmProjects\udacityproject1\venv\testimg1.jpg')
 #   image2 = (r'I:\Python\PycharmProjects\udacityproject1\venv\testimg2.jpg')
  #  with open(image, 'rb') as img1, open(image2, 'rb') as img2:
   #     file_bin = img1.read()
   #     bit_arry = bytearray(file_bin)
    #    file_bin2 = img2.read()
     #   bit_arry2 = bytearray(file_bin2)

        # compare the file sizes for iteration

    # if os.path.getsize(image) >= os.path.getsize(image2):
#    if len(bit_arry) >= len(bit_arry2):
 #       max = len(bit_arry)
  #      min = len(bit_arry2)
   # else:
    ##    min = len(bit_arry)
     #   max = len(bit_arry2)

#    counter = 0  # initialize counter for iteration
 #   bit_arry_bool = []  # initialize empty bit array for boolean construct
  #  while counter < min:
   #     if bit_arry[counter] == bit_arry2[counter]:
    #        bit_arry_bool.append(1)
     #   else:
      #      bit_arry_bool.append(0)
       # counter += 1

   # similarity = 100 * sum(bit_arry_bool) / max
    #return jsonify({'% Similar' : similarity })


# The below code works for comparison of files commented out only for this run:
'''
# create a decorator for flask to wrap the function
def app_keytest(view_function):
    @wraps(view_function)
    def decorate_function(*args,**kwargs):
        if request.args.get('APIKey') and request.args.get('APIKey') == 'KEY1FORTEST':
            return view_function(*args,**kwargs)
        else:
            abort(401)
    return decorate_function

with open(image, 'rb') as image, open(image2, 'rb') as image2:
    file_bin = image.read()
    bit_arry = bytearray(file_bin)
    file_bin2 = image2.read()
    bit_arry2 = bytearray(file_bin2)

    # compare the file sizes for iteration

#if os.path.getsize(image) >= os.path.getsize(image2):
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

similarity = sum(bit_arry_bool) / max
print(similarity)

@app.route('/imagecomp/', methods = ['GET'])
def imagecomp():
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

'''
if __name__ == "__main__":
    app.run()