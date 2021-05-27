from sys import stderr

from flask import Flask, render_template, request
import pickle
import numpy as np
pip
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template("main_form.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final=[np.array(int_features, dtype=float)]
    prediction=model.predict(final)
    output=round(prediction[0],2)

    if output==1:
        return render_template('yes.html')
    else:
        return render_template('nohd.html')



if __name__ == '__main__':
    app.run(debug=True)
