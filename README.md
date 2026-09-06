🛡️ Phishing URL Detection System

Machine Learning Based Phishing Website Detection using Random Forest and Streamlit

A Machine Learning-based cybersecurity project that analyzes URL characteristics and predicts whether a given website URL is Legitimate or Phishing.

---

🚀 Live Demo

🔗 Try the Application:
https://phishing-detector-aswini.streamlit.app

---

📌 Project Overview

Phishing is a common cybersecurity attack in which attackers create fraudulent websites that imitate legitimate websites to steal sensitive information such as usernames, passwords, banking details, and personal information.

This project uses Machine Learning to analyze different characteristics of website URLs and classify them as either Legitimate or Phishing.

A Random Forest Classifier is used to train the model, and a Streamlit web application provides an easy-to-use interface for making predictions.

---

🎯 Objectives

- Detect potentially phishing URLs using Machine Learning.
- Analyze important characteristics of website URLs.
- Perform data preprocessing and feature selection.
- Train and evaluate a classification model.
- Extract URL features automatically.
- Provide a simple web-based interface for users.
- Demonstrate the application of Machine Learning in cybersecurity.

---

🧰 Technologies Used

Technology| Purpose
🐍 Python| Programming Language
🐼 Pandas| Data Processing
🔢 NumPy| Numerical Computation
🤖 Scikit-learn| Machine Learning
🌲 Random Forest| Classification Algorithm
📊 Matplotlib| Data Visualization
💾 Joblib| Model Saving and Loading
🌐 Streamlit| Web Application
☁️ Google Colab| Model Development
💻 VS Code| Development
🔧 Git & GitHub| Version Control

---

📊 Dataset

The project uses a dataset containing URL-based features for identifying phishing websites.

Important URL Features

- "NumDots" – Number of dots in the URL
- "UrlLength" – Length of the URL
- "NumDash" – Number of dashes in the URL
- "AtSymbol" – Presence of the "@" symbol
- "IpAddress" – Indicates whether an IP address is used
- "HttpsInHostname" – HTTPS-related hostname feature
- "PathLevel" – Depth of the URL path
- "PathLength" – Length of the URL path
- "NumNumericChars" – Number of numeric characters

Target Variable

"Phising"

«Note: "Phising" is the original target-column name in the dataset. The standard spelling is Phishing.»

---

🔄 Project Workflow

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
Model Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Application
   ↓
Enter Website URL
   ↓
Extract URL Features
   ↓
Machine Learning Prediction
   ↓
Phishing / Legitimate

---

🤖 Machine Learning Model

Random Forest Classifier

The project uses a Random Forest Classifier for phishing URL classification.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to produce a final prediction.

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

The model learns patterns from URL-based features and uses these patterns to classify new URLs.

---

📈 Model Evaluation

The trained model is evaluated using the following classification metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Model Accuracy

The model achieved approximately:

🎯 82.8% Accuracy

«Model performance may vary depending on preprocessing, dataset version, feature selection, and training configuration.»

---

🌐 Streamlit Application

The project includes an interactive web application developed using Streamlit.

Users can enter a website URL, and the application extracts relevant URL features and sends them to the trained Machine Learning model.

Application Workflow

User enters URL
       ↓
URL Feature Extraction
       ↓
Trained Random Forest Model
       ↓
Prediction
       ↓
┌───────────────────┐
│   Legitimate URL  │
│        OR         │
│    Phishing URL   │
└───────────────────┘

Example

Input:
https://www.example.com

Output:
Legitimate

The application is intended to provide an additional layer of awareness when users encounter suspicious URLs.

---

✨ Key Features

- 🔍 URL-based phishing detection
- 🤖 Machine Learning classification
- 🌲 Random Forest algorithm
- 🧠 Automatic URL feature extraction
- 🌐 Interactive Streamlit interface
- 📊 Model evaluation
- 💾 Trained model saved using Joblib
- 🚀 Web-based prediction
- 🔧 Easy to run locally

---

📁 Project Structure

phishing_url_detector/
│
├── app.py
├── model.pkl
├── Phising_Detection_Dataset.csv
├── project_2.ipynb
├── requirements.txt
├── README.md
└── phishing url detection ppt (1).pdf

---

⚙️ Installation and Setup

1. Clone the Repository

git clone https://github.com/AswiniDesalinka/phishing_url_detector.git

2. Navigate to the Project Directory

cd phishing_url_detector

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit Application

streamlit run app.py

The application will open in your default web browser.

---

📦 Requirements

The main Python libraries used in this project are:

pandas
numpy
scikit-learn
joblib
streamlit
matplotlib

All required dependencies are listed in:

requirements.txt

---

🔮 Future Enhancements

The system can be further improved by:

- Using larger and more diverse phishing URL datasets.
- Testing additional Machine Learning algorithms.
- Improving URL feature extraction.
- Adding real-time domain analysis.
- Integrating webpage-based features.
- Improving model accuracy.
- Adding explainable AI to show why a URL was classified as phishing.
- Detecting newly emerging phishing patterns.
- Deploying the system as a scalable web service.
- Adding additional security-related features.

---

⚠️ Limitations

- The prediction depends on the URL features used during model training.
- The system may not detect every newly created phishing website.
- Model performance depends on the quality and diversity of the dataset.
- URL-based analysis alone cannot guarantee that a website is completely safe.
- Predictions should not be considered a replacement for professional cybersecurity tools or safe browsing practices.

---

🎓 Academic Information

Project Title: Phishing Website Detection System
Domain: Machine Learning & Cybersecurity
Degree: Master of Computer Applications (MCA)
University: Adikavi Nannaya University

---

👩‍💻 Author

Aswini Desalinka

MCA Student
Adikavi Nannaya University

---

📜 License

This project was developed for educational and academic purposes.

---

⭐ Conclusion

The Phishing URL Detection System demonstrates how Machine Learning can be applied to a real-world cybersecurity problem.

By analyzing URL characteristics and using a Random Forest classification model, the system can identify URLs as potentially Phishing or Legitimate.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, feature selection, model training, model evaluation, model saving, URL feature extraction, and deployment through a Streamlit web application.
