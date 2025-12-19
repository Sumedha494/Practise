#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Method_1
with open("example.txt", "r") as file:
    data = file.read()

print(data)


# In[ ]:


#Method_2
import pandas as pd

df = pd.read_csv("customers.csv")
df.head()


# In[ ]:


#Method_3
import pandas as pd

df = pd.read_excel("customers.xlsx")
df.head()

