# Begin code for Sprint 4 project
import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Sprint 4 Project - Vehicle Ads')

# Load and Pre-Process Data
filepath = 'vehicles_us.csv'
unedited_df = pd.read_csv(filepath)

@st.cache_data
def pre_process(df_vhs):
    cols = df_vhs.columns
    df_vhs.rename(columns={x:x.strip().replace('_', ' ').title() for x in cols}, inplace=True)
    df_vhs.rename(columns={'Is 4Wd':'Is 4wd'}, inplace=True)

    df_merc = df_vhs.query("Price == 34900 and Model == 'mercedes-benz benze sprinter 2500'")
    df_merc_2 = df_merc.query("index != 42")
    df_vhs = df_vhs.drop(index=df_merc_2.index)

    df_vhs['Model Year'] = df_vhs.groupby('Model')['Model Year'].transform(lambda x: x.fillna(x.median())) 
    df_vhs['Odometer'] = df_vhs.groupby(['Model','Model Year'])['Odometer'].transform(lambda x: x.fillna(x.median()))

    global_odo_median = df_vhs['Odometer'].median()
    df_vhs['Odometer'] = df_vhs['Odometer'].fillna(global_odo_median) #fills with global median for those that don't have a model median
    df_vhs['Is 4wd'] = df_vhs['Is 4wd'].fillna(0)
    df_vhs['Paint Color'] = df_vhs['Paint Color'].fillna('unknown')
    
    cols = ['Model Year','Is 4wd','Odometer']
    for element in cols:
        df_vhs[element] = df_vhs[element].astype('int')

    df_vhs['Date Posted'] = pd.to_datetime(df_vhs['Date Posted'])
    df_vhs['Manufacturer'] = df_vhs['Model'].str.split().str[0]
    
    df_high_price = df_vhs.query("Price >= 300000") #only 1 result
    df_vhs = df_vhs.drop(index=df_high_price.index)

    return df_vhs

@st.cache_data    
def remove_outliers_per_manu(df):
    df_manu = pd.DataFrame() #blank new DF
    manus = df['Manufacturer'].unique() #obtain all manus
    for manu in manus:
        manu_group = df[df['Manufacturer'] == manu]
        quantile_25 = manu_group['Price'].quantile(0.25)
        quantile_75 = manu_group['Price'].quantile(0.75)
        price_iqr = quantile_75 - quantile_25
        
        filtered_manu_group = manu_group[(manu_group['Price'] >= (quantile_25 - 1.5*price_iqr)) & 
                                         (manu_group['Price'] <= (quantile_75 + 1.5*price_iqr))]
        
        df_manu = pd.concat([df_manu, filtered_manu_group], axis=0).reset_index(drop=True)
        
    return df_manu
    
@st.cache_data
def remove_odo_outs_per_manu(df):
    df_odo = pd.DataFrame()
    manus = df['Manufacturer'].unique()
    for manu in manus:
        manu_group = df[df['Manufacturer'] == manu]
        quantile_25 = manu_group['Odometer'].quantile(0.25)
        quantile_75 = manu_group['Odometer'].quantile(0.75)
        odo_iqr = quantile_75 - quantile_25
        
        filtered_manu_odo = manu_group[(manu_group['Odometer'] >= (quantile_25 - 1.5*odo_iqr)) & 
                                         (manu_group['Odometer'] <= (quantile_75 + 1.5*odo_iqr))]
        
        df_odo = pd.concat([df_odo, filtered_manu_odo], axis=0).reset_index(drop=True)
    
    return df_odo
        
# Create DF using function with all pre-processing and correct model year
df_vhs = pre_process(unedited_df)
#st.dataframe(df_vhs.style.format({'Model Year': '{:.0f}'}))

# Interactive Data Viewer - with checkboxes
st.sidebar.header('Filters for Raw Data:')

price_outliers = st.sidebar.checkbox('Remove all price outliers per manufacturer', value=False)
if price_outliers:
    df_vhs = remove_outliers_per_manu(df_vhs)
