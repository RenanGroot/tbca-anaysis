import sqlite3
import subprocess

def create_database():
    """
    Creates the database (if not exists), inside folder `database/`.
    """
    connection = sqlite3.connect("database/foods.db")
    
    cursor = connection.cursor()

    # Creating Tables, if not exist
    cursor.executescript(
    """
    CREATE TABLE IF NOT EXISTS food_list (
        id TEXT PRIMARY KEY,
        name TEXT,
        scientific_name TEXT,
        group TEXT,
        brand TEXT );

    CREATE TABLE IF NOT EXISTS food_details (
        id TEXT FOREIGN KEY,
        component TEXT,
        unit TEXT,
        unit_per_100g INTEGER,
        standard_deviation INTEGER,
        min INTEGER,
        max INTEGER,
        num_data_used INTEGER,
        references TEXT,
        data_type TEXT);
    """
    )
    connection.commit()



def upload_csv(csv_path:str) -> None:
    """
    This function creates the database (if not exists), and populate it with a csv file.

    Args:
        csv_path (str): Csv file path. Ex: "landing_files/food_table/food_page1.csv"
  
    """
    
    # Run subprocess for populating the DB with the csv file
    subprocess.run(['sqlite3',
                         str("database/foods.db"),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + csv_path
                                 +' flights'],
                        capture_output=True)

    print(f"Successfully populated db with data from : {csv_path}")