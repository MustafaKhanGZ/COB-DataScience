import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the CSV file
df = pd.read_csv('haha.csv')

# Explore the dataset
print(df.head())  # Display the first few rows of the dataset
print(df.info())  # Display information about the dataset

# List of columns you want to analyze and create visualizations for
columns_to_analyze = ['show_id', 'type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in']

# Loop through the columns and create visualizations
for column in columns_to_analyze:
    plt.figure(figsize=(12, 6))  # Adjust the figure size

    if df[column].dtype == 'int64' or df[column].dtype == 'float64':
        # Create a histogram for numeric columns
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
    else:
        # Create a bar plot for categorical columns
        if df[column].nunique() > 10:
            top_categories = df[column].value_counts().nlargest(10).index
            df[column] = df[column].where(df[column].isin(top_categories), 'Other')

        sns.countplot(data=df, x=column, palette='viridis', saturation=0.75)
        plt.title(f'Count of {column}')
        plt.xlabel('Categories')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')  # Adjust rotation and horizontal alignment

    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
