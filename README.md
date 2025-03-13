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

## How to Run
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed and the required libraries are installed.
3. Save the script as `clean_sales_data.py` in your chosen directory.
4. Update the file paths in `clean_sales_data.py` if needed to match your system.
5. Run the script:
   ```bash
   python clean_sales_data.py
6. Verify output files (sales_data_raw.csv, sales_data_cleaned.csv, and unit_price_distribution.png) are generated in your directory.
   
## Visualizations

## Static Boxplot (unit_price_distribution.png): 
A Matplotlib boxplot showing the distribution of Unit Price after cleaning, highlighting the removal of outliers.

## Observations and Analyses
The sales_data_raw.csv contains synthetic sales data for May 2025, with intentional issues like missing values, duplicates, and an outlier (e.g., $1000 Unit Price).
After cleaning, sales_data_cleaned.csv reflects a dataset with consistent Region values ("SP", "RJ", "MG") and no outliers beyond the IQR range.
The boxplot confirms the removal of extreme values, ensuring data quality for further analysis.

## License
This content, including the script, documentation, and generated files, is the intellectual property of its creator. Unauthorized use, reproduction, or distribution of this content without prior written permission is strictly prohibited. Please contact renatofraga.rr@gmail.com for inquiries.
