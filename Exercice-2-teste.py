#!/usr/bin/env python
# coding: utf-8

# # Exam

# ## exercice 2

# In[10]:


def polynomial_2(a):

        if (not int(a)):
            print("a can no be a strings")
            a=int(input("a="))
            polynomial_2(a)
        elif (a<0):
            print("a needs to be >0")
            a=int(input("a="))
            polynomial_2(a)
        elif (a.real != a) :
            print("a need to be real")
            a=int(input("a="))
            polynomial_2(a)
        elif (1>a>1000) :
            print("a needs to be <1000 and >1")
            a=int(input("a="))
            polynomial_2(a)
        else:
            return(a**3-1.5*a**2-6*a+5)
       


# In[21]:


polynomial_2("hi")


# In[ ]:





# In[ ]:





# In[ ]:




