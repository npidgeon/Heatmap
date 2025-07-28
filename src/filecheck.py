import geopandas as gpd

# This script checks if a shapefile can be loaded and lists its columns.
# Column names can then be used in the main.py script.
# IMPORTANT: Replace this with the actual path to your .shp file
shapefile_path = r""

try:
    gdf = gpd.read_file(shapefile_path)

    print("✅ Successfully loaded shapefile.")
    print("\nAvailable columns are:")
    print(gdf.columns) # This will list all column names

    print("\nHere is the first row of data to help you identify the right column:")
    print(gdf.head(1)) # Shows the first row and its values

except Exception as e:
    print(f"❌ An error occurred: {e}")
