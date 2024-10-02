from simpledbf import Dbf5
import pandas as pd

# Load the .dbf file
dbf = Dbf5('Sandy.dbf')

# Convert to pandas DataFrame
df = dbf.to_dataframe()

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

print("Conversion complete! Saved as 'Sandyoutput.csv'.")
