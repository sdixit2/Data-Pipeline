import pandas as pd

def get_tables(path):
    Tables_to_be_loaded = pd.read_csv(path , sep = ':')
    return Tables_to_be_loaded.query('to_be_loaded == "yes"')