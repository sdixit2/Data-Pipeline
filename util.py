import pandas as pd
from mysql import connector as mc
from config import DB_DETAILS
import psycopg2

def load_db_details(env):
    return DB_DETAILS[env]

def get_mysql_connection(db_host, db_user, db_name, db_pass):
    # try:
    connection = mc.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    # except mc.Error as error:
    #     if error.err
    return connection

def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_pass=db_pass
                                          )
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass
                                       )
    return connection
def get_tables(path):
    Tables_to_be_loaded = pd.read_csv(path , sep = ':')
    return Tables_to_be_loaded.query('to_be_loaded == "yes"')