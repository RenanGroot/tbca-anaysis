import sqlite3
import subprocess

def create_database():
    """
    Creates the database (if not exists), inside folder `database/`.
    Tables:
            food_list
            food_details
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
        category TEXT,
        brand TEXT );

    CREATE TABLE IF NOT EXISTS food_details (
        id TEXT FOREING KEY,
        component TEXT,
        unit TEXT,
        unit_per_100g INTEGER,
        standard_deviation INTEGER,
        min INTEGER,
        max INTEGER,
        num_data_used INTEGER,
        reference TEXT,
        data_type TEXT);
    """
    )
    connection.commit()



def upload_csv(
        csv_path:str,
        sql_database:str,
        table:str
        ) -> None:
    """
    This function populates a database with a csv file, using command-like operations in sqlite3.

    Args:
        csv_path (str): Csv file path. Ex: "landing_files/food_table/food_page1.csv"
        sql_database(str): Target SQL database, which the csv data will be uploaded. Ex:"database/foods.db"
        table(str): Target table's name.
  
    """
    
    # Run subprocess for populating the DB with the csv file
    subprocess.run(['sqlite3',
                         str(sql_database),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + csv_path
                                 +f' {table}'],
                        capture_output=True)

    print(f"Successfully populated db with data from : {csv_path}")