import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('oracle://system:oracle@localhost:1521/xe')

df=pd.read_csv('product.csv',delimiter=',')
df.to_sql('product_check', con = engine, if_exists = 'append', chunksize = 100000,index=False)


s='1 2 3 4'
print(tuple(s))
