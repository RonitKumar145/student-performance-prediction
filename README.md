# 🎓 Student Performance Predictor

A Machine Learning project that predicts student exam scores based on academic, personal, and environmental factors using **Linear Regression** and a **Streamlit Web Application**.

---

## 📌 Overview

This project predicts student exam performance using various factors such as:

* Hours Studied
* Attendance
* Previous Scores
* Motivation Level
* Family Income
* Teacher Quality
* Internet Access
* Parental Involvement
* Sleep Hours
* Physical Activity

The project covers the complete Machine Learning workflow:

* Data Collection
* Exploratory Data Analysis (EDA)
* Data Preprocessing
* Feature Engineering
* Model Training
* Model Evaluation
* Model Deployment using Streamlit

---

## 🎯 Objective

The goal of this project is to analyze factors affecting student performance and build a predictive model capable of estimating exam scores accurately.

---

## 📊 Dataset Information

### Dataset

Student Performance Factors Dataset

### Features

| Feature                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| Hours_Studied              | Number of study hours                       |
| Attendance                 | Attendance percentage                       |
| Parental_Involvement       | Parent participation level                  |
| Access_to_Resources        | Availability of educational resources       |
| Extracurricular_Activities | Participation in extracurricular activities |
| Sleep_Hours                | Average sleep duration                      |
| Previous_Scores            | Previous academic performance               |
| Motivation_Level           | Student motivation level                    |
| Internet_Access            | Internet availability                       |
| Tutoring_Sessions          | Number of tutoring sessions                 |
| Family_Income              | Family income category                      |
| Teacher_Quality            | Quality of teaching                         |
| School_Type                | Public or Private school                    |
| Peer_Influence             | Influence of friends                        |
| Physical_Activity          | Physical activity hours                     |
| Learning_Disabilities      | Presence of learning disabilities           |
| Parental_Education_Level   | Parents' education level                    |
| Distance_from_Home         | Distance between home and school            |
| Gender                     | Student gender                              |

### Target Variable

```text
Exam_Score
```

---

## 🛠 Tech Stack

### Programming Language

* Python

### Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Joblib

### Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## 📂 Project Structure

```text
student-performance-prediction/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── models/
│   └── student_score_model.pkl
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── src/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔍 Exploratory Data Analysis

### Performed Analysis

* Dataset Overview
* Missing Value Analysis
* Feature Classification
* Correlation Analysis
* Numerical Feature Analysis
* Categorical Feature Analysis

### Key Findings

* Attendance showed the strongest positive correlation with Exam Score.
* Hours Studied significantly influenced student performance.
* Previous Scores and Tutoring Sessions had moderate impact.
* Sleep Hours showed little linear correlation with Exam Scores.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

* Train-Test Split (80/20)
* Feature Selection
* One-Hot Encoding for Categorical Features
* Pipeline Creation using Scikit-Learn

---

## 🤖 Machine Learning Models

### Linear Regression

Used as the baseline regression model.

### Random Forest Regressor

Used for comparison against Linear Regression.

---

## 📈 Model Performance

### Linear Regression

| Metric   | Value |
| -------- | ----- |
| R² Score | 0.77  |
| MAE      | 0.45  |
| RMSE     | 1.80  |

### Random Forest

| Metric   | Value |
| -------- | ----- |
| R² Score | 0.67  |

### Best Model

🏆 Linear Regression outperformed Random Forest on this dataset.

---

## 🚀 Streamlit Application

The project includes a Streamlit-based web application where users can:

* Enter student information
* Select academic and personal factors
* Predict Exam Score instantly

### Features

* Interactive UI
* Real-Time Prediction
* Easy User Input
* Machine Learning Integration

---

## 📸 Screenshots

### Home Page

Add screenshot here:

```text
screenshots/Homepage.png
```

### Prediction Result

Add screenshot here:

```text
screenshots/prediction.png
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/RonitKumar145/student-performance-prediction.git
```

### Navigate to Project Folder

```bash
cd student-performance-prediction
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🧠 Skills Learned

Through this project, I learned:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning Pipelines
* Linear Regression
* Model Evaluation
* Streamlit Deployment
* Git & GitHub Workflow

---

## 🔮 Future Improvements

* Hyperparameter Tuning
* XGBoost Implementation
* Model Explainability
* Cloud Deployment
* User Authentication
* Dashboard Analytics

---

## 👨‍💻 Author

### Ronit Kumar

Artificial Intelligence & Machine Learning Student

GitHub:
https://github.com/RonitKumar145

LinkedIn:
https://www.linkedin.com/in/ronit-kumar-64271b258

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.
