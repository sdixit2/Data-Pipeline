from util import get_connection

def build_insert_query(table_name, column_name):
    column_values = list(map(lambda column: column.replace(column, '%s')))
    query = (f''' INSERT INTO {table_name} {column_name} VALUES ({column_values})''')
    return query


def insert_data(connection, cursor, query, data, batch_size = 100):
    