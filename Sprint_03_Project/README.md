# Introduction
This project involves analyzing data for the telecom operator Megaline, which offers two prepaid plans: Surf and Ultimate. The goal is to determine which plan generates more revenue to help the commercial department optimize their advertising budget. The analysis is based on data from 500 randomly selected customers in 2018, provided by the company.

# Purpose
This project aims to answer the following quesions:

1. Between the two plans, surf and ultimate, which of them generates more revenue for the Megaline company?
2. Do the users from different areas/regions generate different amount of revenue?

# Hypothesis
To answer the questions above, the following hypotheses are formulated:
1. The average revenue from users of the Ultimate and Surf calling plans differs.
2. The average revenue from users in the NY-NJ area is different from that of the users in the other regions.

# Data Description

The dataset for this project consists of five CSV files, each containing data related to Megaline’s customers and their usage of the Surf and Ultimate prepaid plans.

## 1. Users Table (`megaline_users.csv`)
Contains demographic and subscription data for each user:
- `user_id`: Unique identifier for each user.
- `first_name`: First name of the user.
- `last_name`: Last name of the user.
- `age`: Age of the user in years.
- `reg_date`: Date when the user subscribed to the service (format: dd-mm-yy).
- `churn_date`: Date when the user stopped using the service (missing if the user was still active when the data was extracted).
- `city`: User’s city of residence.
- `plan`: The calling plan the user is subscribed to (either "Surf" or "Ultimate").

## 2. Calls Table (`megaline_calls.csv`)
Contains data about the calls made by users:
- `id`: Unique identifier for each call.
- `call_date`: Date of the call.
- `duration`: Duration of the call (in minutes, rounded up).
- `user_id`: The unique identifier of the user who made the call.

## 3. Messages Table (`megaline_messages.csv`)
Contains data about text messages sent by users:
- `id`: Unique identifier for each text message.
- `message_date`: Date the text message was sent.
- `user_id`: The unique identifier of the user who sent the text.

## 4. Internet Table (`megaline_internet.csv`)
Contains data on internet usage by users:
- `id`: Unique identifier for each web session.
- `mb_used`: The volume of data used during the session (in megabytes).
- `session_date`: Date of the web session.
- `user_id`: The unique identifier of the user who used the data.

## 5. Plans Table (`megaline_plans.csv`)
Contains information about the two available prepaid plans (Surf and Ultimate):
- `plan_name`: Name of the calling plan (either "Surf" or "Ultimate").
- `usd_monthly_fee`: Monthly subscription fee for the plan (in US dollars).
- `minutes_included`: Number of minutes included in the plan per month.
- `messages_included`: Number of text messages included in the plan per month.
- `mb_per_month_included`: Amount of internet data included in the plan per month (in megabytes).
- `usd_per_minute`: Cost per minute for any calls that exceed the included minutes.
- `usd_per_message`: Cost per text message after the included messages are used up.
- `usd_per_gb`: Cost per extra gigabyte of data once the included data is exceeded (1 GB = 1024 MB).

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scipy