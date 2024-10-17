import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data (from the previous data preparation step)
merged_data_cleaned = pd.read_csv('./cleaned_data.csv')

# Step 1: Descriptive Statistics
print(merged_data_cleaned[['Total_Screen_Time', 'Optm', 'Relx', 'Usef']].describe())

# Step 2: Scatter Plot
plt.scatter(merged_data_cleaned['Total_Screen_Time'], merged_data_cleaned['Optm'])
plt.title('Total Screen Time vs Optimism')
plt.xlabel('Total Screen Time (hours)')
plt.ylabel('Optimism')
plt.show()

# Step 3 Correlation Heatmap
sns.heatmap(merged_data_cleaned[['Total_Screen_Time', 'Optm', 'Relx', 'Usef']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Screen Time and Well-being Metrics')
plt.show()

