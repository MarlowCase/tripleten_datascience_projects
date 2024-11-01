/*
Find the number of taxi rides for each taxi company 
for November 15-16, 2017
*/
CREATE TABLE company_avg_trips AS

SELECT 
cabs.company_name,
COUNT(trips.trip_id) AS trips_amount

FROM cabs

INNER JOIN trips
  ON trips.cab_id = cabs.cab_id
    
WHERE 0=0
AND CAST(trips.start_ts AS DATE) BETWEEN '2017-11-15' AND '2017-11-16'

GROUP BY
cabs.company_name

ORDER BY
trips_amount DESC;

/*
Find the number of rides for every taxi company whose name 
contains the words "Yellow" or "Blue" for November 1-7, 2017
*/
SELECT 
cabs.company_name,
COUNT(trips.trip_id) AS trips_amount

FROM trips

INNER JOIN cabs
  ON cabs.cab_id = trips.cab_id
    
WHERE 0=0
AND CAST(trips.start_ts AS DATE) BETWEEN '2017-11-1' AND '2017-11-07'
AND (cabs.company_name LIKE '%Blue%' OR cabs.company_name LIKE '%Yellow%')

GROUP BY 
cabs.company_name;
	
/*
Find the number of rides for Flash Cab and Taxi Affiliation Services
for November 1-7
*/
SELECT 
CASE 
    WHEN cabs.company_name IN ('Flash Cab', 'Taxi Affiliation Services') THEN cabs.company_name
    ELSE 'Other'
    END AS company,
COUNT(trips.trip_id) AS trips_amount

FROM trips

INNER JOIN cabs
  ON cabs.cab_id = trips.cab_id

WHERE 0=0
AND CAST(trips.start_ts AS DATE) BETWEEN '2017-11-1' AND '2017-11-7' 

GROUP BY 
company

ORDER BY 
trips_amount DESC;

/*
Retrieve the identifiers of the O'Hare and Loop
neighborhoods from the neighborhoods table
*/
SELECT 
n.neighborhood_id,
n.name

FROM neighborhoods n

WHERE 0=0 
AND n.name IN ('%O''Hare%', 'Loop');
	
/*
For each hour, retrieve the weather condition records
*/
SELECT 
wr.ts,
CASE 
    WHEN wr.description IN ('%rain%', '%storm%') THEN 'Bad'
    ELSE 'Good'
    END AS weather_conditions

FROM weather_records wr;
	
/*
Retrieve all the rides that started in the Loop (pickup_location_id: 50) 
on a Saturday and ended at O'Hare (dropoff_location_id: 63)
Get the weather conditions for each ride
*/
SELECT 
trips.start_ts,
SUB.weather_conditions,
trips.duration_seconds

FROM trips

INNER JOIN (
    SELECT 
    wr.ts,
    CASE 
        WHEN wr.description IN ('%rain%', '%storm%') THEN 'Bad'
        ELSE 'Good'
        END AS weather_conditions
    
    FROM weather_records wr
) AS SUB
  ON SUB.ts = trips.start_ts

WHERE 0=0
AND trips.pickup_location_id = 50  --Loop
AND trips.dropoff_location_id = 63 --O'Hare
and EXTRACT(DOW FROM CAST(trips.start_ts AS DATE)) = 6; --Saturday