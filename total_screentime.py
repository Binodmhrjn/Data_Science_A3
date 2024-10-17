import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
dataset1 = pd.read_csv('./dataset1.csv')  # Demographics dataset
dataset2 = pd.read_csv('./dataset2.csv')  # Screen Time dataset
dataset3 = pd.read_csv('./dataset3.csv')  # Well-being dataset

# Merge the datasets on the 'ID' column
merged_data = pd.merge(dataset1, dataset2, on='ID', how='inner')
merged_data = pd.merge(merged_data, dataset3, on='ID', how='inner')

# Display the first few rows of the merged dataset to verify
print(merged_data.head())

# Check for missing values in the merged dataset
missing_data = merged_data.isnull().sum()
print("Missing values in each column:\n", missing_data)

# Drop rows with missing values (if necessary)
merged_data_cleaned = merged_data.dropna()
print("Cleaned data preview:\n", merged_data_cleaned.head())

# Create a new column for total screen time by summing screen time columns for weekdays and weekends
merged_data_cleaned['Total_Screen_Time'] = merged_data_cleaned[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

# Verify the newly created column
print(merged_data_cleaned[['Total_Screen_Time', 'C_we', 'C_wk']].head())

# Ensure that Total_Screen_Time and Optm are numeric
merged_data_cleaned['Total_Screen_Time'] = pd.to_numeric(merged_data_cleaned['Total_Screen_Time'], errors='coerce')
merged_data_cleaned['Optm'] = pd.to_numeric(merged_data_cleaned['Optm'], errors='coerce')

# Filter out rows with invalid data (e.g., zero or negative screen time or optimism)
filtered_data = merged_data_cleaned[(merged_data_cleaned['Total_Screen_Time'] > 0) & (merged_data_cleaned['Optm'] > 0)]

# Check data for filtered dataset
print("Filtered data preview:\n", filtered_data[['Total_Screen_Time', 'Optm']].head())

# Scatter plot: Total screen time vs Optimism
plt.scatter(filtered_data['Total_Screen_Time'], filtered_data['Optm'])
plt.title('Total Screen Time vs Optimism')
plt.xlabel('Total Screen Time (hours)')
plt.ylabel('Optimism')
plt.show()
