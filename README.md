# Health Insurance Cost Prediction

This project aims to predict the cost of health insurance for individuals based on several personal and health-related factors. The prediction is made using a machine learning model trained on a dataset of insurance information. The final model is deployed as a user-friendly web application using Streamlit.

## 📈 Project Overview
The data is imported from https://www.kaggle.com/datasets/mirichoi0218/insurance
The core of this project is to analyze how different attributes of an individual correlate with their health insurance charges. The key findings from the exploratory data analysis are:

-   **Age and Charges:** There is a clear positive correlation between age and insurance charges. As age increases, charges tend to go up.
-   **BMI and Charges:** Body Mass Index (BMI) also shows a positive relationship with charges, especially for individuals with a BMI over 30 (classified as obese).
-   **Smoker Status:** This is the most significant factor. Smokers consistently face substantially higher insurance charges compared to non-smokers across all other categories.


## 🤖 Models & Performance

Several regression models were trained and evaluated. The **Random Forest Regressor** provided the best initial performance, and after hyperparameter tuning, its performance improved further.

| Model                       | R-squared (R²) | Root Mean Squared Error (RMSE) |
| --------------------------- | :------------: | :----------------------------: |
| Linear Regression           |     0.7566     |           $5801.24            |
| SGD Regressor               |     0.7568     |           $5799.00            |
| Random Forest (Initial)     |     0.8733     |           $4185.38            |
| XGBoost Regressor           |     0.8528     |           $4511.34            |
| **Random Forest (Tuned)** |   **0.8901** |         **$3898.03** |

The tuned Random Forest model was selected as the final model for deployment due to its superior performance.

## 📂 Repository Contents

-   `EDA-ML.ipynb`: The Jupyter Notebook containing all data analysis, feature engineering, model training, and evaluation steps.
-   `app.py`: The Python script for the Streamlit web application.
-   `insurance_model.pkl`: The saved (pickled) file of the trained and tuned Random Forest model.
-   `scaler.pkl`: The saved file for the `StandardScaler` used on the training data.
-   `requirements.txt`: A list of all Python libraries required to run the project.
-   `README.md`: This file, explaining the project.
