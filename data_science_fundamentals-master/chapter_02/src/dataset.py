from flask import Flask

#from pandas import read_csv
import csv
#import numpy
from flask import jsonify


app = Flask(__name__)

@app.route('/json_from_list')
def show_list():
        filename = "/home/juanfe/Escritorio/Data/data_science_fundamentals-master/chapter_02/uploads/iris.csv"
        #names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
        #data = read_csv(filename, names=names)
        #return jsonify(data.shape)
        raw_data = open(filename, 'r')
        reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
        x = list(reader)
        return jsonify(x)
if __name__ == '__main__':
    app.run()