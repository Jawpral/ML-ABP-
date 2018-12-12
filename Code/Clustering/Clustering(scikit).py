#!/usr/bin/env python
# coding: utf-8

# # CLUSTERING WITH PYTHON
# ####  Using scikitlearn
# ##### LawJarp

# Importing all the important stuff

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering


# Creating a datasets of random points to be clustered
# X=all the x-coordinates of the points
# Y=all the y-coordinates of the points

# In[4]:


import random
X=[]
Y=[]
for i in range(200):
    x=random.choice([1,2,3])
    if x==1:
        X.append(random.choice(range(20)))
        Y.append(random.choice(range(20)))
    elif x==2:
        X.append(random.choice(range(30,50)))
        Y.append(random.choice(range(30,50)))
    else:
        X.append(random.choice(range(60,80)))
        Y.append(random.choice(range(60,80)))
print("X : "+str(X))
print("Y : "+str(Y))


# #### The points on the scatter graph

# In[5]:


plt.scatter(X,Y)
plt.show()


# Lets use scklearn to find number of clusters

# In[6]:


ar=[]
for i in range(len(X)):
    t=[]
    t.append(X[i])
    t.append(Y[i])
    ar.append(t)
Ar=np.array(ar)


# In[11]:


cluster=AgglomerativeClustering(n_clusters=3,affinity='euclidean',linkage='ward')#Create a object trained
cluster.fit_predict(Ar)


# In[12]:


plt.scatter(X,Y,c=cluster.labels_,cmap='rainbow')


# In[ ]:




