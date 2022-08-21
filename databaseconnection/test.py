import pandas as pd

df=pd.read_csv('product.csv')
tpls=[tuple(x) for x in df.to_numpy()]
print(len(tpls))
