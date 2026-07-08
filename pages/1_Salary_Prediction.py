import streamlit as st
import pandas as pd
import pickle

#checking registeration
if "name" not in st.session_state:
    st.warning("Please register first.")
    st.stop()
    
#Load Model
with open("salary_model.pkl","rb") as file:
    loaded,encoder=pickle.load(file)
    
#Heading
st.title("Employee Salary prediction and Analysis")
st.write(f"Welcome, {st.session_state['name']} ")
st.write("Enter the Employee details :")

#Professional Details
education =st.selectbox("Education Level",encoder["Education Level"].classes_)
job = st.selectbox("Job Title",encoder["Job Title"].classes_)
years = st.number_input("Years of Experience",min_value=0,max_value=40)

#Predict salary
if st.button("Predict Salary"):
    # Convert categorical inputs into machine-readable format
    age=st.session_state["age"]
    gender=st.session_state["gender"]
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
    predicted_salary = loaded.predict(new_data)[0]
    
    # Store values for Report Page
    st.session_state["education"] = encoder["Education Level"].inverse_transform([education])[0]
    st.session_state["job"] = encoder["Job Title"].inverse_transform([job])[0]
    st.session_state["experience"] = years
    st.session_state["salary"] = predicted_salary

    st.success("Salary Predicted Successfully!")
    st.switch_page("pages/2_Employee_Report.py")
