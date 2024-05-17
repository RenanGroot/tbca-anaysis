import os
import requests
import pandas as pd

def list_files(
        path:str
)-> list:
    """
    Lists the files from a folder.

    Args:
        path(str): Folder's path.

    Returns:
        list: List with the files paths.
    """

    files = []
    directory = os.fsencode(path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        files.append(path + "/" + filename)

    return files


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
        df.to_csv(f"landing_files/food_table/food_page{str(i)}.csv",index=False)
        i += 1

        print("Successfuly extracted food tables")

def source_to_landing_details():
    """
    Extract all foods' details tables, saving it into csv files in the "landing_files/details" folder.
    """
    files = list_files("landing_files/food_table")
    for file in files:
        temp_df = pd.read_csv(file)
        food_list = temp_df["Código"].to_list()
        for food in food_list:
            already_downloaded = list_files("landing_files/details")
            if f"landing_files/details/product_{food}.csv" in already_downloaded:
                pass
            else:
                df_details = extract_table(f"https://www.tbca.net.br/base-dados/int_composicao_estatistica.php?cod_produto={food}")
                df_details.to_csv(f"landing_files/details/product_{food}.csv",index=False)
    
    print("Successfully extracted food details")

if __name__ == "__main__":
    #source_to_landing_foods()
    source_to_landing_details()