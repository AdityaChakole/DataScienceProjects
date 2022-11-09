import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Calculate',methods=['POST'])
def predict():
      first_input = request.form['number1']  
      second_input = request.form['number2']
    '''
  



    return render_template('index.html', prediction_text='Ticket have 81% chances that it will fall under {} Category'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
