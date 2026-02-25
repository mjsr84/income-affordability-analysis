import os
import pandas as pd
from pathlib import Path

# Define paths.
metadata_path = Path('data') / 'raw' / 'ACSDP5Y2023.DP03-Column-Metadata.csv'
raw_csv_path = Path('data') / 'raw' / 'ACSDP5Y2023.DP03-Data.csv'
output_path = Path('data') / 'processed' / 'county_income_clean.csv'


# Load data.
metadata = pd.read_csv(metadata_path)
acs_data = pd.read_csv(raw_csv_path, header=0, skiprows=[1], low_memory=False)

# Locate target column.
income_col_row = metadata[metadata['Label'].str.contains('Median household income')]
income_col_name = income_col_row['Column Name'].values[0]
print("Median income column code: ", income_col_name)

# Rename columns.
col_map = {
    "GEO_ID": "geography_id",
    "NAME": "county_name",
    income_col_name: "median_household_income"
}
acs_clean = acs_data[list(col_map.keys())].rename(columns=col_map)
print("Cleaned ACS data sample (selected columns): ")
print(acs_clean.head())

# Removing commas (if any), converting to numeric, coerce errors (eg. (x)) into NaN
acs_clean['median_household_income'] = acs_clean['median_household_income'].replace({',': ''}, regex=True)
acs_clean['median_household_income'] = pd.to_numeric(acs_clean['median_household_income'], errors='coerce')
print("Rows with missing income values: ")
print(acs_clean[acs_clean['median_household_income'].isna()]) # Only found two examples with NaN, leaving them alone.
                                                    