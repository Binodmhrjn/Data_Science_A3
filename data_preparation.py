import pandas as pd

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

# Alternatively, you can fill missing values with the mean of the column
# merged_data_cleaned = merged_data.fillna(merged_data.mean())

# Create a new column for total screen time by summing screen time columns for weekdays and weekends
merged_data_cleaned['Total_Screen_Time'] = merged_data_cleaned[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

# Save the cleaned data to a CSV file for later use
merged_data_cleaned.to_csv('./cleaned_data.csv', index=False)

print("Cleaned data has been saved to cleaned_data.csv")




