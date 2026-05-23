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
(Add Screenshot Here)

### Ratings Distribution
(Add Screenshot Here)

### Release Year Trends
(Add Screenshot Here)

### Top Countries by Number of Shows
(Add Screenshot Here)

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
