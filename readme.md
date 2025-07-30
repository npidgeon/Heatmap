# Anonymous US Density Heatmap from CSV 

This is a simple Python script that uses a CSV file of coordinates in conjunction with US national 
shapefile data to generate a density heatmap using Folium, pandas/geopandas and LeafletJS. Coordinates are jittered using a random offset 
of up to 500 meters, adding some anonymity while preserving the general location of each point. Currently, 
the script uses national shapefile data (accessed at https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_nation_5m.zip), 
and will display coordinates in Hawaii, Alaska, and US territories. The output is an HTML file.

It's configured to work with the CSV file in an S3 bucket (using boto3 functions to access) for anonymity's sake, 
but you can also place a CSV in the data directory on your machine, change the csv_data initialization on line 187 
to the filepath, for example "data/source_data.csv" and comment out the AWS-related lines (165-177, 186). 

If anonymity isn't a concern, you can simply set the PRIVACY_RADIUS_METERS variable to 0. Note that
all coordinates are easily accessible in the HTML file.

## Prerequisites

pandas,
geopandas,
folium,
boto3,
numpy

You can install the required Python packages using pip:
    `pip install -r requirements.txt`

## Usage

Ensure that a CSV with proper column names ('lat' and 'long' are defaults) is in an S3 bucket. 
This script reads AWS credentials from your environment variables. Before running, set the following variables
in your terminal:

For **bash**, **zsh**, etc:
```bash
export HEATMAP_AWS_ACCESS_KEY_ID="YOUR_KEY_HERE"
export HEATMAP_AWS_SECRET_ACCESS_KEY="YOUR_SECRET_HERE"
export HEATMAP_S3_BUCKET_NAME="your-bucket-name"
export HEATMAP_S3_FILE_KEY="path/to/your/file.csv"
```

For PowerShell:
```powershell
$env:HEATMAP_AWS_ACCESS_KEY_ID="YOUR_KEY_HERE"
$env:HEATMAP_AWS_SECRET_ACCESS_KEY="YOUR_SECRET_HERE"
$env:HEATMAP_S3_BUCKET_NAME="your-bucket-name"
$env:HEATMAP_S3_FILE_KEY="path/to/your/file.csv"
```

Filecheck.py can be used to confirm that you have a valid shapefile and display the column names, 
but shouldn't be necessary unless you've modified something or are using state/regional shapefiles instead of the national .shp.


## Example
Eastern US using default settings for folium.Map()

<img width="1317" height="1010" alt="Image" src="https://github.com/user-attachments/assets/22def057-d6b3-4a51-bf61-24a40338c3e0" />


##  Contributing / Updates

PRs accepted, I plan to continue iterating on this as a personal project to make it more useful. Current plans include 
adding better handling for state/regional/international scope, including commented-out functions for using local 
source data instead of S3, and refining the color scheme, blur/radius settings, and legend to optimize readability and visual appeal.

## License
MIT License

Copyright (c) 2025 Nicholas Pidgeon

