# Employee Salary Prediction System

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load and preprocess dataset
df = pd.read_csv(r"C:\Users\Sonica K\OneDrive\Documents\Desktop\Employee_Salary_Prediction_System\salary_data.csv")
df.fillna(0, inplace=True)
df["Gender"] = df["Gender"].replace({"Male": "M", "Female": "F"})

# Encode categorical features
encoder = {}
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoder[col] = le

# Separate features and target variable
x = df.drop("Salary", axis=1)
y = df["Salary"]

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=20,random_state=42)
model.fit(x_train, y_train)

# Evaluate model performance
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R² Score:", r2*100)

# Save trained model and encoders
with open("salary_model.pkl", "wb") as file:
    pickle.dump((model, encoder), file)

print("Model saved successfully.")

# Load saved model
with open("salary_model.pkl", "rb") as file:
    loaded_model, encoder = pickle.load(file)

print("Model loaded successfully.")

# Get user input
print("\nEnter Employee Details:")
age = int(input("Age: "))
gender = input("Gender (M/F): ")
education = input("Education Level: ")
job = input("Job Title: ")
years = int(input("Years of Experience: "))

# Convert categorical inputs into machine-readable format
gender = encoder["Gender"].transform([gender])[0]
education = encoder["Education Level"].transform([education])[0]
job = encoder["Job Title"].transform([job])[0]

# Create input data for prediction
new_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Education Level": [education],
    "Job Title": [job],
    "Years of Experience": [years]
})

# Predict salary
predicted_salary = loaded_model.predict(new_data)
print("\nPredicted Salary: ",predicted_salary[0])