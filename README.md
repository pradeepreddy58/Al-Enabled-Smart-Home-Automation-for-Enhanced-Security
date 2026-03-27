**AI-Enabled Smart Home Automation for Enhanced Security  
**Overview**  

This project presents an intelligent AI-enabled smart home security system that uses machine learning techniques to detect anomalies (intrusions) based on IoT sensor data. The system integrates data preprocessing, multiple ML models, and a user-friendly GUI to monitor and enhance home security.  

**Objective**  

The main objective of this project is to:  

Detect unauthorized activities in a smart home environment  
Improve security using machine learning models  
Provide real-time monitoring and alerts  
Automate the analysis of sensor data for intrusion detection  

Tech Stack  
*Programming Language  
Python  
*Libraries Used  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
NLTK  
Tkinter (for GUI)  
*Machine Learning Models  
Support Vector Machine (SVM)  
Random Forest Classifier  
Naive Bayes  
*Dataset Description  

The system uses a dataset containing IoT sensor data with the following features:  

timestamp → Time of sensor reading  
sensor_type → Type of sensor (motion, temperature, etc.)  
sensor_value → Sensor reading value  
location → Location of sensor in home  
alert → Target label (Normal / Anomaly)  
*Project Workflow  
🔹 Step 1: Dataset Upload  
User uploads CSV dataset through GUI  
System displays dataset preview and missing values  
🔹 Step 2: Data Preprocessing  
Label Encoding for categorical features  
Feature Scaling using StandardScaler  
Splitting into training and testing datasets  
🔹 Step 3: Model Training  

The system trains multiple ML models:  

SVM  
Random Forest  
Naive Bayes  

Each model is evaluated using:  

Accuracy  
Precision  
Recall  
F1 Score  
🔹 Step 4: Model Comparison  
A graphical comparison (pie chart) is displayed  
Helps identify best performing model  
🔹 Step 5: Prediction  
User uploads new test data  
System predicts:  
Normal Activity  
Anomalous Activity  
**User Interface (GUI)    

The system provides an interactive GUI with:  

Admin Login System  
Dashboard with control buttons:  
Upload Dataset  
Preprocessing  
Train Models  
Accuracy Graph  
Prediction  
*Key Features  
Multi-model machine learning approach  
Real-time anomaly detection  
User-friendly GUI  
Data visualization (accuracy graph)  
Automated preprocessing and prediction  
*How to Run the Project  
Step 1: Clone the repository  
git clone <your-repo-link>  
cd your-project-folder  
Step 2: Create virtual environment  
python -m venv venv  
Step 3: Activate virtual environment  
venv\Scripts\activate  
Step 4: Install dependencies  
pip install -r req.txt  
Step 5: Download NLTK data  
python -c "import nltk; nltk.download('stopwords')"  
Step 6: Run the project  
python admin_portal.py  
Step 7: Login Credentials  
Username: admin  
Password: admin  
*Results  
Successfully detects anomalies in IoT sensor data  
Provides accurate predictions using multiple ML models  
Random Forest generally performs best (based on experiments)  
*Limitations  
Uses static dataset (no real-time IoT hardware integration)  
GUI-based system (not web deployed)  
Requires dataset format consistency  
Future Enhancements  
Integration with real IoT devices (ESP32, Raspberry Pi)  
Deployment as a web application (Flask/Django)  
Integration of deep learning models  
Real-time alert system (SMS/Email)  
