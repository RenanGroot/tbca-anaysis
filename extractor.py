#TODO
# THis function is going to extract the data from the site to the sql database
# https://www.tbca.net.br/index.html

import requests
import pandas as pd


def check_next_page(
        html:str
) -> bool:
    """
    Args: 
        html(str): page's html
    
    Returns:
        bool: True(if there is next page link); False(if there isn't next page link)
    """

    if " class='nav-link'>pr&oacute;xima" in html:
        return True
    else:
        return False

def extract_table(
        target_url:str
) -> pd.DataFrame():
    """
    Extract the table contained in the html given the target page's url.

    Args:
        target_url(str): Target page url
    
    Returns:
        pd.DataFrame: Dataframe containing table data
    """

    response = requests.get(target_url)
    response_html = response.text
    print(response_html)
    print(check_next_page(response_html))

    # Taking table
    tables_html = pd.read_html(response_html)
    df = tables_html[0]
    return df


dtframe = extract_table("https://www.tbca.net.br/base-dados/composicao_estatistica.php")
print(dtframe)