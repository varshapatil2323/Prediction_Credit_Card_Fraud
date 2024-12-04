# Prediction_Credit_Card_Fraud
prediction of Credit Card Fraud using Machine Learning Models

# Credit Card Fraud Prediction

## Project Overview
This project focuses on predicting fraudulent credit card transactions using machine learning techniques. It tackles the challenges of working with imbalanced datasets and 
emphasizes achieving high accuracy and recall for fraud detection.

## Problem Statement
Credit card fraud detection is a critical task for financial institutions. The goal is to accurately predict whether a transaction is fraudulent (Class 1) or legitimate (Class 0) based 
on a dataset of transaction attributes.

## Dataset
- **Source**: [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Description**: The dataset contains transactions made by European cardholders in September 2013. It is highly imbalanced, with fraudulent transactions accounting for only 
   0.17% of the dataset.
- **Attributes**:
  - `Time`: Seconds elapsed between this transaction and the first transaction in the dataset.
  - `Amount`: Transaction amount.
  - `Class`: Target variable (0 = Non-Fraud, 1 = Fraud).
  - `V1` to `V28`: Principal component analysis (PCA)-transformed features.

## Project Structure
credit-card-fraud-prediction/ ├── data/ │ ├── raw/ (raw dataset files) │ ├── processed/ (processed datasets) │ └── README.md (dataset description)
 ├── notebooks/ │ ├── 01-credit_card_fraud_finaltest.ipynb │ ├── 02-model-building │ ├── 03-model-evaluation │ └── 04-deployment ├── 
models/ (saved trained models in .pkl format) ├── visuals/ (visualizations and plots) ├── requirements.txt (Python dependencies) └── README.md (this file)

## Setup Instructions
1. **Clone the Repository**
 
   git clone https://github.com/varshapatil2323/Prediction_Credit_Card_Fraud.git
   cd Prediction_Credit_Card_Fraud

Install Dependencies Use the provided requirements.txt file to set up your environment:


pip install -r requirements.txt
Run Jupyter Notebooks

Navigate to the notebooks/ folder.
Start Jupyter Notebook:  Open File -File Name
credit_card_fraud_finaltest.ipynb

Key Results
Model Used: Random Forest Classifier 
Accuracy: 99.98%
Precision (Fraud): 99.97%
Recall (Fraud): 100%
AUC-ROC: 99.99%

Models
Save Model the of Random Forest Classifier 
credit_card_model.pkl
fraud_detection_model.pkl

Visualizations
Class Distribution
Feature Distribution using histogram and boxplot
Correlation Matrix
ROC Curve
Confusion Matrix 
Best Model Prediction using Barplot

Future Work
Experiment with deep learning models for fraud detection.
Build an API for real-time fraud prediction.


Contact
For any questions or contributions, feel free to contact me at [varsha.tambe2323@gmail.com].

---




