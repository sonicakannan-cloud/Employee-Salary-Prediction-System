import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"C:\Users\Sonica K\OneDrive\Documents\Desktop\Employee_Salary_Prediction_System\salary_data.csv")

# Handle Missing Values
df.fillna(0, inplace=True)

# Standardize Gender Values
df["Gender"] = df["Gender"].replace({
    "Male": "M",
    "Female": "F"
})

# Dataset Information

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Salary Distribution

plt.figure(figsize=(8,5))

plt.hist(df["Salary"],
         bins=20,
         edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()

# Gender Distribution


plt.figure(figsize=(6,6))

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")
plt.ylabel("")

plt.tight_layout()
plt.show()

# Education Level Distribution

plt.figure(figsize=(8,5))

df["Education Level"].value_counts().plot(
    kind="bar"
)

plt.title("Education Level Distribution")
plt.xlabel("Education Level")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Top 10 Job Titles

plt.figure(figsize=(10,6))

df["Job Title"].value_counts().head(10).plot(
    kind="bar"
)

plt.title("Top 10 Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Salary vs Years of Experience

plt.figure(figsize=(8,5))

plt.scatter(
    df["Years of Experience"],
    df["Salary"]
)

plt.title("Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()



print("\nData Visualization Completed Successfully!")
