import numpy as np
import pandas as pd
import pickle

data =pd.read_excel('Laptop.xlsx')
data.head()

data=data.drop(['Model','Battery','Operating system'],axis=1)

data=data.iloc[:,1:]
x=data.iloc[:,:-1]
y=data.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn import preprocessing
#le = preprocessing.LabelEncoder()
#X_train['Hard disk','Processor']=le.fit(['Hard disk','Processor'])

from sklearn.linear_model import LinearRegression
laptop=LinearRegression()
laptop.fit(X_train,y_train)

pickle.dump(laptop, open('model1.pkl', 'wb'))