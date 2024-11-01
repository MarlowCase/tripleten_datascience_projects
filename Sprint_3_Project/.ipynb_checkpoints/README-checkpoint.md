# Introduction
This project focuses on analyzing grocery shopping habits using data from the Instacart platform. Instacart is a popular online grocery delivery service, and the dataset provided contains information on customer orders, products, departments, and aisles. The aim of this porject is to clean and analyze the data to uncover trends and insights into customer shopping behavior. 

The dataset was originally released for a Kaggle competition and has been modified for this project by introducing missing and duplicate values to simulate real-world data challenges. 

# Purpose
The primary objective of this project is to apply Exploratory Data Analysis (EDA) techniques to better understand the shopping habits of Instacart users. By cleaning, transforming, and visualizing the data, we aim to:
- Identify patterns in when and how customers place their orders.
- Analyze customer behaviors such as reorder habits and time between orders.
- Uncover which products are ordered most frequently and the order they are added to the cart. 
- Use this analysis to better understand customer behavior, which could ultimately help Instacart improve customer experience and optimize operations. 

# Data Descriptions
**The total dataset consists of five CSV files:**
1. **instacart_orders.csv:** Contains order information.
2. **products.csv:** A list of products available for purchase.
3. **order_products.csv:** Details of the products ordered in each order.
4. **aisles.csv:** Aisle categories for the products.
5. **departments.csv:** Department categories for the products.

## Data Dictionary
**instacart_orders.csv**
- `order_id`: Unique ID for each order.
- `user_id`: Unique ID for each customer.
- `order_number`: The sequence number of the order for each customer.
- `order_dow`: Day of the week the order was placed (0–6).
- `order_hour_of_day`: The hour of the day the order was placed (0–23).
- `days_since_prior_order`: Days since the customer’s previous order.

**products.csv**
- `product_id`: Unique ID for each product.
- `product_name`: Name of the product.
- `aisle_id`: Aisle ID.
- `department_id`: Department ID.

**order_products.csv**
- `order_id`: Unique ID for each order.
- `product_id`: Unique ID for each product ordered.
- `add_to_cart_order`: Sequence in which the product was added to the cart.
- `reordered`: Whether the product was reordered (0 = no, 1 = yes).

**aisles.csv**
- `aisle_id`: Unique aisle ID.
- `aisle`: Name of the aisle.

**departments.csv**
- `department_id`: Unique department ID.
- `department`: Name of the department.

# Data Preprocessing
The data preprocessing stage involved cleaning the data and preparing it for analysis:
1. **Handling missing values**: Identified and filled missing values where appropriate.
2. **Removing duplicates**: Identified and removed duplicate entries.
3. **Data type verification**: Ensured the correct data types for each column, especially ID columns as integers.

# Data Analysis and Visualizations
This project includes the following analyses:
1. **Order patterns**:
   - Analysis of order frequency by hour of the day and day of the week.
   - Visualization of how long customers wait between orders.
   
2. **Customer behavior**:
   - Comparison of order patterns between different days of the week (e.g., Wednesdays vs. Saturdays).
   - Visualization of the distribution of the number of orders placed by customers.
   
3. **Product insights**:
   - Identification of the top 20 most frequently ordered products.
   - Analysis of reorder habits, including the most frequently reordered items.
   
4. **Advanced product analysis** (optional):
   - Proportions of reorders for each product.
   - Insights into the first product added to the cart in each order.

# Main Libraries Used
- Pandas
- NumPy
- Matplotlib

# Table of Contents
1. Duplicate Values
2. Missing Values
3. Easy Tasks
	- Verify the Order hours and days of the week are sensible.
	- What time of day do people shop for groceries?
	- What day of the week do people shop for groceries?
	- How long do people wait until placing another order?
4. Medium Tasks
	- Is there a difference in `hour_of_day` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.
	- What's the distribution for the number of orders per customer?
	- What are the top 20 popular products (display their ID and Name)?
5. Hard Tasks
	- How many items do people typically buy in one order? What does the distribution look like?
	- What are the top 20 items that are reordered most frequently (display their Names and product IDs)?
	- For each product, what proportion of its orders are reorders?
	- For each customer, what proportion of their products ordered are reorders?
	- What are the top 20 items that people put in their carts first?
