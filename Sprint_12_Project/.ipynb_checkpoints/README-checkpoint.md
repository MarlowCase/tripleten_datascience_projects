# Introduction
Zyfra, an efficiency solutions provider for heavy industries, has contracted us to develop a machine learning model prototype aimed at increasing efficiency in mining technology. The project’s objective is to predict the amount of gold recovered from gold ore during the mining process — a metric known as "gold recovery." Zyfra has supplied separate test and training datasets, along with a combined datasheet. We have the flexibility to determine which information is essential for model development. The model will target two key predictions: rough concentrate recovery and final concentrate recovery, which represent intermediate and final stages of the gold recovery process.

# Project Objectives

This section outlines the key criteria Zyfra has requested for this project:

1. **Validate Recovery Calculations**: Ensure that the provided recovery calculations are accurate.
2. **Feature Analysis**: Identify and analyze features that are not included in the test set.
3. **Target Addition**: Add target variables to the test set.
4. **Feed Particle Size Comparison**: Compare feed particle size distributions between the training and test sets.
5. **Anomaly Detection**: Identify any anomalous data points in the concentration levels of all substances.
6. **sMAPE Calculation**: Develop a function to calculate symmetric Mean Absolute Percentage Error (sMAPE).
7. **Model Training and Evaluation**: Train multiple models and evaluate performance using cross-validation.

# Data
Description of the data

- `date`: the exact datetime of the gold extraction process

Other columns follow this format: **`[stage].[parameter_type].[parameter_name]`**

*Possible values for `[stage]`:*
- _**rougher:**_ flotation
- _**primary_cleaner:**_ primary purification (_stage 1 of cleaning_)
- _**secondary_cleaner:**_ secondary purification (_stage 2 of cleaning_)
- _**final:**_ final characteristics

*Possible values for `[parameter_type]`:*
- _**input:**_ raw material parameters
- _**output:**_ product parameters (_tail and concentrate_)
- _**state:**_ parameters characterizing the current state of the stage
    - <small>the **state** parameter essentially refers to variables that describe the current operating conditions or physical state of the machinery and environment at each stage in the processing operation.</small>
- _**calculation:**_ calculation characteristic

*Possible values for `[parameter_name]`*
- `_air`: volume of air
- `_level`: fluid level
- `feed_size`: size of the feed particle
- `feed_rate`: feeding speed
- `concentrate_`: percentage of the substance in the concentrate
- `tail_`: percentage of the substance in the rougher tails
- `recovery`: gold recovery in percentage

*Targets*
- `rougher.output.recovery`
- `final.output.recovery` 

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, CatBoost, XGBoost

# Table of Contents 
1. Introduction
    - Ore Processing Stages
    - Terminology
    - Formulas
    - Project Criteria
2. Data Exploration
    - Column Naming Convention
    - Conclusion
3. Data Preprocessing
    - Checking Rougher Recovery
    - Train Features vs. Test Features
    - Missing Values
4. Exploratory Data Analysis
    - Change in Concentrations of Metals per Purification Stage
    - Distribution of Feed Size in Training Set vs. Test Set
    - Total Concentrations at Different Stages
5. Feature Processing
    - Separate into Target and Features
    - Feature Scaling
6. Model Development
    - Training Multiple Models
    - Tuning Hyperparameters of Top 3 Models
7. Conclusion
8. Appendix