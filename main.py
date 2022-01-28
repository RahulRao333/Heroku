# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pickle

from flask import Flask,render_template,request,jsonify
import numpy as np
app=Flask(__name__)
model=pickle.load(open('models.pkl','rb'))


@app.route("/")
def home():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
        if prediction == [0]:
        return render_template('index.html',prediction_text='You are Healthy')
    else:
        return render_template('index.html',prediction_text="You may suffer a Stroke")




  
if __name__ == '__main__':
    app.run(debug=True)
