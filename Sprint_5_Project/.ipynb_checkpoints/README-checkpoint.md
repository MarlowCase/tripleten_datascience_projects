# TT-Sprint_4_Project
The project for sprint 4

In order to view the application associated with the code in app.py, go to this link: https://tt-sprint-4-project.onrender.com

This application opens the vehicles_us.csv data and and allows the user to apply various filtering methods that are outlined in more detail below.
In addition to opening the file, it also applies all preprocessing functions to the data as well - that is outlined in the code in app.py.

Summary of EDA: 
- Main concern is missing values. 
- Price:       Will replace missing values with average for that model and year
- Odometer:    Will replace missing values with median for that model
- Model Year:  Can use the model to replace this, otherwise it will be missing
- paint color: irrelevant
- is 4wd:      irrelevant - is a flag field so first confirm any real nulls, if only one value, then fill with opposite value
- date fields: cannont replace

Featured visualizations:
- price distribution across all data
    - User can filter on price outliers, mileage outliers, size of manufacturers, and mileage of car
	- these filters effect entire viewed data set to see how other charts adjust
- price distribution per each manufacturer
- mileage distribution per each manufacturer
- mileage scatterplot per condition
    - User can select conditions to display
- number of ads per vehicle type by manufacturer
    - User can filter based on car type
- Model Year frequency distribution per condition
    - User can filter on condition.
- line chart showing average price of all adss over time
	
