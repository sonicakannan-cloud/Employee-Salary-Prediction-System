import streamlit as st

#Page configuration
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="centered"
)

#Title
st.title("💼 Employee Salary Prediction System")
st.subheader("Employee Registration Form")

st.write("Please enter your personal details befor predicting the salary.")

#Registeration Form
with st.form("registeration_form"):
    name=st.text_input("Full Name")
    age=st.number_input("Age",min_value=18,max_value=65)
    gender=st.selectbox("Gender",["M","F"])
    email=st.text_input("Email")
    phone=st.text_input("Phone Number")
    city=st.text_input("City")
    register=st.form_submit_button("Register")
    
#After Clicking Register
if register:
    #save details
    st.session_state["name"]=name
    st.session_state["age"]=age
    st.session_state["gender"]=gender
    st.session_state["email"]=email
    st.session_state["phone"]=phone
    st.session_state["city"]=city
    
    st.success("Registeration Successful!")
    st.info("Moving to Salary Prediction page...")
    st.switch_page("pages/1_Salary_Prediction.py")