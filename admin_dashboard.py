import tkinter as tk
from tkinter import filedialog
import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tkinter import END
from tkinter.simpledialog import askstring
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, END, Text
from sklearn.naive_bayes import GaussianNB
import time
# Function to perform label encodingfrom sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
import tkinter as tk
from tkinter import filedialog, END, Text
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import END, Text
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import string
from nltk.corpus import stopwords




# Function to load the dataset
def Upload_dataset():
    global dataset_file, data, text
    dataset_file = filedialog.askopenfilename(initialdir="dataset")
    pathlabel.config(text=dataset_file)
    text.delete('1.0', tk.END)
    text.insert(tk.END, dataset_file + " dataset loaded\n\n")
    data = pd.read_csv(dataset_file, encoding='latin-1')
    text.insert(tk.END, str(data.head()) + "\n")
    # Calculate and display the shape of the data
    dataset_shape = data.shape
    text.insert(tk.END, f"Dataset Shape: {dataset_shape}\n")
    # Identify missing values and display them
    missing_values = data.isnull().sum()
    text.insert(tk.END, "Missing Values:\n")
    for column, count in missing_values.items():
        text.insert(tk.END, f"{column}: {count}\n")



def Preprocessing():
    global data,X_train, X_test, y_train, y_test

    # Specify the relevant features (adjust as necessary based on your data)
    relevant_features = ["timestamp", "sensor_type", "sensor_value", "location", "alert"]

    # Select the features from the data and separate the target variable (alert)
    X = data[relevant_features]
    X = X.drop('alert', axis=1)  # 'alert' is the target variable
    y = data['alert']
    

    # Apply Label Encoding to categorical columns in X
    label_encoder = LabelEncoder()
    categorical_cols = X.select_dtypes(include=['object']).columns

    # Apply LabelEncoder to each categorical column in X
    for col in categorical_cols:
        X[col] = label_encoder.fit_transform(X[col])

    # Apply Label Encoding to the target variable (y)
    y = label_encoder.fit_transform(y)

    # Scale numerical features (e.g., timestamp, sensor_value)
    scaler = StandardScaler()
    X[['timestamp', 'sensor_value']] = scaler.fit_transform(X[['timestamp', 'sensor_value']])

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Update the Text widget with the shapes of the splits
    text.delete('1.0', END)  # Clear existing content in the Text widget
    text.insert(END, "Shapes of X_train, X_test, y_train, y_test are: \n\n\n")
    text.insert(END, "Shape of X_train: " + str(X_train.shape) + "\n")
    text.insert(END, "Shape of X_test: " + str(X_test.shape) + "\n")
    text.insert(END, "Shape of y_train: " + str(y_train.shape) + "\n")
    text.insert(END, "Shape of y_test: " + str(y_test.shape) + "\n")








# Function to train and evaluate SVM model
def SVM_model():
    global svm_model, svm_accuracy
    svm_model = SVC(kernel='linear')  # You can choose other kernels like 'rbf', 'poly', etc.
    svm_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = svm_model.predict(X_test)

    # Calculate accuracy score
    svm_accuracy = accuracy_score(y_test, y_pred)
    #recall_score
    svm_recall = recall_score(y_test, y_pred)
    #f1_score
    svm_f1 = f1_score(y_test, y_pred)
    #precision_score
    svm_precision = precision_score(y_test, y_pred)


    # Display the accuracy score in the Text widget
    text.delete('1.0', END)  # Clear existing content in the Text widget
    text.insert(END, "The SVM model achieved an accuracy of: {:.2f}%".format(svm_accuracy * 100)+ "\n\n")
    text.insert(END, "The SVM model achieved a recall of: {:.2f}%".format(svm_recall * 100)+ "\n\n")
    text.insert(END, "The SVM model achieved a f1 score of: {:.2f}%".format(svm_f1 * 100)+ "\n\n")
    text.insert(END, "The SVM model achieved a precision of: {:.2f}%".format(svm_precision * 100)+ "\n\n")
     






