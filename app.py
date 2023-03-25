from config import DB_DETAILS
from util import get_tables

def main():
    ans = DB_DETAILS['dev']
    tables = get_tables('Tables_to_be_loaded.csv')
    for table in tables['table_name']:
        print(table)

if __name__ == '__main__':
    main()
