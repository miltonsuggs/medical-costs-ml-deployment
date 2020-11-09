import numpy
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('predictor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
#     For rendering results on HTML GUI
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='The predicted medical cost is $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)