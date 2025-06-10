# Fintech-App-Analytics-Week2

This repository contains the code, data, and documentation for a fintech app analytics project analyzing review data for banks CBE, BOA, and DASHEN. The project follows a real-world data engineering and analytics workflow using Oracle Database XE.

## Project Structure
- `src/`: Python scripts for data processing and database operations.
  - `preprocess_reviews.py`: Cleans raw review data (Task 1).
  - `insert_to_oracle.py`: Inserts processed data into Oracle (Task 3).
- `data/`: Data files and SQL schemas.
  - `sql/bank_reviews_schema.sql`: SQL schema for banks and reviews tables (Task 3).
  - `processed/`: Cleaned and sentiment-analyzed data (e.g., `sentiment_results.csv`) (Task 2).
- `analysis.ipynb`: Jupyter Notebook with visualizations for Task 4.
- `sentiment_rating_visualization.png`: Visualization of sentiment trends and distribution (Task 4).
- `report.md`: 4-page report with insights and recommendations (Task 4).

## Tasks Completed

### Task 1: Data Collection and Preprocessing
- Scraped and cleaned review data from fintech apps.
- Removed duplicates and missing values, standardized dates and bank IDs (e.g., `DASHEN` to `DASH`).
- Output: `clean_reviews.csv` saved in `data/processed/`.

### Task 2: Sentiment Analysis and Thematic Processing
- Performed sentiment analysis using TextBlob to generate `sentiment_label` and `sentiment_score`.
- Identified themes in reviews and saved results in `sentiment_results.csv`.

### Task 3: Store Cleaned Data in Oracle
- Set up Oracle XE and created a database with `banks` and `reviews` tables.
- Inserted 1377 cleaned reviews into the database using Python.
- Committed SQL schema dump (`bank_reviews_schema.sql`) to GitHub.

### Task 4: Insights and Recommendations
- Analyzed sentiment trends and distributions for CBE, BOA, and DASHEN.
- Generated visualizations: Average Sentiment Score Trends and Sentiment Score Distribution.
- Identified drivers (e.g., CBE sentiment peak, DASHEN consistency) and pain points (e.g., BOA volatility, CBE baseline).
- Suggested improvements: Stabilize BOA experience, improve CBE usability.
- Drafted a 4-page report noting potential negative bias in reviews.

## Setup
1. Install Oracle XE and configure the listener (port 1521).
2. Install Python dependencies: `pip install oracledb pandas matplotlib seaborn`.
3. Update `insert_to_oracle.py` with your Oracle password (e.g., `senait.01`).
4. Run `python src/insert_to_oracle.py` to verify data insertion.

## Usage
- Run `python src/preprocess_reviews.py` to regenerate `clean_reviews.csv`.
- Open `analysis.ipynb` in Jupyter Notebook to view and regenerate visualizations.
- Review `report.md` for insights and recommendations.

