# Introduction
This project aims to develop a binary classification model for the mobile carrier Megaline. The model aims to recommend one of the two phone plans: Smart or Ultra. The model will be developed by analyzing the existing subscriber's behavior data provided to us by the company (see sprint 3 project).

# Project Objective
The accuracy of the final model selected has to be 75% and above as requesterd by the Megaline company.

# Data
Description of the data provided
- `calls`: number of calls
- `minutes`: total call duration in minutes
- `messages`: number of text messages
- `mb_used`: internet traffic used in MB
- `is_ultra`: plan for the current month (Ultra - 1, Smart - 0)

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, and Scikit-Learn

# Table of Contents 
1. Introduction
    - Criteria 
2. Data Exploration
3. Exploratory Data Analysis
    - Distributions of Features
    - Distribution of Target
4. Development and Tuning of Different Models
    - Separating the Dataset
    - Decision Tree
    - Random Forest
    - Logistic Regression
5. Final Model Selection and Evaluation
    - Final Model Evalutation
6. Conclusion