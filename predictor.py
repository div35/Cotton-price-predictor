#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import sys
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from keras.models import load_model
from sklearn.preprocessing import StandardScaler


# In[ ]:


data = sys.argv
Us=float(data[1])
temp=int(data[2])
Fer=int(data[3])
bri=int(data[4])
yell=float(data[5])
oil=float(data[6])
pr=int(data[7])
fibe=float(data[8])
clim=data[9]
state=data[10]
month=data[11]
input_data=[Us,temp,Fer,bri,yell,oil,pr,fibe,clim,state,month]


# In[ ]:


dataset = pd.read_csv('data.csv')
dataset = dataset.iloc[:,:-1].values


# In[ ]:


ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [8,9,10])], remainder='passthrough')
dataset = ct.fit_transform(dataset)


# In[ ]:


sc = StandardScaler()
sc.fit(dataset)


# In[ ]:


model = load_model('cpp.h5')


# In[ ]:


input_data = np.array(input_data)
input_data = input_data.reshape(1,-1)
input_data = ct.transform(input_data)
input_data = sc.transform(input_data)
print(model.predict(input_data)[0])


# In[ ]:




