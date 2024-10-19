"""Query the database"""
from dotenv import load_dotenv
from databricks import sql
import os

complex_query = """
WITH candy_stats AS (
    SELECT 
        hard,  -- Group by the presence or absence of 'hard' feature
        COUNT(competitorname) AS candy_count,
        AVG(sugarpercent) AS avg_sugar,
        AVG(pricepercent) AS avg_price,
        AVG(winpercent) AS avg_win
    FROM default.candy_data  
    GROUP BY hard
)

SELECT *
FROM default.candy_data
JOIN candy_stats
ON default.candy_data.hard = candy_stats.hard  
ORDER BY candy_stats.avg_win DESC;  
"""



def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    load_dotenv()
    with sql.connect(server_hostname=os.getenv("SERVER_HOSTNAME"),
                     http_path=os.getenv("HTTP_PATH"),
                     access_token=os.getenv("DATABRICKS_KEY")) as connection:
        
        with connection.cursor() as cursor:
            cursor.execute(complex_query)
            result = cursor.fetchall()
            
            for row in result:
                print(row)
            
            cursor.close()
            connection.close()
            
    return "query successful"


if __name__ == "__main__":
    query()
