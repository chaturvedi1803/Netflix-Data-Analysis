

































Claim offer
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
plt.show() kya isko linkdin updte kru ?

Haan, but raw code dump mat daalna.
Weak point ye hai ki abhi project sirf “plots bana diye” level pe hai. Data analyst recruiters usually dekhte hain:

problem statement

cleaning steps

insights

business interpretation

visualization quality

GitHub structure

Agar sirf code paste karogi toh impact kam hoga.

Better approach:

LinkedIn Post Structure
1. Short intro
“Built a Netflix Data Analysis project using Python, Pandas and Matplotlib to analyze trends in Netflix movies and TV shows.”

2. Mention skills/tools
Use entity refs for tools:

Python

Pandas

Matplotlib

3. What you analyzed
Movies vs TV Shows distribution

Content ratings

Movie duration trends

Release year trends

Top countries producing Netflix content

4. Add 2–3 insights
Without insights, it looks tutorial-based.

Example:

Movies dominate the Netflix catalog compared to TV Shows.

Most Netflix content falls under mature audience ratings.

Content releases increased rapidly after 2015.

5. Add screenshots
This matters more than code on LinkedIn.

Use image carousel style visuals:


https://images.openai.com/static-rsc-4/t8Y92ujuXxjlLXgAWqNEzYHe0xpPYFqB4I4QIF5HC0oJwUf82er6QY8yUDGwhC21nQUvepYrfuLx5C2TuxiiDiRo87ri5v2KQSeT-OQF-9QzhGlt2WOqlTlzQamVZAjXNRkyzYREcTNjSIL8de0bNFSK-JxqcXL6Md_bwp_GrfQWnnQKugwTLL-jUw1zjOYq?purpose=fullsize

https://images.openai.com/static-rsc-4/3hCtWnxrB987vaLwa_gp1F_hLtnbEQOodMLg_XXXtbGAsyvzsxdFKDMVATHY46Mdh-HM224ebmUAxyVenAXN1BNQSCNmUKglpQBpNYvuYmx5Dq194cgzte7XVZTWLJfJYFfeaG5nK7r4118KHqtqvjLJm6dqOtTqDjp5648Gc7q5hm4DnePK-Iy2cCAOoIy5?purpose=fullsize

https://images.openai.com/static-rsc-4/41mGZjSfiycVoFfUmLB_TzUPyJKlvgy_Izi6Q0pHO_-l21NY12qJVUjnEDW3svQ0HvrZGZDsoQmP4pEiipcBqaT0C7bZEBcwfFLdq8iBYvaYnIu9Y9FGuOmAGWYANhrdyFaMUpGk2Za9b_4DEZFqsgDCwR_0psQs248Ob_Y72_Pw9jyfRYc0RvZlM-swMF_-?purpose=fullsize
6
6. Add GitHub link
Put clean repo:

README

dataset source

requirements.txt

screenshots

insights section

One thing to fix in your project
This line can break:

.astype(int)
Because TV Shows have durations like "2 Seasons".

You filtered movies before it, so currently safe — but mention this in interview:

“I separated movie records before converting duration to integer to avoid season-based values from TV Shows.”

That shows actual understanding.

Better LinkedIn caption
Built a Netflix Data Analysis project using Python, Pandas and Matplotlib.

In this project, I cleaned and analyzed the Netflix Titles dataset and created visualizations to identify trends in content type, ratings, release years, movie duration, and country-wise distribution.

Key Insights:
• Movies are more dominant than TV Shows on Netflix
• Content releases increased significantly after 2015
• Mature audience ratings appear most frequently
• Certain countries contribute a major share of Netflix content

Tools Used:
Python | Pandas | Matplotlib

#Python #DataAnalytics #Pandas #DataVisualization #MachineLearning #Netflix
One more thing:
This is decent for a beginner portfolio project, but not enough alone for data analyst shortlisting. The missing part is:

SQL project

Excel dashboard

business KPI analysis

one end-to-end dashboard project (Power BI/Tableau)

Right now this project shows:

“I can clean data and plot graphs.”

Not yet:

“I can solve business problems with data.”


toh kya thik kar sakte hain iss project me /

