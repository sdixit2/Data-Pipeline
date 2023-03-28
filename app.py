from config import DB_DETAILS
import util
import read
import write

def main():
    # ans = DB_DETAILS['dev']
    tables = util.get_tables('Tables_to_be_loaded.csv')
    table = tables['table_name'].values
    db_details = util.load_db_details('dev')
    for table_name in table:
        data, columns = read.read_table(db_details,table_name)
        write.load_table(db_details,data,columns,table_name)

if __name__ == '__main__':
    main()
