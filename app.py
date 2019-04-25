import numpy as np
from flask import Flask
from flask import request
from flask import jsonify
from sklearn.externals import joblib
 
app = Flask(__name__)

model = 'model.joblib'
loaded_model = joblib.load(model)
 
@app.route('/predict', methods=['GET','POST'])
def predict():
    data = request.get_json()
    X = data['X']
    X = np.array(list(map(float,X.split(',')))) #str to float
    preds = loaded_model.predict(X.reshape(1,-1))
    return jsonify({'classes': preds.tolist()})

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0') #,debug=True

