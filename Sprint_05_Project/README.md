# Ice Video Game Sales Analysis

## Project Overview
This project is designed to analyze video game sales data for the online store **Ice**, which sells video games globally. The goal is to identify patterns that determine the success of a video game, allowing the company to predict potential winners and plan advertising campaigns effectively. 

The dataset goes back to 2016, and we will use it to build insights for the upcoming year (2017).

## Project Objective
The primary objective of this project is to:
- **Analyze** historical data on video games to find trends and patterns.
- **Identify** the factors that influence game success in terms of sales.
- **Make recommendations** for selecting games and platfroms to focus on in 2017 for advertising and marketing campaigns.

## Data Description
The dataset contains the following columnns:
- `Name`: The name of the game.
- `Platform`: The platform on which the game was released.
- `Year_of_Release`: The release year of the game.
- `Genre`: The genre of the game (e.g., Action, Sports).
- `NA_sales`: Sales in North America (in USD million).
- `EU_sales`: Sales in Europe (in USD million).
- `JP_sales`: Sales in Japan (in USD million).
- `Other_sales`: Sales in other regions (in USD million).
- `Critic_Score`: Game's score from professional critics (maximum of 100).
- `User_Score`: Game's user score (maximum of 10).
- `Rating`: ESRB rating (e.g., Teen, Mature).

## Project Workflow

The project is divided into the following steps:

### Step 1: Data Exploration
- Load and examine the dataset.
- Understand its structure and identify any potential issues with missing values or incorrect data types.

### Step 2: Data Preprocessing
- Rename columns to lowercase for consistency.
- Convert data to appropriate types (e.g., year, score values).
- Handle missing values and decide how to process the `TBD` values in the user scores.
- Add a new column for **total sales**, representing the sum of sales across all regions for each game.

### Step 3: Exploratory Data Analysis (EDA)
- Analyze the number of games released each year and check if the data is sufficient for analysis.
- Study platform-wise sales distribution over time, identifying leading and declining platforms.
- Determine the relevant data period for building predictions for 2017.
- Analyze sales trends by platform and genre, focusing on identifying potentially profitable platforms and genres.
- Examine the impact of **user** and **critic reviews** on sales using correlation analysis.

### Step 4: Regional User Profiles
- Identify the top platforms and genres for each region (North America, Europe, Japan).
- Investigate whether ESRB ratings influence sales in these regions.

### Step 5: Hypothesis Testing
Test two hypotheses:
1. **H₀ (Null Hypothesis)**: The average user ratings for Xbox One and PC platforms are the same.
2. **H₀ (Null Hypothesis)**: The average user ratings for the Action and Sports genres are different.

### Step 6: Conclusion
Summarize the key findings of the analysis, including recommendations for the **2017 marketing campaign**.

## Main Libraries Used
Pandas, NumPy, Matplotlib, SciPy, and Seaborn

## Table of Contents 
1. Introdcution
2. Data Exploration
3. Data Preprocessing
    - Column Headers, Data Types & Dimensionality Reductions
    - Erroneous Values
    - Missing Values
        - Name
        - Year of Release
        - Critic & User Scores
        - Rating
4. Exploratory Data Analysis
    - Number of Games Released per Year
    - Global Sales per Platform
    - Effect of User & Critic Reviews on Sales
    - Sales of the Same Games from Different Platforms
    - Distribution of Sales of Games per Genre
5. Regional Sales Analysis
    - Market Shares per Platform
    - Relationship between ESRB Rating and Game Sales
6. Hypothesis Testing
    - Average User Scores of the Xbox One and PC Platforms are the Same
    - Average User Scores for the Action and Sports Genres are Different
7. Conclusion