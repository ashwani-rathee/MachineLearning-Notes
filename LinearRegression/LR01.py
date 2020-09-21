# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:48:17 2020
@author: TIET
"""
import numpy as np
X=np.array([[-2],[1],[3]])  # Input data
Y=np.array([[-1],[1],[2]])  # output varaible data
print(X)
print(Y)
print(np.size(X))
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)

 #B0
print(model.intercept_) 
#B1
print(model.coef_)  
#v1=model.predict([[-2]])
v1=model.predict([[2]])  # new input 
print(v1)


#no unseen data