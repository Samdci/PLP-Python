# DATA ANALYSIS AND VISUALIZATION ASSIGNMENT
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

try:
    # Load the Iris dataset from sklearn
    iris_data = load_iris()
    
    # Convert it to a pandas DataFrame
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nData Information:")
    print(df.info())

    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())

    # Since the Iris dataset has no missing values, 
    # but if there were, we could handle them like this:
    df = df.dropna()  # or df.fillna(method='ffill')
    print("\nAfter cleaning, dataset shape:", df.shape)

except FileNotFoundError:
    print("Error: Dataset file not found. Please check the file path.")
except Exception as e:
    print("An error occurred while loading the dataset:", e)
    
    
# Task 2: Basic Data Analysis

# Compute basic statistics
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())

# Grouping by 'species' and computing mean for each numeric column
grouped_means = df.groupby('species').mean(numeric_only=True)
print("\nAverage Measurements per Species:")
print(grouped_means)

# Example observation
print("\nObservations:")
print("- Iris-virginica generally has the largest petal and sepal measurements.")
print("- Iris-setosa has the smallest measurements, making it easily distinguishable.")

# Task 3: Data Visualization

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Line Chart – show trend (simulate a time-series using sample index)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart: Sepal vs Petal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar Chart – average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, palette="Set2")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3️⃣ Histogram – distribution of sepal length
plt.figure(figsize=(8, 5))
plt.hist(df["sepal length (cm)"], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram: Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot – relationship between sepal and petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Findings / Observations
print("\n--- Findings ---")
print("1. There are no missing values in the dataset.")
print("2. Iris-virginica species has the highest average petal length and width.")
print("3. The scatter plot clearly shows species separation based on petal and sepal measurements.")
print("4. The histogram shows most sepal lengths fall between 5.0 and 6.5 cm.")

# End of Script
