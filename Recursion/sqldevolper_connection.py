import cx_Oracle
import pandas as pd
from cx_Oracle import DatabaseError

try:

    df=pd.read_csv('product.csv')
    df.info()
    print(df.head(5))
    connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
    cur = connection.cursor()
    # cur.execute('create table product_check(name varchar2(50),sku varchar2(100),description varchar2(200))')
    print("table created successfully")
    for i,row in df.iterrows():
        sql = "INSERT INTO product_check(name,sku,description) VALUES(:1,:2,:3)"
        cur.execute(sql, tuple(row))
    connection.commit()
    # cur.execute('select * from product_list')
    # for result in cur:
    #     print(result)
    # cur.close()
except DatabaseError as e:
    print("There is a problem",e)
finally:
    cur.close()
    connection.close()
