
import numpy as np
import pandas as pd
import pickle
import matplotlib as pyplot

data =pd.read_excel('Mobile.xlsx')
data.head()

data=data.drop(['Model','Proceesor','Company'],axis=1)

data.head()
x=data.drop(['Price'],axis=1)
y=data['Price']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state=42)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

from sklearn.metrics import accuracy_score
y_pred=lr.predict(x_test)

pickle.dump(lr, open('model.pkl', 'wb'))
