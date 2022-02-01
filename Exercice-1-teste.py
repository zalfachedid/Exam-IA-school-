#!/usr/bin/env python
# coding: utf-8

# # EXAM

# ## Exo 1

# # a

# In[9]:


def polynomiale(x):   
    u=x**3-1.5*x**2-6*x+5
    return u


# In[10]:


polynomiale(5)


# # b

# In[15]:


def factorielle(x):
    t=1
    if x==0 :
        return 1
    else :
        for i in range(1,x+1):
            t=t*i
    return t


# In[12]:


factorielle(1)


# In[18]:


factorielle(2)


# In[20]:


factorielle(5)


# # c

# In[38]:


def fibonacci(x):
    l=[0,1,1]
    if x<= 3:
        l=l[0:x+1]
    else:
        for i in range(x-3):
            u=l[-1]+l[-2]
            l.append(u)
    return l
        


# In[41]:


fibonacci (6)


# In[45]:


a=int(input("Entrez un nombre:"))
print("La suire fibonacci est:" )
print(fibonacci(a))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




