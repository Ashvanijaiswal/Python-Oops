import cx_Oracle
from cx_Oracle import DatabaseError
import pandas as pd

def create_connection(username,password):
    try:
        connection = cx_Oracle.connect(f'{username}/{password}@localhost:1521/xe')
        return connection
    except DatabaseError as e:
        print('There is a problem exists',e)


def create_table(connection,table):
    try:
        cursor = connection.cursor()
        print('Creating table...')
        cursor.execute(f'create table {table}(name varchar2(50),sku varchar2(100),description varchar2(200))')
        print("table created")
        return cursor
    except DatabaseError as e:
        print('Something wrong, Please check')


def load_data(file_name,cursor,connection):
    data=pd.read_csv('product.csv')
    tpls=[tuple(x) for x in data.to_numpy()]
    try:

        sql = "INSERT INTO products(name,sku,description) VALUES(:1,:2,:3)"
        cursor.executemany(sql,tpls)
        print('Data lodaed into table...')

    except DatabaseError as e:
        print('Error',e)

    finally:
        cursor.close()
        connection.close()

if __name__=='__main__':
    connection=create_connection('system','oracle')
    cursor=create_table(connection,'products')
    load_data('product.csv',cursor,connection)
