print("Hello World")
import pandas as pd
df=pd.read_csv("/usr/src/basket_data.csv",sep='delimiter', header=None,engine='python')
df=df[0].str.split(',',expand=True)
rows=df.shape[0]
cols=df.shape[1]
car_set=set()
for i in range(100):
    for j in range(4):
        if df[j][i]:
            car_set.add(df[j][i].strip())
print(len(car_set))