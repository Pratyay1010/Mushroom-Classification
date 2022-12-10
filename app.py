from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model('model.h5')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    temp = request.form.get('Mushroom_Data')
    Mushroom_Data = []
    for i in temp.split(','):
        Mushroom_Data.append(int(i))
   
    prediction = model.predict([[Mushroom_Data]])

    if prediction[0][0]==True:
        return render_template('index.html', prediction_text="Mushroom is Poisonous")
    else:
        return render_template('index.html', prediction_text="Mushroom is Not Poisonous")


if __name__ == '__main__':
    app.run(debug=True)
