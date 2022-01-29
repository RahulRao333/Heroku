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
    int_features=[float(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=prediction
    return render_template('index.html',prediction_text='[0] represents Healthy ,[1] represents possibility of stroke {}'.format(output))




  
if __name__ == '__main__':
    app.run(debug=True)
