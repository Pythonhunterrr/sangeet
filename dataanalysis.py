import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('data/dataset.csv')

# 1. Statistics of the data
print(df.describe())

# 2. Graphs

# Pie chart of track genres
plt.figure(figsize=(10, 10))
df['track_genre'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Distribution of Track Genres')
plt.axis('equal')
plt.show()

# Scatter plot of popularity vs. danceability
plt.figure(figsize=(10, 6))
sns.scatterplot(x='danceability', y='popularity', data=df)
plt.title('Popularity vs. Danceability')
plt.show()

# Box plot of energy by genre
plt.figure(figsize=(12, 6))
sns.boxplot(x='track_genre', y='energy', data=df)
plt.title('Energy Distribution by Genre')
plt.xticks(rotation=90)
plt.show()

# Histogram of track durations
plt.figure(figsize=(10, 6))
df['duration_min'] = df['duration_ms'] / 60000  # Convert to minutes
sns.histplot(df['duration_min'], bins=30, kde=True)
plt.title('Distribution of Track Durations')
plt.xlabel('Duration (minutes)')
plt.show()