# Function to train and evaluate Random Forest model
def Run_RF_model():
    global rf_model,rf_accuracy
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # 100 trees in the forest
    rf_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_model.predict(X_test)

    # Calculate accuracy score
    rf_accuracy = accuracy_score(y_test, y_pred)
    #recall_score
    rf_recall = recall_score(y_test, y_pred)
    #f1_score
    rf_f1 = f1_score(y_test, y_pred)
    #precision_score
    rf_precision = precision_score(y_test, y_pred)


    # Display the accuracy score in the Text widget
    text.delete('1.0', END)  # Clear existing content in the Text widget
    text.insert(END, "Random Forest Model Accuracy: {:.2f}%".format(rf_accuracy * 100)+"\n\n")
    text.insert(END, "Random Forest Model Recall: {:.2f}%".format(rf_recall * 100)+"\n\n")  
    text.insert(END, "Random Forest Model F1 Score: {:.2f}%".format(rf_f1 * 100)+"\n\n")
    text.insert(END, "Random Forest Model Precision: {:.2f}%".format(rf_precision * 100)+"\n\n")


# Function to train and evaluate Naive Bayes model
def run_Naive_Bayes_model():
    global nb_model, nb_accuracy
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = nb_model.predict(X_test)

    # Calculate accuracy score
    nb_accuracy = accuracy_score(y_test, y_pred)
    #recall_score
    nb_recall = recall_score(y_test, y_pred)
    #f1_score
    nb_f1 = f1_score(y_test, y_pred)
    #precision_score
    nb_precision = precision_score(y_test, y_pred)


    # Display the accuracy score in the Text widget
    text.delete('1.0', END)  # Clear existing content in the Text widget
    text.insert(END, "Naive Bayes Model Accuracy: {:.2f}%".format(nb_accuracy * 100)+"\n\n")
    text.insert(END, "Naive Bayes Model Recall: {:.2f}%".format(nb_recall * 100)+"\n\n")
    text.insert(END, "Naive Bayes Model F1 Score: {:.2f}%".format(nb_f1 * 100)+"\n\n")
    text.insert(END, "Naive Bayes Model Precision: {:.2f}%".format(nb_precision * 100)+"\n\n")




# Function to display Accuracy Pie Chart
def Accuracy_Graph():
    # List of algorithm names and their corresponding accuracy scores
    algorithms = ['SVM', 'Random Forest', 'Naive Bayes']
    accuracies = [svm_accuracy, rf_accuracy, nb_accuracy]  # Using the accuracy values from the models

    # Set color palette for the pie chart
    colors = ['#ff9999','#66b3ff','#99ff99']

    # Create pie chart
    plt.figure(figsize=(7,7))
    plt.pie(accuracies, labels=algorithms, autopct='%1.2f%%', startangle=90, colors=colors, explode=(0.1, 0, 0))
    plt.title('Algorithm Accuracy Comparison')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart
    plt.show()



def predict():
    global prediction_file, prediction_data
    prediction_file = filedialog.askopenfilename(initialdir="dataset", filetypes=[("CSV Files", "*.csv")])
    pathlabel.config(text=prediction_file)
    text.delete('1.0', tk.END)
    text.insert(tk.END, prediction_file + " file loaded\n\n")
    prediction_data = pd.read_csv(prediction_file, encoding='latin-1')
    text.insert(tk.END, str(prediction_data.head()) + "\n")

    # Check the number of rows in the loaded prediction data
    num_rows = prediction_data.shape[0]
    text.insert(tk.END, f"Number of rows in input data: {num_rows}\n")

    # Apply the same preprocessing steps as in the Preprocessing function
    relevant_features = ["timestamp", "sensor_type", "sensor_value", "location"]
    prediction_data = prediction_data[relevant_features]

    label_encoder = LabelEncoder()
    categorical_cols = prediction_data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        prediction_data[col] = label_encoder.fit_transform(prediction_data[col])

    # Ensure to scale numerical features
    scaler = StandardScaler()
    prediction_data[['timestamp', 'sensor_value']] = scaler.fit_transform(prediction_data[['timestamp', 'sensor_value']])

    # Check the shape of the preprocessed data
    text.insert(tk.END, f"Shape of preprocessed data: {prediction_data.shape}\n")

    # Use the trained models to make predictions
    rf_prediction = rf_model.predict(prediction_data)

    # Display the predictions
    text.insert(tk.END, "Predictions:\n")
    for i in range(num_rows):
        text.insert(tk.END, f"Row {i+1}:\n")
        text.insert(tk.END, f"Random Forest: {'normal' if rf_prediction[i] == 1 else 'anomaly'}\n")






