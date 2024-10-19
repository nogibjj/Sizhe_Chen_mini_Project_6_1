## SQLite Lab

[![CI](https://github.com/jessc0202/Sizhe_Chen_mini_Project_6_1/actions/workflows/cicd.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_6_1/actions/workflows/cicd.yml)

# Project Overview

This project involves extracting, transforming, loading (ETL), and querying data related to candy rankings. The dataset comes from [FiveThirtyEight's candy data](https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking). The project includes several Python scripts to automate these processes using Databricks and unit tests using `pytest`. 

## Project Structure

Here’s an overview of the project structure:
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── candy-data.csv
├── main.py
├── mylib
│   ├── __init__.py
│   ├── __pycache__
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── requirements.txt
├── setup.sh
└── test_main.py


## Requirements

Before running the project, ensure you have the following dependencies installed:

- Python 3.9+
- `requests` - for fetching data from a URL.
- `pytest` - for unit testing.
- `databricks-sql-connector` - for connecting to Databricks.

## Complex Query

Here’s the complex query used in this project:

```sql
WITH candy_stats AS (
    SELECT 
        hard,  -- Group by the presence or absence of 'hard' feature
        COUNT(competitorname) AS candy_count,
        AVG(sugarpercent) AS avg_sugar,
        AVG(pricepercent) AS avg_price,
        AVG(winpercent) AS avg_win
    FROM default.jessie_candy_data  -- Your candy dataset table
    GROUP BY hard
)

SELECT *
FROM default.jessie_candy_data
JOIN candy_stats
ON default.jessie_candy_data.hard = candy_stats.hard  -- Join on the 'hard' feature
ORDER BY candy_stats.avg_win DESC;  -- Rank by average win percentage

```
## Query Explanation

- **CTE `candy_stats`**: This common table expression groups candies by whether they are "hard" or not, calculating:
    - The **total count** of candies.
    - The **average sugar content**.
    - The **average price**.
    - The **average win percentage**.
  
- **Join**: The `candy_stats` CTE is then joined back to the original `jessie_candy_data` table, enriching the dataset with aggregated statistics for each candy type.

- **Ranking**: Finally, the results are ordered by the **average win percentage** in descending order to reveal whether "hard" or "non-hard" candies have a higher success rate (win percentage).

This structure allows us to gain insights into which candy characteristics (like "hard") may contribute to higher success rates, and how candy types compare based on sugar, price, and performance.

- **sample output**: 

Row(competitorname='Snickers', chocolate=1, fruity=0, hard=0, avg_sugar=0.75, avg_win=0.90)
Row(competitorname='M&Ms', chocolate=1, fruity=0, hard=1, avg_sugar=0.70, avg_win=0.85)
...

## Check Format and Test Errors 
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

## References 
1. [Databricks SQL Documentation](https://docs.databricks.com/sql/index.html)
2. [Databricks SQL Connector for Python](https://docs.databricks.com/dev-tools/python-sql-connector.html)
3. [FiveThirtyEight Datasets](https://data.fivethirtyeight.com/)

