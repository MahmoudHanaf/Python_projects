# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:38:40 2022

@author: Mahmoud
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset =pd.read_csv('data.csv')

print(dataset)
print(dataset.info())

print(dataset.dtypes)
print(dataset.duplicated().sum())

dataset.drop_duplicates(inplace=True)
print(dataset.duplicated().sum())

print(dataset.isnull().sum())

miscol =dataset.Albumin_and_Globulin_Ratio
miscol = miscol.fillna(miscol.mean)
dataset.Albumin_and_Globulin_Ratio =miscol 

print(dataset.isnull().sum())

print(dataset.info())
dataset['Total_Bilirubin']=dataset['Total_Bilirubin'].astype(int)
dataset['Direct_Bilirubin']=dataset['Direct_Bilirubin'].astype(int)
dataset['Total_Protiens']=dataset['Total_Protiens'].astype(int)
dataset['Albumin']=dataset['Albumin'].astype(int)
print(dataset.info())

x =dataset.iloc[:,[0,2,3,4,5,6,7,8]]
y= dataset.iloc[:,[10]]















































print(y)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x_train ,x_test,y_train,y_test =train_test_split(x,y,test_size=.2)

from sklearn.cluster import KMeans

km =KMeans(n_clusters=3)
y_train2=km.fit_predict(x_train)
print(y_train2)

print(x_train)




plt.plot(y_train2 ,color='r')
plt.title('volume vs turnover')
plt.xlabel('volume')
plt.ylabel('turnover')

plt.show()