# Function for animating the title
class AnimatedTitle:
    def __init__(self, label, text, interval=150):
        self.label = label
        self.text = text
        self.interval = interval
        self.index = 0
        self.animate()

    def animate(self):
        if self.index <= len(self.text):
            self.label.config(text=self.text[:self.index])
            self.index += 1
            self.label.after(self.interval, self.animate)


# Add button for plotting graphs
def admin_portal():
    global portal  # Declare portal as a global variable
    portal = tk.Tk()
    portal.title("Al-Enabled Smart Home Automation for Enhanced Security")
    portal.geometry("1000x700")
    portal.configure(bg="#222222")

    # Title Section with Animation
    title_frame = tk.Frame(portal, bg="#444444", pady=10)
    title_frame.pack(fill="x")
    title_label = tk.Label(
        title_frame,
        text="",
        font=("Helvetica", 24, "bold"),
        bg="#444444",
        fg="#FFD700",
    )
    title_label.pack(pady=20)
    title_text = "Al-Enabled Smart Home Automation for Enhanced Security"
    AnimatedTitle(title_label, title_text, interval=100)

    # Navbar Frame with styled buttons
    navbar_frame = tk.Frame(portal, bg="#333333", pady=10)
    navbar_frame.pack(fill="x", pady=(0, 20))

    button_style = {
        "font": ("Helvetica", 14, "bold"),  # Larger font with bold text
        "bg": "#FFD700",  # Gold background
        "fg": "#333333",  # Dark text color for contrast
        "width": 10,  # Slightly larger width for better visibility
        "height": 1,  # Adequate height for better user interaction
        "bd": 2,  # Border thickness
        "relief": "sunken",  # Default button relief to create a pressed effect
        "activebackground": "#FFA500",  # Background color when the button is clicked
        "activeforeground": "#fff",  # Text color when clicked
        "highlightbackground": "#444444",  # Border color when the button is not in focus
        "highlightcolor": "#FFD700",  # Border color when the button is focused
        "highlightthickness": 2,  # Thicker border to highlight the button
        "padx": 10,  # Padding for more space around the text
        "pady": 10,  # Padding for more space around the text
        "borderwidth": 3,  # Thicker border for better depth perception
        "relief": "raised",  # Raised effect when hovered
        "overrelief": "solid",  # The effect when clicked
        "font": ("Helvetica", 12, "bold"),
    }

    def hover_in(event):
        event.widget["bg"] = "#FFA500"

    def hover_out(event):
        event.widget["bg"] = "#FFD700"

    buttons = [
        ("Upload Dataset", Upload_dataset),
        ("Preprocessing", Preprocessing),  # Ensure this points to the updated Preprocessing function
        ("SVM", SVM_model),
        ("Run_RF", Run_RF_model),
        ("run_Naive_Bayes", run_Naive_Bayes_model),
        ("Accuracy_Graph", Accuracy_Graph),
        ("Predict", predict),
    ]

    # Create Buttons in a horizontal line
    for i, (btn_text, command) in enumerate(buttons):
        btn = tk.Button(navbar_frame, text=btn_text, command=command, **button_style)
        btn.grid(row=0, column=i, padx=10, pady=10)  # Place all buttons in one row
        btn.bind("<Enter>", hover_in)
        btn.bind("<Leave>", hover_out)

    # File path display
    global pathlabel
    pathlabel = tk.Label(
        portal,
        text="No file selected",
        bg="#222222",
        fg="#FFD700",
        font=("Helvetica", 14),
    )
    pathlabel.pack(pady=10)

    # Large Textbox for content display
    global text
    text = tk.Text(
        portal,
        font=("Courier", 12),
        width=120,
        height=20,
        wrap="word",
        bg="#f4f4f4",
        fg="#333333",
        bd=2,
        relief="sunken",
    )
    text.pack(pady=(10, 20))

    portal.mainloop()