Kaafi kuch. Abhi project descriptive analytics tak limited hai. Tum graphs dikha rahi ho, but “analysis” kam hai. Recruiter ka next question hota hai:

“So what?”

Uska answer project me visible hona chahiye.

Sabse important improvements
1. Insights section add karo
Abhi sirf charts hain.

Har graph ke niche conclusion likho.

Example:

“Movies contribute nearly X% of Netflix catalog.”

“Content production sharply increased after 2015.”

“TV-MA is the most common rating category.”

“United States dominates Netflix content library.”

Ye analytical thinking show karta hai.

2. Dataset cleaning aur strong karo
Abhi weak cleaning hai.

Tumne:

df.dropna(subset=['type', 'rating', 'duration'])
Kiya hai.

Problem:

unnecessary rows delete ho sakte hain

valuable data lose hota hai

Better:

df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')
Recruiters dekhte hain:

“Did candidate preserve data intelligently?”

3. Country analysis currently inaccurate hai
Weak point:
country column me multiple countries hoti hain.

Example:

United States, India
Tum value_counts() directly kar rahi ho → wrong counts.

Better approach:

country_series = df['country'].str.split(', ')
country_series = country_series.explode()

country_counts = country_series.value_counts().head(10)
This is actual analyst-level cleaning.

4. Add Genre Analysis (Important)
Missing major feature.

Use:

listed_in
column.

Questions:

Most common genres?

Drama vs Comedy vs Documentary?

Movies vs genres?

Visualization:

horizontal bar chart

This makes project richer.

5. Add yearly trend by type properly
Current version:

subplots(1,2)
works, but comparison weak hai.

Better:
single graph with two lines.

plt.plot(...Movies...)
plt.plot(...TV Shows...)
plt.legend()
Then trend compare clearly visible hoga.

6. Add business questions
THIS is the biggest upgrade.

Instead of:

“I made charts.”

Frame as:

“I answered business questions.”

Example questions:

Which type of content dominates Netflix?

Which countries produce maximum content?

How has Netflix content evolved over time?

Which audience rating is most common?

What is the average movie duration?

Now it sounds like analysis.

7. Add KPI metrics
Before charts print:

print("Total Content:", len(df))
print("Total Movies:", ...)
print("Total TV Shows:", ...)
print("Average Movie Duration:", ...)
Very common in dashboards.

8. Convert into dashboard later
Current project = notebook analysis.

Next level:

Power BI dashboard
OR

Streamlit app

That becomes portfolio-worthy.

9. Folder structure improve karo
Current beginners usually keep random files.

Do this:

Netflix-Data-Analysis/
│
├── data/
├── notebook/
├── images/
├── README.md
├── requirements.txt
└── netflix_analysis.py
Looks professional instantly.

10. Add README properly
Most students skip this.

README should include:

Objective

Dataset

Tools

Questions solved

Insights

Screenshots

GitHub project quality doubles.

Biggest missing thing
Abhi tum Matplotlib use kar rahi ho.

Good for learning.

But recruiters often expect:

Seaborn

Power BI

SQL

So this project should become:

Python EDA

SQL analysis

Power BI dashboard

Then it starts looking employable.


redeme # Netflix Movies & TV Shows Data Analysis

## About This Project

This project is based on the analysis of Netflix Movies and TV Shows data using Python.  
The main purpose of this project was to practice real-world data analysis by cleaning datasets, finding useful insights, and creating visualizations.

Using Pandas and Matplotlib, different trends and patterns were explored from the Netflix dataset such as:
- Movies vs TV Shows distribution
- Release year trends
- Ratings analysis
- Country-wise content production
- Genre popularity

This project helped improve my understanding of data cleaning, data visualization, and working with real datasets using Python.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

---

## Dataset Used

Dataset: Netflix Titles Dataset (Kaggle)

The dataset includes:
- Movie & TV Show titles
- Release years
- Ratings
- Duration
- Countries
- Genres
- Directors and cast information

---

## What I Did in This Project

### Data Cleaning
- Checked missing values
- Removed unnecessary data
- Organized important columns
- Prepared the dataset for analysis

