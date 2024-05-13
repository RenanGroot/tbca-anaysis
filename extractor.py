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


#dtframe = extract_table("https://www.tbca.net.br/base-dados/composicao_estatistica.php")
#print(dtframe)


if __name__ == "__main__":
    page = requests.get("https://www.tbca.net.br/base-dados/composicao_estatistica.php")
    i = 1
    #TODO
    # Need to fix, it is not stoping the loop
    # Create a new condition which looks for how much data is in the data frame
    while check_next_page(page) == False:
        df = extract_table(f"https://www.tbca.net.br/base-dados/composicao_estatistica.php?pagina={str(i)}")
        df.to_csv(f"landing_files/food_page{str(i)}.csv")
        i += 1
        print(i)