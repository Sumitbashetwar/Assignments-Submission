import pandas as pd
import numpy as np
import random

df = pd.DataFrame(np.random.randn(5, 4), index = ['Row1' , 'Row2' , 'Row3' , 'Row4' , 'Row5'] , columns = ['Column1' , 'Column2' , 'Column3' , 'Column4'])

print(df.head() , '\n\n')
print(df.tail() , '\n\n')
print(df['Column1'] , '\n\n')
print(type(df) , '\n\n')
print(df.loc['Row1'] , '\n\n')
print(df.iloc[2 : 5 , 0 : 2] , '\n\n')
print(df.sum() , '\n\n')
print(df.isnull() ,'\n\n')
print(df.isnull().sum() , '\n\n')
print(df.info() , '\n\n')
print(df.corr() , '\n\n')
print(df.dropna(axis=0) , '\n\n')