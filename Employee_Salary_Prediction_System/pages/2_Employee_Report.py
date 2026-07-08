import streamlit as st
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet

#Page Configuration
st.set_page_config(
    page_title="Employee Salary Report",
    page_icon="📄",
    layout="centered"
)

#Check whether Salary is predicted
if "salary" not in st.session_state:
    st.warning("Please predict the salary first")
    st.stop()

#Heading
st.title("Employee Salary Report")
st.success("Salary Prediction Completed Successfully!")

st.divider()

#Employee Details
st.subheader("Employee Details")
st.write("**Employee Name:**",st.session_state["name"])
st.write("**Age:**",st.session_state["age"])
st.write("**Gender:**", st.session_state["gender"])
st.write("**Email:**", st.session_state["email"])
st.write("**Phone Number:**", st.session_state["phone"])
st.write("**City:**", st.session_state["city"])
st.write("**Education Level:**", st.session_state["education"])
st.write("**Job Title:**", st.session_state["job"])
st.write("**Years of Experience:**", st.session_state["experience"])

st.divider()

#Salary

st.subheader("Predicted Annual Salary")

salary=st.session_state["salary"]

st.metric(
    label="predicted Annual Salary",
    value=f"Rs {salary:.2f}"
)

st.divider()

#Create PDF
def create_pdf():
    filename="Employee_Salary_Report.pdf"
    doc=SimpleDocTemplate(filename)
    styles=getSampleStyleSheet()
    content=[]
    
    content.append(Paragraph("<b>Employee Salary Report</b>",styles["Title"]))
    
    content.append(Paragraph(f"Employee Name : {st.session_state['name']}", styles["Normal"]))
    content.append(Paragraph(f"Age : {st.session_state['age']}", styles["Normal"]))
    content.append(Paragraph(f"Gender : {st.session_state['gender']}", styles["Normal"]))
    content.append(Paragraph(f"Email : {st.session_state['email']}", styles["Normal"]))
    content.append(Paragraph(f"Phone : {st.session_state['phone']}", styles["Normal"]))
    content.append(Paragraph(f"City : {st.session_state['city']}", styles["Normal"]))
    content.append(Paragraph(f"Education : {st.session_state['education']}", styles["Normal"]))
    content.append(Paragraph(f"Job Title : {st.session_state['job']}", styles["Normal"]))
    content.append(Paragraph(f"Experience : {st.session_state['experience']} Years", styles["Normal"]))
    content.append(Paragraph(f"Salary : Rs {salary:,.2f}", styles["Heading2"]))
    
    doc.build(content)
    return filename

#Download PDF
pdf=create_pdf()

with open(pdf,"rb") as file:
    st.download_button(
        label="Download",
        data=file,
        file_name="Employee_Salary_Report.pdf",
        mime="application/pdf"
    )