#else:
#    df_vhs = pre_process(unedited_df)
    
odo_outliers = st.sidebar.checkbox('Remove all mileage outliers per manufacturer', value=False)
if odo_outliers:
    df_vhs = remove_odo_outs_per_manu(df_vhs)
#else:
 #   df_vhs = pre_process(unedited_df)

small_manus = st.sidebar.checkbox('Include manufacturers with less than 1000 ads', value=True)
if not small_manus:
    manu_counts = df_vhs['Manufacturer'].value_counts()
    large_manus = manu_counts[manu_counts >= 1000].index #grabs manus
    df_vhs = df_vhs[df_vhs['Manufacturer'].isin(large_manus)]

mileage_threshold = st.sidebar.number_input('Mileage threshold (enter value to filter for maximum mileage)', min_value=0, value=150000)
user_odos = st.sidebar.checkbox(f"Include only ads with with under {mileage_threshold} miles", value=False)

if user_odos:
    df_vhs = df_vhs[df_vhs['Odometer'] < mileage_threshold]

st.subheader('Raw Data Viewer')
st.write(df_vhs)

# Histogram for Price across all vehicles
price_hist = px.histogram(df_vhs, x='Price', color='Condition', title='Distribution of All Vehicle Prices')

# Box plot for price by manufacturer
price_box_manu = px.box(df_vhs, x='Manufacturer', y='Price', title='Price by Manufacturer')

# Box plot for mileage by manufacturer
mileage_box_manu = px.box(df_vhs, x='Manufacturer', y='Odometer', title='Mileage by Manufacturer')

# Scatter of price vs mileage
scat_price_odo = px.scatter(df_vhs, x='Odometer', y='Price', color='Condition', 
    title='Scatterplot Distribution of Price vs Mileage by Condition')

# Bar chart for vehicle types by manufacturers
vehicle_types = df_vhs['Type'].unique().tolist() #lists the vehicle types
st.sidebar.header('Filter for Type Bar Chart:')
selected_types = st.sidebar.multiselect('Select Vehicle Types to Display', vehicle_types, default='sedan')

filtered_types = df_vhs[df_vhs['Type'].isin(selected_types)]
counts_per_type = filtered_types.groupby(['Manufacturer', 'Type']).size().reset_index(name='Count')
vehicle_type_bar = px.bar(counts_per_type, x='Manufacturer', y='Count', color='Type', barmode='group', 
    title='Number of Ads per Vehicle Types by Manufacturer')

# Histogram for condition vs model year
conditions = df_vhs['Condition'].unique().tolist()
st.sidebar.header('Filters for Condition Chart')
selected_condition = st.sidebar.multiselect('Select Vehicle Conditions to Display',conditions, default='good')

    #Input to control the years shown - for fun
year_threshold = st.sidebar.number_input('Year threshold (enter the value to filter for max year)', 
    min_value=df_vhs['Model Year'].min(), value=2000)
user_years = st.sidebar.checkbox(f"Implement selected maximum year to display",  value=False)

df_user_years = df_vhs.copy()
if user_years:
    #df_user_years = df_user_years.query(f"Model Year >= {year_threshold}")
    df_user_years = df_user_years[df_user_years['Model Year'] >= year_threshold]

cond_hist = px.histogram(df_user_years[df_user_years['Condition'].isin(selected_condition)], x='Model Year', 
    color='Condition', title='Distribution of Model Year for Conditions')

# Line chart for Average Price over Time
price_over_time = df_vhs.groupby('Date Posted')['Price'].mean().reset_index()
price_line = px.line(price_over_time, x='Date Posted', y='Price', title='Average Price over Time (days)')


st.plotly_chart(price_hist)
st.plotly_chart(price_box_manu)
st.plotly_chart(mileage_box_manu)
st.plotly_chart(scat_price_odo)
st.plotly_chart(vehicle_type_bar)
st.plotly_chart(cond_hist)
st.plotly_chart(price_line)
