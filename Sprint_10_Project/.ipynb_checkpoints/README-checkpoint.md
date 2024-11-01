# Introduction
Having been hired by OilyGiant, a mining company planning to choose a new region and develop new oil wells, our objective is to determine which region will have the highest profit margin.

OilyGiant has provided data on oil samples from three regions, detailing various parameters for each oil well in these regions, though specific parameter definitions are not provided. The objective is to build a machine learning model to identify the region with the highest profit potential. Additionally, an analysis of potential profit and associated risks will be conducted using the _Bootstrapping_ method.

# Project Objectives
1. **Data Split:** Split the data into a training and validation set in a 75:25 ratio.
2. **Model:** Train the model using linear regression.
3. **Volume of Reserves:** Calculate the volume of reserves required to develop a new well without incurring losses. Compare this to the average reserve volume in each region.
4. **Profit Calculation:** Estimate profit based on the top 200 wells with the highest predicted reserves.
5. **Bootstrapping:** Use 1,000 bootstrap samples to determine the profit distribution.
6. **Risk Assessment:** Only consider regions with a loss risk below 2.5%; select the region with the highest average profit among these.

# Data
Description of the data
*Features*
- `id`: unique oil well identifier
- `f0, f1, f2`: three features of points (their specific meaning is not important, but the features themselves are significant to predict the target)

*Target*
- `product`: volume of reserves in the oil well (thousand barrels)

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, and Scikit-Learn

# Table of Contents 
1. Introduction
2. Data Exploration
3. Exploratory Data Analysis
    - Distribution of the Features
    - Distribution of the Target
    - Correlation Analysis
4. Model Development
    - Model Performance
5. Profit Calculations
    - Variable Definitions
    - Minimum Volume of Reserves per Oil Well without Losses
    - Profit of Top 200 Oil Wells per Region
    - Bootstrapping and Resulting Distributions
6. Conclusion