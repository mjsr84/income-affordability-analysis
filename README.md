# Income & Affordability Analysis

## Project Overview
This project explores the relationship between household income, cost of living, and regional affordability.  
The goal is to move beyond raw income metrics and examine effective purchasing power across regions.

## Objectives
- Analyze household income distributions
- Compare income against cost-of-living factors
- Construct affordability metrics
- Identify regional patterns and outliers
- Build reproducible SQL-based analysis

## Tools & Technologies
- PostgreSQL (data storage & querying)
- SQL (analysis & transformations)
- Python (data processing)
- Power BI (visualization)
- VS Code (development environment)

## Data Processing Workflow
1. **Raw Data:** ACS 5-Year Estimates (DP03) CSVs
2. **Metadata Driven:** Dynamically identify the Median Household Income column using ACS Metadata
3. **Column Selection:** Keep only three columns:
    - 'GEO_ID' -> 'geograph_id' (stable county-level key)
    - 'NAME' -> 'county_name' (more intuitive)
    - Median household income -> 'median_household_income'
4. **Data Cleaning:**
    - Remove commas from income values
    - conver (x) or missing entries to 'NaN'
    - Retain two counties (Esmeralda County, NV and Kenedy County, TX) as 'NULL' for transparency
5. **Output:** Cleaned CSV ('county_income_clean.csv') ready for PostgreSQL import

## Analytical Focus
The analysis emphasizes:

- Median vs distributional income effects
- Cost distortion across regions
- Derived affordability ratios
- Window function usage
- Reproducible data workflows

## Project Status
Initial setup and repository structure created.  
Data ingestion and schema design in progress.

## Reproducibility
All analysis is designed to be reproducible from raw datasets using SQL queries and documented transformations.