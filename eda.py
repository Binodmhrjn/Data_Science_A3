import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data (from the previous data preparation step)
merged_data_cleaned = pd.read_csv('./cleaned_data.csv')

# Step 1: Descriptive Statistics
print(merged_data_cleaned[['Total_Screen_Time', 'Optm', 'Relx', 'Usef']].describe())


# Step 2: Histogram for Total Screen Time
plt.hist(merged_data_cleaned['Total_Screen_Time'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Total Screen Time')
plt.xlabel('Total Screen Time (hours)')
plt.ylabel('Frequency')
plt.show()



# Step 3: Histogram for Optimism (Optm)
plt.hist(merged_data_cleaned['Optm'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Optimism Scores')
plt.xlabel('Optimism Score')
plt.ylabel('Frequency')
plt.show()
