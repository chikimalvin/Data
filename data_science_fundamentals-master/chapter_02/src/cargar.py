from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_CAT = "/home/juanfe/Escritorio/Data/data_science_fundamentals-master/chapter_02/uploads/cat"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
#Define the path to the upload folder
app.config['UPLOAD_CAT'] = UPLOAD_CAT
#Specifies the maximum size (in bytes) of the files to be uploaded
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

UPLOAD_DOG = "/home/juanfe/Escritorio/Data/data_science_fundamentals-master/chapter_02/uploads/dog"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
#Define the path to the upload folder
app.config['UPLOAD_DOG'] = UPLOAD_DOG
#Specifies the maximum size (in bytes) of the files to be uploaded
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        if request.form.get('opciones') == '1':

                if 'filec' not in request.files:
                    return 'No file part'
                    
                file = request.files['filec']
        
                if file.filename == '':
                    return 'No selected file'
                
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_CAT'], filename))
                    return 'Gato subido correctamente'

               
        elif request.form.get('opciones') == '2':
            
                if 'filec' not in request.files:
                    return 'No file part'
                    
                file = request.files['filec']
        
                if file.filename == '':
                    return 'No selected file'
                
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_DOG'], filename))
                    return 'Perro subido correctamente'
        
        else:
                      return 'No allowed extension'
if __name__ == '__main__':
    app.run()