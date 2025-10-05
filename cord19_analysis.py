# ==========================================================
# CORD-19 METADATA ANALYSIS PROJECT
# Author: [Samuel Munene]

# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# ---------------------------------------------------------
# PART 1: Data Loading and Basic Exploration
# ---------------------------------------------------------

try:
    # Load the dataset
    df = pd.read_csv("metadata.csv", low_memory=False)
    print("✅ Dataset loaded successfully!")

    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Display structure and info
    print("\nDataset Information:")
    print(df.info())

    # Dimensions
    print(f"\nDataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")

    # Check missing values
    print("\nMissing Values Summary:")
    print(df.isnull().sum().sort_values(ascending=False).head(15))

    # Basic statistics for numerical columns
    print("\nBasic Statistics for Numerical Columns:")
    print(df.describe())

except FileNotFoundError:
    print("❌ Error: metadata.csv file not found. Please ensure it’s in the same directory.")
except Exception as e:
    print("❌ Error loading data:", e)

# ---------------------------------------------------------
# PART 2: Data Cleaning and Preparation
# ---------------------------------------------------------

# Handle missing values — example: drop rows missing key columns
important_columns = ['title', 'publish_time', 'journal']
df = df.dropna(subset=important_columns)
print("\nAfter cleaning, dataset shape:", df.shape)

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Create new column: abstract word count (if available)
if 'abstract' in df.columns:
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

print("\nData preparation complete. Columns now include:")
print(df.columns.tolist())

# ---------------------------------------------------------
# PART 3: Data Analysis and Visualization
# ---------------------------------------------------------

# 1️⃣ Count papers by publication year
year_counts = df['year'].value_counts().sort_index()

# 2️⃣ Top journals
top_journals = df['journal'].value_counts().head(10)

# 3️⃣ Most frequent words in titles
from collections import Counter
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

all_titles = " ".join(df['title'].dropna().apply(clean_text))
word_freq = Counter(all_titles.split())
common_words = word_freq.most_common(20)

# ------------------ Visualizations ------------------

sns.set(style="whitegrid")

# A. Publications Over Time
plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values, color='teal')
plt.title("Number of Publications Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.show()

# B. Top Journals
plt.figure(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.show()

# C. Word Cloud of Paper Titles
plt.figure(figsize=(10, 6))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Paper Titles")
plt.show()

# D. Distribution by Source (if available)
if 'source_x' in df.columns:
    plt.figure(figsize=(10, 5))
    df['source_x'].value_counts().head(10).plot(kind='bar', color='orange')
    plt.title("Top Sources by Paper Count")
    plt.xlabel("Source")
    plt.ylabel("Number of Papers")
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------
# PART 4: Streamlit Application
# ---------------------------------------------------------

def run_streamlit_app():
    st.title("CORD-19 Data Explorer")
    st.write("Explore COVID-19 research paper metadata interactively")

    # Year range slider
    min_year, max_year = int(df['year'].min()), int(df['year'].max())
    year_range = st.slider("Select publication year range:", min_year, max_year, (2020, 2021))

    # Filter by year
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    st.subheader("📊 Publications Over Time")
    year_counts = filtered_df['year'].value_counts().sort_index()
    st.bar_chart(year_counts)

    st.subheader("🏢 Top Journals")
    top_journals = filtered_df['journal'].value_counts().head(10)
    st.bar_chart(top_journals)

    st.subheader("☁️ Word Cloud of Titles")
    all_titles = " ".join(filtered_df['title'].dropna().apply(clean_text))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

    st.subheader("📄 Sample Data")
    st.dataframe(filtered_df.head())

# Uncomment the line below to run Streamlit locally
# run_streamlit_app()

# ---------------------------------------------------------
# PART 5: Documentation and Reflection
# ---------------------------------------------------------

"""
Findings:
1. Most publications were concentrated around 2020 and 2021.
2. Certain journals published a majority of COVID-19-related papers.
3. Frequent words in titles include 'covid', 'coronavirus', and 'pandemic'.
4. Data cleaning was crucial since many rows had missing abstracts or dates.

Reflection:
- Handling large datasets required care with memory and missing values.
- Visualizing trends helped understand research focus over time.
- Streamlit simplified building an interactive data exploration app.
"""

# End of Script