### Data Analysis
Analyzed:
- Number of Movies and TV Shows
- Netflix release trends over the years
- Most common ratings
- Top countries producing Netflix content
- Popular genres/categories

### Data Visualization
Created different charts such as:
- Bar Charts
- Pie Charts
- Line Graphs
- Horizontal Bar Charts

These graphs helped in understanding patterns and trends more clearly.

---

## Key Insights from the Dataset

### Movies vs TV Shows
Movies are available in much higher numbers compared to TV Shows on Netflix.

### Release Trends
Netflix content releases increased rapidly after 2015, showing major growth in content production.

### Ratings Analysis
TV-MA and TV-14 are among the most common ratings, indicating that much of the content is targeted toward mature audiences.

### Country-wise Analysis
The United States contributes the highest amount of Netflix content compared to other countries.

### Genre Analysis
Drama and International categories appear frequently, showing Netflix’s focus on globally popular entertainment.

---

## Why Different Charts Were Used

| Chart Type | Purpose |
|---|---|
| Bar Chart | Compare categories easily |
| Pie Chart | Show percentage distribution |
| Horizontal Bar Chart | Improve readability for long labels |

---

## Project Structure

bash
Netflix-Data-Analysis/
│
├── netflix_analysis.py
├── netflix_titles.csv
├── README.md
  └── screenshots/


---

## How to Run This Project

### 1. Clone the Repository

bash
git clone https://github.com/your-username/Netflix-Data-Analysis.git


### 2. Install Required Libraries

bash
pip install pandas matplotlib


### 3. Run the Python File

bash
python netflix_analysis.py


---

## Screenshots
<img width="1200" height="633" alt="Python 3 11 22-05-2026 00_15_43" src="https://github.com/user-attachments/assets/aae27d3f-1450-4e62-9e15-95fe17486a3b" />

<img width="800" height="607" alt="Python 3 11 22-05-2026 00_15_52" src="https://github.com/user-attachments/assets/a80d70b3-fa1c-4ad1-b785-9cf75e6049de" />

<img width="800" height="642" alt="Python 3 11 22-05-2026 00_16_02" src="https://github.com/user-attachments/assets/cb224533-bc41-4678-814d-beacf04e5dc4" />

<img width="1200" height="542" alt="Python 3 11 22-05-2026 00_16_14" src="https://github.com/user-attachments/assets/a4e5907b-f9de-4794-b040-dc0d95a0445a" />





## Skills Learned

Through this project, I practiced:
- Data Cleaning
- Data Analysis
- Data Visualization
- Working with CSV datasets
- Python programming
- Pandas operations
- Graph selection for different data types

---

## Future Improvements

In the future, this project can be improved by:
- Adding interactive dashboards
- Using Plotly or Seaborn
- Creating a recommendation system
- Building a Streamlit web app

---

## Author

Sakshi  
BTech CSE Student  
Interested in Python, Data Analysis, and Machine Learning.

---

## Final Note

This project was created to strengthen practical Python and data analysis skills using a real-world dataset.  
It demonstrates how raw data can be converted into meaningful insights through analysis and visualization. kya kmi hai /

README beginner level ke liye decent hai, but recruiter/GitHub reviewer angle se kuch weak points hain. Major problems content me nahi — positioning aur professionalism me hain.

Sabse pehli kami
1. Bahut generic wording hai
Ye lines:

“This project helped improve my understanding…”

“This project was created to strengthen…”

Bahut template-like lagti hain. Almost हर beginner README me hoti hain.

Replace with concrete things:

rows analyzed

columns used

transformations applied

business questions answered

2. Objective weak hai
Current:

“practice real-world data analysis”

Weak because every beginner writes this.

Better:

Objective:
Analyze Netflix content trends to understand content distribution, audience targeting, release growth, and country-wise production patterns.
More analyst-like.

3. “What I Did” section still sounds task-based
You wrote:

Checked missing values

Removed unnecessary data

But not:

why?

what impact?

what method?

Better:

### Data Cleaning
- Handled missing values in rating, duration, and country columns
- Standardized country information for analysis
- Converted movie duration from string format to numerical values
- Filtered movie-specific records for duration analysis
This sounds technically stronger.

