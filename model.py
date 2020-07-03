import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xgboost as xgb
import pickle
import joblib


dataset2 = pd.read_csv('estates_price.csv', encoding = "utf-8")
#dataset2 = pd.read_csv('estates.csv', encoding = "ISO-8859-1")
#dataset2['area'] = dataset2['area'].str.replace(',', '.').astype(float)

dataset2['area'] = dataset2['area'].astype(float)
dataset2['price'] = dataset2['price'].astype(float)

dataset2['price_m'] = 0
k = []
l = list(dataset2['city'].unique())
for c in l:
    for i in range(2):            
        df = dataset2.loc[(dataset2['city'] == c) & (dataset2['category'] == i)]
        s = df['price']/df['area']
        s = s.mean(axis = 0)
        k.append(c)
        k.append(s)
        df['price_m'] = s

        dataset2.loc[(dataset2['city'] == c) & (dataset2['category'] == i)] = df
        
    

    #s = dataset[dataset['region'] != "Nabeul"]
dataset2 = dataset2[ dataset2['price'] < 2000000 ]

dataset2 = dataset2[ dataset2['area'] > 50 ]

#s1 = dataset2.municipality.unique()


X1 = dataset2.iloc[:, 2:6].values
X2 = dataset2.iloc[:, -1:].values

X = np.concatenate((X1, X2), axis=1)

y = dataset2.iloc[:, -2].values


#data_dmatrix = xgb.DMatrix(data=X,label=y)



#missing data


#Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#X[:, 1] = labelencoder_X.fit_transform(X[:, 1])

#labelEncoder = preprocessing.LabelEncoder() 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, :])
X[:, :] = imputer.transform(X[:, :])


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 250)

#X_test[:,147:] = sc_X.fit_transform(X_test[:,147:])
# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor


regressor = RandomForestRegressor(n_estimators = 400, criterion = "mse", random_state = 0)
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)

#Model accuracy 
from sklearn.metrics import mean_absolute_error ,r2_score
print('median absolute error: %.2f' % mean_absolute_error(y_test, y_pred))

print('median absolute error: %.2f' % r2_score(y_test, y_pred))

pickle.dump(regressor, open('model.pkl','wb'))
