# Anonymous US Density Heatmap from CSV 

This is a simple Python script that uses a CSV file of coordinates in conjunction with US national 
shapefile data to plot a density heatmap using Folium. Coordinates are jittered using a random offset 
of up to 500 meters, adding some anonymity while preserving the general location of each point. Currently, 
the script uses national shapefile data (accessed at https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_nation_5m.zip), 
and will display coordinates in Hawaii, Alaska, and US territories. 

It's configured to work with the CSV file in an S3 bucket (using boto3 functions to access) for anonymity's sake, 
but you can also place a CSV in the data directory on your machine, change the csv_data initialization on line 187 
to the filepath, for example "data/source_data.csv" and comment out the AWS-related lines (165-177, 186).

## Usage

Ensure that a CSV with proper column names ('lat' and 'long' are defaults) is in an S3 bucket. 
Change the values of aws_key, aws_secret, bucket_name, and file_key to your environment variable names. 
Filecheck.py can be used to confirm that you have a valid shapefile and display the column names, 
but shouldn't be necessary unless you've modified something or are using state/regional shapefiles instead of the national .shp.


##  Contributing / Updates

PRs accepted, I plan to continue iterating on this as a personal project to make it more useful. Current plans include 
adding better handling for state/regional/international scope, including commented-out functions for using local 
source data instead of S3, and refining the color scheme, blur/radius settings, and legend to optimize readability and visual appeal.

## License

MIT License

Copyright (c) 2025 Nicholas Pidgeon

