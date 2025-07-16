from flask import Flask, request, render_template
import pandas as pd
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('insurance_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the form submission and returns the prediction."""
    if request.method == 'POST':
        # Get the form data
        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        # Create a DataFrame from the input data
        input_data = {
            'age': [age],
            'sex': [sex],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],
            'region': [region]
        }
        input_df = pd.DataFrame(input_data)

        # Preprocessing
        input_df['sex'] = input_df['sex'].map({'female': 0, 'male': 1})
        input_df['smoker'] = input_df['smoker'].map({'no': 0, 'yes': 1})
        
        region_dummies = pd.get_dummies(input_df['region'], drop_first=True, dtype=int)
        input_df = pd.concat([input_df.drop('region', axis=1), region_dummies], axis=1)

        training_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 
                            'region_northwest', 'region_southeast', 'region_southwest']
        input_df = input_df.reindex(columns=training_columns, fill_value=0)

        # features Scaling
        scaled_features = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(scaled_features)
        
        # Format the prediction for display
        output = f"${prediction[0]:,.2f}"

        return render_template('index.html', prediction_text=f'Predicted Insurance Charge: {output}')

if __name__ == "__main__":
    app.run(debug=True)