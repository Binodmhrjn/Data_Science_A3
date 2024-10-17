import pandas as pd

# Load cleaned data
merged_data_cleaned = pd.read_csv('./cleaned_data.csv')

# Calculate the correlation matrix
corr_matrix = merged_data_cleaned[['Total_Screen_Time', 'Optm', 'Relx', 'Usef']].corr()
print("Correlation matrix:\n", corr_matrix)
