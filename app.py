from config import DB_DETAILS
import util
import read

def main():
    # ans = DB_DETAILS['dev']
    # tables = get_tables('Tables_to_be_loaded.csv')
    table_name = "departments"
    db_details = util.load_db_details('dev')
    data, columns = read.read_table(db_details,table_name)
    print('reading data for table')


if __name__ == '__main__':
    main()
