# -*- coding: utf-8 -*-
"""
@author: TIET
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv('houses_price.csv')
print(data)
X=data[['No of Bed Rooms']]
Y=data[['Price']]
import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.xlabel('No of Bed Rooms')
plt.ylabel('Price')
plt.show()
model = LinearRegression()
#x_train,x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=1)
#print(x_train)
#model.fit(x_train, y_train)
#pred= model.predict(x_test)
#print(model.coef_)
#print(model.intercept_)
#v1=model.predict([[2]])  # new input 
#print(v1)