# ETL Pipeline Demo – Sales Data Cleanup & Transformation

## Overview
This project demonstrates a simple yet realistic ETL (Extract, Transform, Load) pipeline using **Python** and **Pandas**. It simulates a scenario where raw retail sales data is cleaned and transformed into a structured format for analysis.

## Features
- **Extract**: Reads raw sales data from CSV
- **Transform**:
  - Drops duplicates and nulls
  - Cleans and standardizes column names
  - Fills missing prices with median values
  - Converts data types
- **Load**: Saves the cleaned data to a new CSV file

## Tech Stack
- Python 3.x
- Pandas

## Project Structure
```
etl-pipeline-demo/
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── etl_pipeline.py
├── README.md
└── requirements.txt
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/etl-pipeline-demo.git
   cd etl-pipeline-demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the ETL script:
   ```bash
   python etl_pipeline.py
   ```

4. The cleaned data will be saved to `data/cleaned_data.csv`