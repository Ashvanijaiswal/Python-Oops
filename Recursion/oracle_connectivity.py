import cx_Oracle
import pandas as pd
from cx_Oracle import DatabaseError

try:
    df=pd.read_csv('product.csv')
    df.info()
    connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
    cursor = connection.cursor()
    cursor.execute('create table product_check(name varchar2(50),sku varchar2(100),description varchar2(200))')
    print("table created")
    tpls=[tuple(x) for x in df.to_numpy()]
    cols=','.join(list(df.columns))
    sql = "INSERT INTO product_check(name,sku,description) VALUES(:1,:2,:3)"

    cursor.executemany(sql, tpls)
    print('Ye chla?')
    connection.commit()
    print("Data inserted using execute_many() successfully...")
except DatabaseError as e:
    print("There is a problem",e)
finally:
    cursor.close()
    connection.close()
