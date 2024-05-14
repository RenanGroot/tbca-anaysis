#TODO
# THis function is going to extract the data from the site to the sql database
# https://www.tbca.net.br/index.html

import requests
import pandas as pd


def extract_table(
        target_url:str
) -> pd.DataFrame:
    """
    Extract the table contained in the html given the target page's url.

    Args:
        target_url(str): Target page url
    
    Returns:
        pd.DataFrame: Dataframe containing table data
    """

    response = requests.get(target_url)
    response_html = response.text
    # Taking table
    tables_html = pd.read_html(response_html)
    df = tables_html[0]
    return df


def source_to_landing_foods():
    """
    Extract all foods' tables, saving it into csv files in the "landing_files/food_table" folder.
    """
    i = 1
    is_empty = False

    # Loop though all the pages
    while is_empty == False:
        df = extract_table(f"https://www.tbca.net.br/base-dados/composicao_estatistica.php?pagina={str(i)}")

        # Condition if table there is no row, stop the looping
        if df.shape[0] < 1:
            is_empty = True
            continue
        df.to_csv(f"landing_files/food_table/food_page{str(i)}.csv")
        i += 1

        print("Successfuly extracted food tables")

if __name__ == "__main__":
    source_to_landing_foods()