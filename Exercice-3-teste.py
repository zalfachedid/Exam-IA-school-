#!/usr/bin/env python
# coding: utf-8

# # Exam

# ## Exercice 3

# In[6]:


import numpy as np


# In[4]:


import math as mt


# In[13]:


def pricer (s,x,t,r,y,N) :
    d1=(mt.log10(s/x)+(r+ (y**2)/2)*t)/(y*mt.sqrt(t))
    d2=(mt.log10(s/x)+(r- (y**2)/2)*t)/(y*mt.sqrt(t))
    c=s*N[d1]-x*mt.exp(-r*t)* N[d2]
    p=x*mt.exp(-r*t)*N[-d2]-s*N[-d1]
    return p,c


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




