# Introduction
This project aims to develop a binary classification model for Beta Bank, because the bank is losing its customer base little by little every month! However, the bank has discovered that it is more cost-effective to retain the existing customers than to attract new ones. The model's objective is to predict whether a customer will leave the bank soon using the provided data on clients' past behavior.

# Project Objectives
1. Train the model without taking into account the imbalance as requested by Beta Bank.
2. Improve the quality of the model using at least two different approaches to fixing class imbalance.
3. Must train more than one model to find the best option.
4. Must use a training and validation set; once the best model is found, test it with a test set.
5. The final model selected must have an F1 score of at least 0.59

# Data
Description of the data *features*
- `row_number`: data string index
- `customer_id`: unique customer identifier
- `surname`: customer name
- `credit_score`: customer credit score
- `geography`: country of residence
- `gender`: customer gender
- `age`: customer age
- `tenure`: period of maturation for a customer's fixed deposit (_years_)
- `balance`: customer account balance
- `num_of_products`: number of banking products used by the customer
- `has_cr_card`: customer has a credit card
- `is_active_member`: customer's activeness
- `estimated_salary`: estimated salary

*Target*
- `exited`: customer has left

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

# Table of Contents 
1. Introduction
    - Criteria 
2. Data Exploration
    - Data Description
    - Issues
3. Data Preprocessing
    - Missing Values
4. Exploratory Data Analysis
    - Distributions of Numerical Features
    - Distributions of Categorical Features
    - Distribution of the Target Classes
5. Feature Processing
    - Encoding
    - Log Transformation
    - Feature Scaling
6. Development and Tuning of Different Models
    - Functions
    - Baseline Models
    - Class Weight Adjustment
    - Upsampling
      - One to One
    - Downsampling
       - One to One
7. Final Model Selection and Evaluation
    - Threshold Adjustments
    - F1-Score, Precision, and Recall
    - Testing the Filled Data
    - ROC & AUC-ROC
8. Conclusion
       