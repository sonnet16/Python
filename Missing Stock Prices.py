import pandas as pd
import numpy as np
n = int(input())
data = []
for _ in range(n):
    data.append(input().split())

data = pd.DataFrame(data)
data.columns = ['date', 'time', 'price']
data.price = pd.to_numeric(data.price, errors='coerce')
del data['date']
del data['time']

missingidxlist = data.loc[pd.isna(data["price"]), :].index
data.interpolate(method='polynomial',order=2,inplace=True)

for i in missingidxlist:
    print(-1e32)
    #print(data.at[i, 'price'])
