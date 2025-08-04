#working withpandas
import numpy as np
import pandas as pd


# series = pd.Series([1,1,2,2,2,3],index=["a","b","c","d","e","f"])
# print(series)
#
# print(series["f"])
#
# data = pd.DataFrame([1,2,3,4,5])
# print(data)

data = pd.DataFrame({'NAME':["Anupam","Singh","Shashi","Yadav"],
                     'AGE':[12,13,14,11]},['A1','A2','A3','A4'])
print(data.head())
print(data['NAME'])
print(data.columns(v))