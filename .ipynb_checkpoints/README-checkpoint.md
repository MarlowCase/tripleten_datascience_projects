# Introduction
The Sweet Lift Taxi company has provided historical data on taxi orders at airports; the data covers the period from March through August of 2018. The company's goal is to predict the amount of taxi orders in the next hour, enabling the company to attract more taxi drivers during peak demand hours.

# Project Objective
As requested by Sweet Lift Taxi, the *RMSE* metric on the test set should not be more than **_48_**.

# Data
Description of the data

*Features:*
- `datetime`: Date and time of each observation. Provided to us at intervals of every 10 minutes.
 
*Target:*
- `num_orders`: Number of taxi orders at the corresponding date and time.

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Statmodels, LightGBM, ARIMA

# Table of Contents
1. Introduction
2. Imports
3. Data Exploration & Preprocessing
4. Exploratory Data Analysis
    - Hourly, Daily, Weekly, and Monthly Time Series Graphs
    - Mean Taxi Orders by Index
    - Trend & Seasonality
    - Stationarity
    - EDA Conclusion
5. Feature Creation
6. Model Training
7. Model Evaluations & Analysis
8. Conclusion