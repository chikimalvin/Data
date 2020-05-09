from flask import Flask
import time

app = Flask(__name__)

@app.route('/hora')
def showhora():
         time.strftime("%c")
         return {"mesage": "Año : " + time.strftime("%Y") + " Mes : "+ time.strftime("%m") + " Día : " + time.strftime("%d") 
                 + " Hora : " + time.strftime("%H") + " Minuto : " + time.strftime("%M") 
                 + " Segundos : " + time.strftime("%S")}


if __name__ == '__main__':
    app.run()
    