# Data Cleaning Sales Pipeline

## Objective
This project applies data cleaning techniques to a fictional sales dataset using Python and the Pandas library. The goal is to identify and correct common issues such as missing values, duplicates, inconsistencies, and outliers, preparing the data for analysis.

## Project Structure
- `clean_sales_data.py`: Main script that performs data cleaning.
- `sales_data_raw.csv`: Original dataset with issues (generated automatically).
- `sales_data_cleaned.csv`: Cleaned dataset after processing.
- `unit_price_distribution.png`: Boxplot showing the distribution of `Unit Price` after cleaning.

## Script Steps
1. **Create Fictional Dataset**:
   - Generates sales data for May 2025 with columns: `Date`, `Product`, `Quantity`, `Unit Price`, `Region`, `Total Sale`.
   - Intentionally adds missing values, duplicates, and outliers.
2. **Identify Issues**:
   - Uses `describe()` and `isnull().sum()` for descriptive statistics and missing value counts.
   - Checks duplicates with `duplicated().sum()`.
3. **Remove Duplicates**:
   - Uses `drop_duplicates()` to remove duplicate rows.
4. **Handle Missing Values**:
   - Fills `Quantity` and `Unit Price` with their medians using `fillna()`.
5. **Standardize Data**:
   - Standardizes the `Region` column (e.g., "Sao Paulo" → "SP") with `replace()`.
6. **Remove Outliers**:
   - Removes outliers in `Unit Price` using the IQR (Interquartile Range) method.
7. **Visualization**:
   - Generates a boxplot to visualize the `Unit Price` distribution after cleaning.
8. **Save Results**:
   - Saves the cleaned dataset to `sales_data_cleaned.csv`.
