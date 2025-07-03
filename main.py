# main.py (Final Version with CORS)
import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware # <--- IMPORT THIS

# 1. Create the FastAPI app object
app = FastAPI()


# #####################################################################
# ## NEW SECTION: Add CORS Middleware #################################
# #####################################################################

# Define the origins that are allowed to connect to your API
# Using ["*"] allows all origins, which is fine for local development.
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# #####################################################################


# 2. Load the trained model and scaler
model = joblib.load('insurance_model.pkl')
scaler = joblib.load('scaler.pkl')

# 3. Define the input data structure
class InsuranceData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

# 4. Create the prediction endpoint
@app.post('/predict')
def predict_charge(data: InsuranceData):
    # (The rest of your prediction function stays exactly the same)
    
    input_df = pd.DataFrame([data.dict()])
    
    # Preprocessing
    input_df['sex'] = input_df['sex'].map({'female': 0, 'male': 1})
    input_df['smoker'] = input_df['smoker'].map({'no': 0, 'yes': 1})
    region_dummies = pd.get_dummies(input_df['region'], drop_first=True, dtype=int)
    input_df = pd.concat([input_df, region_dummies], axis=1)
    input_df.drop('region', axis=1, inplace=True)
    
    training_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 
                        'region_northwest', 'region_southeast', 'region_southwest']
                        
    input_df = input_df.reindex(columns=training_columns, fill_value=0)
    
    scaled_features = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_features)

    return {'predicted_charge': prediction[0]}