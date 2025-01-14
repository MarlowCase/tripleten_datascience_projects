# Introduction
The telecom operator _Interconnect_ would like to identify potential leaving clients. If they can discover that a client is planning to leave, they will offer the client special marketing packages. The Interconnect's marketing team has collected some of their clientele's personal data, including information about the clientele's plan and contract.

# Project Objective
1. To identify the characteristics and behaviors that distinguish between active clients and those who are likely to leave. 
2. To develop a machine learning model to predict client churn with an AUC-ROC score of at least 0.85.

# Data
Description of `contract`:

- `customerID`: A unique identifier for the client
- `BeginDate`: The date when the client started using our services.
- `EndDate`: The date the client terminated their existing contract.
    - A value of **No** indicates that the client is still using our services (_is an active client_).
- `Type`: The contract's payment subscription (_monthly, annually, bi-annually_).
- `PaperlessBilling`: Binary flag field describing whether the client is subscribed to digital billing.
- `PaymentMethod`: The method of payment for the subscribed services (_Eletronic Check, Mailed Check, etc._).
- `MonthlyCharges`: The amount charged to the client on a monthly basis.
- `TotalCharges`: The amount charged to the client over the lifespan of their subscription.

Description of `Internet`:

- `customerID`: A unique identifier for the client.
- `InternetService`: Details the type of internet hookup the client has (_DSL or Fiber optic_).
- `OnlineSecurity`: Binary flag indicating whether client is subscribed to the malware blocker. 
- `OnlineBackup`: Binary flag indicating whether the client is subscribed to the cloud storage and backup services.
- `DeviceProtection`: Binary flag indicating whether the client is subscribed to the antivirus software. 
- `TechSupport`: Binary flag indicating whether the client is subscribed to the technical support line.
- `StreamingTV`: Binary flag indicating whether the client is subscribed to TV streaming.
- `StreamingMovies`: Binary flag indicating whether the client is subscribed to the movie directory. 

Description of `Personal`:

- `customerID`: A unique identifier for the client.
- `gender`: Binary field indicating whether the client is male or female.
- `SeniorCitizen`: Binary field indicating whether the client is a senior citizen (_65 in the U.S._).
- `Partner`: Binary flag indicating whether the client has a partner or is single.
- `Dependents`: Binary flag indicating whether the client has other family members in the household they provide for.  

Description of `Phone`:

- `customerID`: A unique identifier for the client.
- `MultipleLines`: A binary flag indicating whether the client is subscribed to multiple phone lines. 

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Optuna, Tensorflow

# Table of Contents
1. Introduction
    - Purpose
	- Services Summary
	- Challenges
	- Objectives
2. Initializations
3. Data Exploration
    - Contract
	- Internet
	- Personal
	- Phone
	- Conclusion
4. Data Preprocessing
    - Merging the Datasets
	- Implementing Data Fixes
	- Feature Engineering
	    - Tenure
		- Service Types
		- Number of Internet services
		- Payment Method Reduction
		- Quarters
5. Exploratory Data Analysis (EDA)
    - Numerical Features
	- Categorical Features
	    - Chi-Squared Tests
	- Distribution of the Target Class
	- Monthly Payments
	- Percentages of Clients by Service type
	- Client Inflow and Outflow
	- Correlation Matrix
	- Conclusion
6. Model Development
    - Prepare Features & Target
	- Addressing Class Imbalance 
	- Model Performance Analysis Across Imbalance Correction Methods
	- Methodology
7. Model Training
    - Methodology
	- Base Model
	- Decision Tree
	- LogR
	- Decision Tree with Adaptive Boosting
	- CatBoost
	- XGBoost
	- LightGBM
	- Histogram Gradient Boosting
	- Neural Network
	- Stacking Ensemble
8. Final Model Selection & Evaluation
    - Final Model Selection
	- Feature Importances
	- Evaluation of the Final Model on the Test Set
9. General Conclusion
10. Recommendations
11. Appendix A: Saving Models
12. Appendix B: Preprocessing Notes
13. Appendix C: Work Plan
14. Appendix D: Challenges Faced