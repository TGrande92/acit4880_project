import pandas as pd

#load the data
df = pd.read_csv("./wind_speed_annual/wind_speed_annual.csv")

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate daily average wind speed for each block
df['Avg_Wind_Speed'] = df[[f"Hour {i:02} Wind Speed" for i in range(24)]].mean(axis=1)

# Drop hourly columns
columns_to_drop = [f"Hour {i:02} {param}" for i in range(24) for param in ["Wind Speed", "Weibull C", "Weibull K"]]
df = df.drop(columns=columns_to_drop)

# Using paixrplot to visualize relationships between continuous variables:
sns.pairplot(df[['Wind Speed', 'Weibull C', 'Weibull K', 'Avg_Wind_Speed']])
plt.show()

# Using relplot to draw a scatter plot between two variables, say 'Wind Speed' and 'Avg_Wind_Speed':
# sns.relplot(x='Wind Speed', y='Avg_Wind_Speed', data=df)
# plt.show()

# sns.boxplot(data=df[['Wind Speed', 'Avg_Wind_Speed', 'Weibull C', 'Weibull K']])
# plt.show()

