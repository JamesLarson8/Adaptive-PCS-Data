import geopandas as gpd

# Read the shapefile into a GeoDataFrame
shapefile = 'path/to/yourfile.shp'  # Replace with the path to your .shp file
gdf = gpd.read_file(shapefile)

# Display the first few rows to see what fields are available
print(gdf.head())

# Extract coordinate data (geometry)
gdf['latitude'] = gdf.geometry.y
gdf['longitude'] = gdf.geometry.x

# If there's a time attribute, extract it (replace 'time_field' with the actual field name)
if 'time_field' in gdf.columns:
    time_data = gdf['time_field']
else:
    time_data = None

# Save the extracted data to a CSV file
gdf[['latitude', 'longitude', 'time_field']].to_csv('extracted_data.csv', index=False)
print("Location and time data extracted to 'extracted_data.csv'")
