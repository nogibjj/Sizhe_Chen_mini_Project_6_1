"""
Transforms and Loads data into the local databricks database

"""
import csv
import os
from dotenv import load_dotenv
from databricks import sql


def load(dataset="data/candy-data.csv"):
    """"Transforms and Loads data into the local Databricks database"""
    
    # Load the dataset
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)  
    
    # Load environment variables for connection details
    load_dotenv()
    
    # Establish connection to the database
    with sql.connect(server_hostname=os.getenv("SERVER_HOSTNAME"),
                     http_path=os.getenv("HTTP_PATH"),
                     access_token=os.getenv("DATABRICKS_KEY")) as connection:
        
        with connection.cursor() as cursor:
            # Create the table if it does not already exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS jessie_candy_data (
                competitorname STRING,
                chocolate INT,
                fruity INT,
                caramel INT,
                peanutyalmondy INT,
                nougat INT,
                crispedricewafer INT,
                hard INT,
                bar INT,
                pluribus INT,
                sugarpercent FLOAT,
                pricepercent FLOAT,
                winpercent FLOAT
            );
            """)

            cursor.execute("SELECT * FROM jessie_candy_data")
            result = cursor.fetchall()
            if not result:
                print("here")
                insert_query = """
                INSERT INTO jessie_candy_data (
                    competitorname, chocolate, fruity, caramel, peanutyalmondy, nougat,
                    crispedricewafer, hard, bar, pluribus, sugarpercent, pricepercent, winpercent
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
            
                for row in payload:
                    cursor.execute(insert_query, row)

                connection.commit()
    return "db loaded or already loaded"


if __name__ == "__main__":
    load()