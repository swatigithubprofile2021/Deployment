from flask import Flask, render_template,request,url_for
import pickle
import numpy as np

model = pickle.load(open('iris_model.pickle','rb'))

app = Flask(__name__)

@app.route('/')
def man():
    pred=''
    return render_template('templates/home.html')

@app.route('/predict',methods = ['POST'])
def home():

    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    #arr = np.array[[data1,data2,data3,data4]]
    pred = model.predict([[data1,data2,data3,data4]])
    return render_template('templates/after.html', data=pred)

if __name__ == "__main__":
    app.run(debug = True)