4. Missing numerical insights
This is a major weakness.

Current insights are qualitative only.

Add numbers.

Example:

- Movies make up nearly 70% of total Netflix content.
- Content releases increased sharply after 2015.
- TV-MA was the most common content rating.
- The United States contributed the highest number of titles.
Even approximate percentages improve credibility.

5. Project structure formatting broken hai
This part:

├── README.md
  └── screenshots/
Indentation wrong hai.

Should be:

Netflix-Data-Analysis/
│
├── netflix_analysis.py
├── netflix_titles.csv
├── README.md
└── screenshots/
Small thing, but professionalism matters.

6. “Pie Charts” mention misleading hai
Tumhare code me pie chart nahi hai.

README me false claim avoid karo.

Either:

actually add pie chart
OR

remove mention.

Recruiters notice mismatch.

7. Missing GitHub polish items
Add these:

Badges
Optional but good:

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
requirements.txt
Currently mentioned indirectly only.

Create actual file:

pandas
matplotlib
8. Screenshots section weakly presented
Currently raw image dump hai.

Better:

### Movies vs TV Shows Distribution
(image)

### Release Year Trends
(image)
Structured sections improve readability.

9. Missing business interpretation
This is the biggest gap between:

“student project”
vs

“analyst project”

Example:

Business Insight:
The increase in Netflix releases after 2015 reflects aggressive platform expansion and investment in original content.
Now it sounds analytical.

10. Future improvements section can be stronger
Current:

recommendation system

Streamlit app

Good, but disconnected from current work.

Better progression:

Future Improvements
- Build interactive Power BI dashboard
- Perform SQL-based analysis
- Add genre recommendation features
- Deploy analysis using Streamlit
More realistic roadmap.

Biggest issue overall
Your project currently proves:

“I know Python basics and can create charts.”

It does NOT yet strongly prove:

“I can independently analyze messy business data.”

To reach that level:

more cleaning logic

better insights

SQL

dashboard

KPIs

business questions

maybe correlation analysis

Then the same project becomes much stronger.

Still, for a first public GitHub data project, this is publishable. Just don’t present it as advanced analytics.


thik krke redme de do updated

# Netflix Movies & TV Shows Data Analysis

## Project Overview

This project focuses on analyzing Netflix Movies and TV Shows data using Python.  
The objective of this analysis was to explore content trends on Netflix and extract meaningful insights using data cleaning, analysis, and visualization techniques.

The project was performed using the Netflix Titles Dataset from Kaggle and includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Trend analysis
- Content distribution analysis
- Data visualization using charts and graphs

---

## Objective

The main objective of this project was to analyze Netflix content trends and answer questions such as:

- Are Movies more common than TV Shows?
- How has Netflix content grown over the years?
- Which ratings appear most frequently?
- Which countries contribute the most content?
- Which genres are most popular on Netflix?

---

## Technologies Used

- Python
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- VS Code

---

## Dataset Information

Dataset Used: Netflix Titles Dataset (Kaggle)

The dataset contains information about:
- Movies and TV Shows
- Release years
- Ratings
- Duration
- Country
- Genres/Categories
- Directors and Cast

---

## Data Cleaning & Preprocessing

The following preprocessing steps were performed before analysis:

- Checked missing/null values
- Handled missing values in important columns
- Filled missing country values with "Unknown"
- Filtered movie records separately for duration analysis
- Converted movie duration from string format to numerical values
- Organized dataset for visualization and trend analysis

---

## Exploratory Data Analysis (EDA)

The project includes analysis of:

### 1. Movies vs TV Shows Distribution
Compared the total number of Movies and TV Shows available on Netflix.

### 2. Ratings Distribution
Analyzed the most common audience ratings such as TV-MA, TV-14, PG, etc.

### 3. Movie Duration Analysis
Studied the distribution of movie durations using histograms.

### 4. Release Year Trends
Analyzed how Netflix content production changed over time.

### 5. Country-wise Content Analysis
Identified the top countries contributing Netflix content.

### 6. Genre Analysis
Explored the most common genres/categories available on Netflix.

---

## Data Visualizations

Different types of charts were used to represent insights clearly:

