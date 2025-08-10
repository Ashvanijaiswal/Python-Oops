
import pandas as pd
import numpy as np
from IPython.lib.deepreload import original_reload


def gredient_descent(x,y,lr=0.1,epochs=3000):

    m=0.0
    b=0.0
    min_cost=1000000
    final_b=-1
    final_m=-1
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    x_scaled = (x - x_min) / (x_max - x_min)
    y_scaled = (y - y_min) / (y_max - y_min)
    for epoch in range(0,epochs):
        y_pred=m*x_scaled+b
        error=y_scaled-y_pred
        cost=np.mean(error**2)
        if (min_cost > cost):
            min_cost=cost
            final_b=b
            final_m=m
        dm=-2*np.mean(error*x_scaled)
        db=-2*np.mean(error)
        b=b-db*lr
        m=m-dm*lr

    b_original = b * (y_max - y_min) + y_min - m * (y_max - y_min) * x_min / (x_max - x_min)
    m_original = m * (y_max - y_min) / (x_max - x_min)
    return b_original,m_original




if __name__=='__main__':
    df=pd.read_csv('data/home_prices.csv')
    x=df['area_sqr_ft'].to_numpy()
    y=df['price_lakhs'].to_numpy()
    b,m=gredient_descent(x,y)
    print(f"m={m},b={b}")