import pandas as pd

# Load data from the specified folder and file
df = pd.read_csv('wind_speed_annual/wind_speed_annual.csv')



# Calculate daily average wind speed for each block
df['Avg_Wind_Speed'] = df[[f"Hour {i:02} Wind Speed" for i in range(24)]].mean(axis=1)

# Drop hourly columns
columns_to_drop = [f"Hour {i:02} {param}" for i in range(24) for param in ["Wind Speed", "Weibull C", "Weibull K"]]
df = df.drop(columns=columns_to_drop)

# The DataFrame is now simplified with daily average wind speed. From here, you can further proceed with regression models 
# to predict 'Avg_Wind_Speed' using other columns as features.
# print(df.info())

top_blocks = df[['Block', 'Avg_Wind_Speed']].sort_values(by='Avg_Wind_Speed', ascending=False).head(10)
print(top_blocks)


std_dev = df['Avg_Wind_Speed'].std()
print(f"Standard Deviation of Average Wind Speed: {std_dev:.2f}")


df['Rounded_Lat'] = df['Lat'].round(1)
df['Rounded_Lon'] = df['Lon'].round(1)
grouped_areas = df.groupby(['Rounded_Lat', 'Rounded_Lon'])['Avg_Wind_Speed'].mean().sort_values(ascending=False).head(10)
print(grouped_areas)



df['Speed_Difference'] = abs(df['Wind Speed'] - df['Avg_Wind_Speed'])
top_differences = df[['Block', 'Speed_Difference']].sort_values(by='Speed_Difference', ascending=False).head(10)
print(top_differences)


# Calculate the overall average wind speed
overall_avg_speed = df['Wind Speed'].mean()

# Count blocks where wind speed exceeds the overall average
above_avg_blocks_count = df[df['Wind Speed'] > overall_avg_speed].shape[0]

print(f"There are {above_avg_blocks_count} blocks where wind speed exceeds the overall average of {overall_avg_speed:.2f} m/s.")

