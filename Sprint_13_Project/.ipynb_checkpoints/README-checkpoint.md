# Introduction
The Sure Tomorrow insurance company wants to solve several tasks related to the customer insurance benefits. This project aims to solve the given tasks with machine learning models and secure the privacy of customer data.

# Project Objectives

This section outlines the key criteria Sure Tomorrow has requested for this project:

1. **Task 1:** Find customers who are similar to a given customer. This will help the company's agents with marketing.
2. **Task 2:** Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
3. **Task 3:** Predict the number of insurance benefits a new customer is likely to receive using a linear regression model.
4. **Task 4:** Protect clients' personal data without breaking the model from the previous task. It's necessary to develop a data transformation algorithm that would make it hard to recover personal information if the data fell into the wrong hands. This is called data masking, or data obfuscation. But the data should be protected in such a way that the quality of machine learning models doesn't suffer. You don't need to pick the best model, just prove that the algorithm works correctly.

# Data
Description of the data

*Features:*
- `gender`: customer's gender (we are unsure which number is male/female as it has already been encoded)
- `age`: customer's age
- `income`: customer's yearly income
- `family_members`: number of customer's family members (assuming in same household)

*Target:*
- `insurance_benefits`: number of insurance benefits received by an insured person over the last five years.

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

# Table of Contents
1. Project Objective Statement
2. Data Preprocessing & Exploration
3. Task 1
4. Task 2
5. Task 3
6. Task 4
7. Conclusions
8. Appendix