import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/student_score_model.pkl")

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


st.title("Student Performance Predictor")

st.write(
    "Predict a student's exam score using study habits and academic factors."
)

# Inputs

hours_studied = st.number_input(
    "Hours Studied",
    min_value=1,
    max_value=50,
    value=20
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

parental_involvement = st.selectbox(
    "Parental Involvement",
    ["Low", "Medium", "High"]
)

access_to_resources = st.selectbox(
    "Access to Resources",
    ["Low", "Medium", "High"]
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=1,
    max_value=12,
    value=7
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=0,
    max_value=100,
    value=70
)

motivation_level = st.selectbox(
    "Motivation Level",
    ["Low", "Medium", "High"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

tutoring_sessions = st.number_input(
    "Tutoring Sessions",
    min_value=0,
    max_value=20,
    value=2
)

family_income = st.selectbox(
    "Family Income",
    ["Low", "Medium", "High"]
)

teacher_quality = st.selectbox(
    "Teacher Quality",
    ["Low", "Medium", "High"]
)

school_type = st.selectbox(
    "School Type",
    ["Public", "Private"]
)

peer_influence = st.selectbox(
    "Peer Influence",
    ["Positive", "Neutral", "Negative"]
)

physical_activity = st.number_input(
    "Physical Activity (hrs/week)",
    min_value=0,
    max_value=20,
    value=5
)

learning_disabilities = st.selectbox(
    "Learning Disabilities",
    ["Yes", "No"]
)

parental_education = st.selectbox(
    "Parental Education Level",
    ["High School", "College", "Postgraduate"]
)

distance_from_home = st.selectbox(
    "Distance From Home",
    ["Near", "Moderate", "Far"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

if st.button("Predict Score"):

    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Extracurricular_Activities": [extracurricular],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Motivation_Level": [motivation_level],
        "Internet_Access": [internet_access],
        "Tutoring_Sessions": [tutoring_sessions],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "School_Type": [school_type],
        "Peer_Influence": [peer_influence],
        "Physical_Activity": [physical_activity],
        "Learning_Disabilities": [learning_disabilities],
        "Parental_Education_Level": [parental_education],
        "Distance_from_Home": [distance_from_home],
        "Gender": [gender]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Exam Score: {prediction[0]:.2f}"
    )
    st.metric(
    "Predicted Score",
    f"{prediction[0]:.2f}"
)

st.markdown(
    """
    ## Student Performance Predictor
    Predict exam scores using machine learning.
    """
)