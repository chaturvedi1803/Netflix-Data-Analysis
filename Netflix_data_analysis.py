# =========================================================
# Netflix Data Analysis Project
# Tools Used: Python, Pandas, Matplotlib
# Dataset: Netflix Titles Dataset
# Objective:
# Analyze Netflix movies and TV shows using data visualization
# =========================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# Part 1: Movies vs TV Shows Distribution
# =========================================================

# =========================================================
# Load Dataset
# =========================================================

df = pd.read_csv('netflix_titles.csv')

# Display first 5 rows
print(df.head())


# =========================================================
# Data Cleaning
# =========================================================

# Check missing values
print(df.isnull().sum())

# Remove rows with missing values in important columns
df = df.dropna(subset=['type', 'rating', 'duration'])
df['country'] = df['country'].fillna('Unknown')

# Verify missing values after cleaning
print(df.isnull().sum())

# Count movies and TV shows
type_Counts = df['type'].value_counts()

# Set figure size
plt.figure(figsize=(6,4))

# Create bar chart
plt.bar(type_Counts.index,
        type_Counts.values,
        color=['skyblue','orange'])

# Add labels and title
plt.title('Number of Movies VS TV Shows On Netflix')
plt.xlabel('Type')
plt.ylabel('Count')

# Adjust layout spacing
plt.tight_layout()
plt.show()


# =========================================================
# Part 2: Content Ratings Distribution
# =========================================================

rating_Counts = df['rating'].value_counts().head(8)

plt.figure(figsize=(12,6))

plt.bar(rating_Counts.index,
        rating_Counts.values,
        color='skyblue')

plt.title('Netflix Content Age Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Number of Shows')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# =========================================================
# Part 3: Movie Duration Distribution
# =========================================================

movie_df = df[df['type']=='Movie'].copy()

movie_df['duration_int'] = movie_df['duration'] \
    .str.replace('min','',regex=False) \
    .astype(int)

plt.figure(figsize=(8,6))

plt.hist(movie_df['duration_int'],
         bins=30,
         color='purple',
         edgecolor='black')

plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')

plt.tight_layout()
plt.show()


# =========================================================
# Part 4: Release Year vs Number of Shows
# =========================================================

release_count = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,6))

plt.plot(release_count.index,
         release_count.values,
         color='red',
         marker='o')

plt.title('Release Year Vs Number Of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')

plt.tight_layout()
plt.show()


# =========================================================
# Part 5: Top 10 Countries by Number of Shows
# =========================================================

country_counts = df['country'].value_counts().head(10)

plt.figure(figsize=(8,6))

plt.barh(country_counts.index,
         country_counts.values,
         color='red')

plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')

plt.tight_layout()
plt.show()


# =========================================================
# Part 6: Movies vs TV Shows Released Per Year
# =========================================================

content_by_year = df.groupby(['release_year','type']) \
                    .size() \
                    .unstack() \
                    .fillna(0)

fig, ax = plt.subplots(1,2,figsize=(12,5))

# Movies subplot
ax[0].plot(content_by_year.index,
           content_by_year['Movie'],
           color='blue')

ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel("Number Of Movies")

# TV Shows subplot
ax[1].plot(content_by_year.index,
           content_by_year['TV Show'],
           color='red')

ax[1].set_title("TV Shows Released Per Year")
ax[1].set_xlabel('Year')
ax[1].set_ylabel("Number Of Shows")

fig.suptitle('Comparison of Movies and TV Shows Released Over the Years')

plt.tight_layout()
plt.show()