| Visualization | Purpose |
|---|---|
| Bar Chart | Compare categories |
| Line Graph | Analyze trends over time |
| Histogram | Study distribution of movie durations |
| Horizontal Bar Chart | Improve readability of country data |

---

## Key Insights

- Movies are available in significantly higher numbers compared to TV Shows on Netflix.
- Netflix content production increased rapidly after 2015.
- TV-MA and TV-14 are among the most common ratings, indicating strong mature audience targeting.
- The United States contributes the highest number of Netflix titles.
- Drama and International categories appear frequently across the platform.

---

## Business Insights

- The rapid growth in releases after 2015 reflects Netflix’s expansion strategy and increasing investment in content production.
- Mature audience ratings dominating the platform suggest Netflix focuses heavily on adult and young adult viewers.
- High contribution from countries like the United States highlights regional dominance in content creation.

---

## Project Structure

```text
Netflix-Data-Analysis/
│
├── netflix_analysis.py
├── netflix_titles.csv
├── requirements.txt
├── README.md
└── screenshots/
How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/Netflix-Data-Analysis.git
2. Install Required Libraries
pip install pandas matplotlib
3. Run the Python File
python netflix_analysis.py
Screenshots
Movies vs TV Shows Distribution
(Add Screenshot Here)

Ratings Distribution
(Add Screenshot Here)

Release Year Trends
(Add Screenshot Here)

Top Countries by Number of Shows
(Add Screenshot Here)

Skills Practiced
This project helped strengthen practical skills in:

Data Cleaning

Exploratory Data Analysis

Data Visualization

Python Programming

Working with CSV datasets

Pandas operations

Graph selection and interpretation

Future Improvements
This project can be extended further by:

Building an interactive dashboard using Power BI

Performing SQL-based analysis

Using Seaborn or Plotly for advanced visualizations

Creating a Streamlit web application

Adding a content recommendation system

Author
Sakshi
BTech CSE Student
Interested in Python, Data Analysis, and Machine Learning

Final Conclusion
This project demonstrates how raw entertainment data can be transformed into meaningful insights using Python-based data analysis techniques.

Through this analysis, important trends related to Netflix content distribution, audience targeting, release growth, and country-wise production were identified using data cleaning and visualization methods.


copy paste kar saku direct aisa do

# Netflix Movies & TV Shows Data Analysis

## Project Overview

This project focuses on analyzing Netflix Movies and TV Shows data using Python.  
The objective of this analysis was to explore content trends on Netflix and extract meaningful insights using data cleaning, analysis, and visualization techniques.

The project was performed using the Netflix Titles Dataset from Kaggle and includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Trend analysis
- Content distribution analysis
- Data visualization using charts and graphs

---

## Objective

The main objective of this project was to analyze Netflix content trends and answer questions such as:

- Are Movies more common than TV Shows?
- How has Netflix content grown over the years?
- Which ratings appear most frequently?
- Which countries contribute the most content?
- Which genres are most popular on Netflix?

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

---

## Dataset Information

Dataset Used: Netflix Titles Dataset (Kaggle)

The dataset contains information about:
- Movies and TV Shows
- Release years
- Ratings
- Duration
- Country
- Genres/Categories
- Directors and Cast

---

## Data Cleaning & Preprocessing

The following preprocessing steps were performed before analysis:

- Checked missing/null values
- Handled missing values in important columns
- Filled missing country values with "Unknown"
- Filtered movie records separately for duration analysis
- Converted movie duration from string format to numerical values
- Organized dataset for visualization and trend analysis

---

## Exploratory Data Analysis (EDA)

The project includes analysis of:

### 1. Movies vs TV Shows Distribution
Compared the total number of Movies and TV Shows available on Netflix.
<img width="600" height="442" alt="Python 3 11 23-05-2026 21_59_35" src="https://github.com/user-attachments/assets/9f140d15-1824-40d5-82b7-fd293ef85884" />


### 2. Ratings Distribution
Analyzed the most common audience ratings such as TV-MA, TV-14, PG, etc.
<img width="1200" height="633" alt="Python 3 11 22-05-2026 00_15_43" src="https://github.com/user-attachments/assets/5250b099-55e2-4fbd-80b1-08a965870c70" />


### 3. Movie Duration Analysis
Studied the distribution of movie durations using histograms.
<img width="800" height="607" alt="Python 3 11 22-05-2026 00_15_52" src="https://github.com/user-attachments/assets/2bb900d6-ba9b-4534-96aa-11b259817350" />


### 4. Release Year Trends
Analyzed how Netflix content production changed over time.
<img width="1000" height="642" alt="Python 3 11 23-05-2026 22_00_17" src="https://github.com/user-attachments/assets/20ec8cbe-61bb-4bd3-a9ab-c146c0986a50" />


### 5. Country-wise Content Analysis
Identified the top countries contributing Netflix content.
<img width="800" height="642" alt="Python 3 11 22-05-2026 00_16_02" src="https://github.com/user-attachments/assets/80d1ecf2-28b8-44da-bb95-a2bdd30e053d" />


### 6. Genre Analysis
Explored the most common genres/categories available on Netflix.
<img width="1200" height="542" alt="Python 3 11 23-05-2026 22_00_27" src="https://github.com/user-attachments/assets/fa72f3b9-3f0b-4c54-b40b-da6db7d9861d" />

---

## Data Visualizations

Different types of charts were used to represent insights clearly:

| Visualization | Purpose |
|---|---|
| Bar Chart | Compare categories |
| Line Graph | Analyze trends over time |
| Histogram | Study distribution of movie durations |
| Horizontal Bar Chart | Improve readability of country data |

---

## Key Insights

- Movies are available in significantly higher numbers compared to TV Shows on Netflix.
- Netflix content production increased rapidly after 2015.
- TV-MA and TV-14 are among the most common ratings, indicating strong mature audience targeting.
- The United States contributes the highest number of Netflix titles.
- Drama and International categories appear frequently across the platform.

---

## Business Insights

- The rapid growth in releases after 2015 reflects Netflix’s expansion strategy and increasing investment in content production.
- Mature audience ratings dominating the platform suggest Netflix focuses heavily on adult and young adult viewers.
- High contribution from countries like the United States highlights regional dominance in content creation.

---

## Project Structure

```text
Netflix-Data-Analysis/
│
├── netflix_analysis.py
├── netflix_titles.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Netflix-Data-Analysis.git
```

### 2. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 3. Run the Python File

```bash
python netflix_analysis.py
```

---

## Screenshots

### Movies vs TV Shows Distribution
<img width="600" height="442" alt="Python 3 11 23-05-2026 21_59_35" src="https://github.com/user-attachments/assets/5c79f44f-0996-41dc-b1b2-2de1bdf04c1e" />


### Ratings Distribution
<img width="1200" height="633" alt="Python 3 11 22-05-2026 00_15_43" src="https://github.com/user-attachments/assets/38c2740d-8575-4cc1-a138-2096c4248352" />


### Release Year Trends
<img width="1000" height="642" alt="Python 3 11 23-05-2026 22_00_17" src="https://github.com/user-attachments/assets/fba4a646-42fe-439f-8269-076443c95df2" />


### Top Countries by Number of Shows
<img width="800" height="642" alt="Python 3 11 22-05-2026 00_16_02" src="https://github.com/user-attachments/assets/1b8fba43-669c-47f2-a2c8-6ea7caffdf4d" />


---

## Skills Practiced

This project helped strengthen practical skills in:

- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Python Programming
- Working with CSV datasets
- Pandas operations
- Graph selection and interpretation

---

## Future Improvements

This project can be extended further by:

- Building an interactive dashboard using Power BI
- Performing SQL-based analysis
- Using Seaborn or Plotly for advanced visualizations
- Creating a Streamlit web application
- Adding a content recommendation system

---

## Author

Sakshi  
BTech CSE Student  
Interested in Python, Data Analysis, and Machine Learning

---

## Final Conclusion

This project demonstrates how raw entertainment data can be transformed into meaningful insights using Python-based data analysis techniques.

Through this analysis, important trends related to Netflix content distribution, audience targeting, release growth, and country-wise production were identified using data cleaning and visualization methods.

