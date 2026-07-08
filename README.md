# 💼 Employee Salary Prediction System

## 📌 Project Overview

The **Employee Salary Prediction System** is a Machine Learning-based web application developed using **Python** and **Streamlit** to predict employee salaries based on personal and professional details.

The application enables users to:

- Register employee details
- Predict employee salary using Machine Learning
- View employee report
- Download employee report

The project was initially developed using the **Random Forest Classifier** and later enhanced by replacing it with the **Random Forest Regressor**, significantly improving the prediction performance to an **R² Score of 92.67%**.

---

# 🚀 Features

- 📝 Employee Registration
- 💰 Salary Prediction using Machine Learning
- 📋 Employee Report Generation
- ⬇ Download Employee Report
- 📊 Exploratory Data Analysis (EDA)
- 📈 Data Visualization using Matplotlib
- 🌐 Multi-page Streamlit Web Application
- 💻 User-friendly Interface

---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pickle

---

# 🤖 Machine Learning Model

## Algorithm Used

- Random Forest Regressor

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Model Performance

| Metric | Performance |
|----------|------------|
| R² Score | **92.67%** |

---

# 📊 Data Visualization

A separate **data_visualization.py** file is included to perform Exploratory Data Analysis (EDA) on the employee salary dataset.

The following visualizations are generated:

## 📈 Salary Distribution

![Salary Distribution](screenshot/Visualization/salary_distribution.png)

---

## 👥 Gender Distribution

![Gender Distribution](screenshot/Visualization/gender_distribution.png)

---

## 🎓 Education Level Distribution

![Education Level Distribution](screenshot/Visualization/education_distribution.png)

---

## 💼 Top 10 Job Title Distribution

![Top Job Title Distribution](screenshot/Visualization/top_job_title_distribution.png)

---

## 📊 Salary vs Years of Experience

![Salary vs Experience](screenshot/Visualization/salary_vs_experience.png)

---

# 🔄 Project Workflow

## Employee Salary Prediction Workflow

![Employee Salary Prediction Workflow](screenshot/Workflow/employee_salary_prediction_workflow.PNG)

---

## Streamlit Web Application Workflow

![Streamlit Web Application Workflow](screenshot/Workflow/streamlit_web_application_workflow.PNG)

---

# 📷 Application Screenshots

## 📝 Registration Form

![Registration Form](screenshot/registration_form.png)

---

## 💰 Salary Prediction Page

![Salary Prediction](screenshot/salary_prediction_page.png)

---

## 📋 Employee Report

![Employee Report](screenshot/employee_Report_Page.png)

---

## ⬇ Download Employee Report

![Download Employee Report](screenshot/download_report.pdf)

---

## 📊 Model Performance

![Model Performance](screenshot/model_performance.png)

---

# 📁 Project Structure

```text
Employee-Salary-Prediction-System/
│
├── home.py
├── salary_model_training.py
├── data_visualization.py
├── salary_data.csv
├── salary_model.pkl
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Salary_Prediction.py
│   └── 2_Employee_Report.py
│
├── screenshot/
│   ├── registration_form.png
│   ├── salary_prediction_page.png
│   ├── employee_report.png
│   ├── download_report.png
│   ├── model_performance.png
│   │
│   ├── Visualization/
│   │   ├── salary_distribution.png
│   │   ├── gender_distribution.png
│   │   ├── education_distribution.png
│   │   ├── top_job_title_distribution.png
│   │   └── salary_vs_experience.png
│   │
│   └── workflow/
│       ├── employee_salary_prediction_workflow.png
│       └── streamlit_web_application_workflow.png
```

---

# 📋 Prerequisites

Before running the project, ensure you have:

- Python 3.10 or later
- pip
- Git (optional)

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/sonicakannan-cloud/Employee-Salary-Prediction-System.git
```

### Navigate to the project folder

```bash
cd Employee-Salary-Prediction-System
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run home.py
```

---

# 🌐 Live Demo

After deploying the project using **Streamlit Community Cloud**, update this section with your live application link.

Example:

```text
https://employee-salary-prediction.streamlit.app
```

---

# 📈 Project Evolution

## 🔹 Version 1 (Initial Implementation)

- Developed the Employee Salary Prediction System.
- Implemented using **Random Forest Classifier**.
- Achieved **42.67% Accuracy**.
- Built the initial salary prediction pipeline.

---

## 🔹 Version 2 (Enhanced Implementation)

- Replaced **Random Forest Classifier** with **Random Forest Regressor**.
- Achieved an **R² Score of 92.67%**.
- Evaluated the model using **MAE, MSE, RMSE, and R² Score**.
- Saved the trained model as **salary_model.pkl**.
- Developed a multi-page Streamlit web application.
- Added Employee Registration page.
- Added Salary Prediction page.
- Added Employee Report page.
- Added Download Employee Report functionality.
- Added Exploratory Data Analysis using **data_visualization.py**.
- Added project workflow diagrams.
- Added application screenshots.
- Improved project documentation.

---

# 🔮 Future Enhancements

- User Authentication
- Database Integration
- Cloud Deployment
- Interactive Dashboard
- Comparison of Multiple Machine Learning Models
- Email Report Generation
- Responsive User Interface

---

# 👩‍💻 Developed By

**Sonica Kannan**

B.E. Computer Science and Engineering  
(Artificial Intelligence & Machine Learning)

Thiagarajar College of Engineering

Machine Learning & Deep Learning Intern

---

⭐ **If you found this project helpful, consider giving it a Star on GitHub!**
