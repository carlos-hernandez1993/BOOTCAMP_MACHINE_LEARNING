import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from utils.functions import replace_string

print("ruta inicial",os.getcwd())
os.chdir(os.path.dirname(__file__))

print("ruta cambiada del fichero de ejecucion", os.getcwd())


df1=pd.read_csv("data\\raw\\dft-flights-data-2011-1.csv",encoding="unicode_escape")
df1.drop(["Number of Travellers","Customer"],axis=1,inplace=True)
replace_string(df = df1, col= " Total Cost ex VAT ", string_list=[',', '£'], replacement='')
df1[" Total Cost ex VAT "]=df1[" Total Cost ex VAT "].astype("float")
df1[['day', 'month', 'year']] = df1['Travel Date'].str.split('/',expand=True)
df1['year'] = df1['year'].astype(int)
df1['month'] = df1['month'].astype(int)
df1['day'] = df1['day'].astype(int)
df1.drop("Travel Date", axis=1,inplace=True)

df1=df1.replace("ECONOMY",0)
df1=df1.replace('PREMIUM ECONOMY',1)
df1=df1.replace('BUSINESS',2)
df1=df1.replace('FIRST',3)

from sklearn import preprocessing
le_df1=preprocessing.LabelEncoder()
le_df1.fit(df1["Journey Finish Point"])
df1["Journey Finish Point_le"]=le_df1.transform(df1["Journey Finish Point"])

le2_df1=preprocessing.LabelEncoder()
le2_df1.fit(df1["Journey Start Point"])
df1["Journey Start Point_le"]=le2_df1.transform(df1["Journey Start Point"])

le3_df1=preprocessing.LabelEncoder()
le3_df1.fit(df1["Air Carrier"])
df1["Air Carrier_le"]=le3_df1.transform(df1["Air Carrier"])

df1.drop(["year","Ticket Single or Return","Journey Start Point","Journey Finish Point","Air Carrier"],axis=1,inplace=True)

df2_log=np.log(df1+1)

X2=df2_log.drop(" Total Cost ex VAT ",axis=1)
y2=df2_log[" Total Cost ex VAT "]
from sklearn.model_selection import train_test_split
X2_train, X2_test, y2_train, y2_test =  train_test_split(X2, y2, test_size = 0.20, random_state = 42)

from sklearn import preprocessing
std_scale2 = preprocessing.StandardScaler().fit(X2_train)
X2_train_scal = std_scale2.transform(X2_train)
X2_test_scal = std_scale2.transform(X2_test)

from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(random_state=42,max_depth=50,n_estimators=1000)
forest.fit(X2_train_scal, y2_train)

from sklearn import metrics
from sklearn.metrics import r2_score

print('MAE:', metrics.mean_absolute_error(y2_test, forest.predict(X2_test_scal)))
print('MSE:', metrics.mean_squared_error(y2_test, forest.predict(X2_test_scal)))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y2_test,forest.predict(X2_test_scal))))
print("R2 score:", r2_score(y2_test,forest.predict(X2_test_scal)))

import pickle
with open('model\\Random_Forest', "wb") as archivo_salida:
    pickle.dump(forest, archivo_salida)

prueba_prediccion=pd.DataFrame({"Travel Class":[0],"day":[29],"month":[3],"Journey Finish Point_le":[122],"Journey Start Point_le": [58],"Air Carrier_le":[28]})
prueba_prediccion_log=np.log(prueba_prediccion+1)
std_scale_prueba=preprocessing.StandardScaler().fit(prueba_prediccion_log)
prueba_scal = std_scale_prueba.transform(prueba_prediccion_log)
print("Predicciones",forest.predict(prueba_prediccion_log))
print("prediccion_real", np.exp(forest.predict(prueba_prediccion_log)))

