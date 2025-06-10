# Fintech-App-Analytics-week2

This repository contains the code and data for a fintech app analytics project focusing on review data for banks CBE, BOA, and DASHEN. The project simulates a real-world data engineering workflow using Oracle Database XE.

## Project Structure
- `src/`: Python scripts for data processing and database insertion.
  - `insert_to_oracle.py`: Inserts cleaned review data into Oracle.
  - `preprocess_reviews.py`: Preprocesses raw review data.
- `data/`: Data files and SQL schemas.
  - `sql/bank_reviews_schema.sql`: SQL schema for banks and reviews tables.
  - `processed/`: Cleaned and sentiment-analyzed data (e.g., `sentiment_results.csv`).
- `task_4_visualization.ipynb`: Jupyter Notebook with visualizations for Task 4.
- `sentiment_rating_visualization.png`: Visualization of sentiment trends and distribution.

## Tasks Completed
- **Task 3: Store Cleaned Data in Oracle**
  - Set up Oracle XE and created `banks` and `reviews` tables.
  - Inserted 1377 cleaned reviews into the database.
  - Committed SQL schema dump to GitHub.
- **Task 4: Insights and Recommendations**
  - Analyzed sentiment trends and distributions for CBE, BOA, and DASHEN.
  - Generated visualizations (sentiment trends, distribution).
  - Provided insights and recommendations in a 4-page report.

## Setup
1. Install Oracle XE and configure the listener (port 1521).
2. Install Python dependencies: `pip install oracledb pandas matplotlib seaborn`.
3. Update `insert_to_oracle.py` with your Oracle password.
4. Run `python src/insert_to_oracle.py` to verify data insertion.

## Usage
- Open `task_4_visualization.ipynb` in Jupyter Notebook to view and regenerate visualizations.
- Review `report.md` (or export from notebook) for insights and recommendations.

