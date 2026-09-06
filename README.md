Phishing Website Detection System

 Project Overview:

The Phishing Website Detection System is a Machine Learning-based project that predicts whether a given website URL is legitimate or phishing.

Phishing websites are designed to imitate legitimate websites and trick users into providing sensitive information such as usernames, passwords, banking details, and personal information.

This project uses URL-based features and a Random Forest Classifier to identify potentially phishing websites.

---
Objectives:

- Detect phishing websites using Machine Learning.
- Analyze important characteristics of website URLs.
- Perform data preprocessing and feature engineering.
- Train and evaluate a classification model.
- Provide a simple interface for users to check a URL.

---

 Technologies Used:

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Matplotlib
- Streamlit
- Joblib
- Google Colab / VS Code
- Git & GitHub

---

Dataset:

The project uses a dataset containing URL-based features used to identify phishing websites.

Some of the features include:

- "NumDots"
- "UrlLength"
- "NumDash"
- "AtSymbol"
- "IpAddress"
- "HttpsInHostname"
- "PathLevel"
- "PathLength"
- "NumNumericChars"

The target variable is:

- "Phising" — indicates whether the URL is phishing or legitimate.

---

Project Workflow:

Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Random Forest Classifier
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Application
   ↓
Enter Website URL
   ↓
Prediction
   ↓
Phishing / Legitimate

---

Machine Learning Model:

A Random Forest Classifier is used for classification.

Random Forest combines multiple decision trees to make predictions and is suitable for classification problems involving multiple URL features.

The dataset is divided into training and testing data using an 80:20 split.

---

 Model Evaluation:

The trained model is evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The model achieved approximately 82.8% accuracy on the test data during development.

«Note: Model performance may vary depending on preprocessing, dataset version, features, and training configuration.»

---

Application:

The project includes a simple Streamlit-based interface.

Users can enter a website URL, and the system extracts relevant URL features and uses the trained Machine Learning model to predict whether the website is:

Legitimate

or

Phishing

---

 Project Structure:

phishing_url_detector/
│
├── app.py
├── model.pkl
├── Phising_Detection_Dataset.csv
├── requirements.txt
├── README.md
└── screenshots/

---

 How to Run the Project:

1. Clone the repository

git clone https://github.com/AswiniDesalinka/phishing_url_detector.git

2. Open the project folder

cd phishing_url_detector

3. Install required libraries

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open in your browser.

---

Requirements:

The main Python libraries used are:

pandas
numpy
scikit-learn
joblib
streamlit

---

Future Enhancements:

The project can be improved by:

- Using larger and more diverse datasets.
- Testing additional Machine Learning algorithms.
- Improving feature extraction.
- Adding real-time URL analysis.
- Integrating domain and webpage-based features.
- Improving model accuracy.
- Deploying the application as a web service.
- Adding explainable AI features to show why a URL was classified as phishing.

---
Output:
https://phishing-detector-aswini.streamlit.app

Limitations:

- The prediction depends on the features used during model training.
- The system may not detect every newly created phishing website.
- Model performance depends on the quality and diversity of the dataset.
- URL-based analysis alone cannot guarantee that a website is completely safe.

---

 Author:

Aswini Desalinka

MCA Student
Adikavi Nannaya University

---

Conclusion:

The Phishing Website Detection System demonstrates how Machine Learning can be applied to cybersecurity problems.

By analyzing URL characteristics and using a Random Forest classification model, the system can help identify potentially phishing websites and provide users with an additional layer of awareness before visiting suspicious URLs.
