from flask import Flask, render_template, request
from finalproject import soil , crops , fertilizers
import pandas as pd
import joblib



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the trained models
    crop_model = joblib.load('crop_model.pkl')
    fertilizer_model = joblib.load('fertilizer_model.pkl')

    # Get user input values
    soil_color = request.form['soil_color']
    nitogen = request.form['nitrogen']
    phosphorus = request.form['phosphorus']
    potassium = request.form['potassium']
    pH = request.form['pH']
    temperature = request.form['temperature']

    # Get other input fields: Nitrogen, Phosphorus, Potassium, pH, Temperature

    # Prepare user input as a DataFrame
    user_input = pd.DataFrame({
        'Soil_color': [soil_color],
        'Nitrogen': [nitogen],
        'Phosphorus': [phosphorus],
        'Potassium': [potassium],
        'pH': [pH],
        'Temperature': [temperature]
    })

    # Make predictions
    user_input['Soil_color'] = soil(user_input['Soil_color'][0])
    predicted_crop = crop_model.predict(user_input)[0]
    user_input['Crop'] = [predicted_crop]
    predicted_fertilizer = fertilizer_model.predict(user_input)[0]
    predicted_crop = crops(predicted_crop)
    predicted_fertilizer = fertilizers(predicted_fertilizer)

    return render_template('index.html', crop=predicted_crop, fertilizer=predicted_fertilizer)

if __name__ == '__main__':
    app.run(debug=True)
