#!/usr/bin/env python
# coding: utf-8

# In[68]:


import bs4


# In[69]:


from urllib.request import urlopen


# In[70]:


android_url="https://en.wikipedia.org/wiki/Android_version_history"


# In[71]:


android_data=urlopen(android_url)


# In[72]:


print(type(android_data))


# In[73]:


android_html=android_data.read()


# In[74]:


print(android_html)
android_data.close()


# In[75]:


from bs4 import BeautifulSoup as soup


# In[76]:


android_soup=soup(android_html,'html.parser')


# In[77]:


print(android_soup)


# In[78]:


print(type(android_soup))


# In[79]:


android_soup.h1


# In[80]:


android_soup.findAll('h1',{})


# In[81]:


tables=android_soup.findAll('table',{'class':'wikitable'})


# In[82]:


print(len(tables))


# In[83]:


android_table=tables[0]


# In[84]:


count=android_table.findAll('th')


# In[85]:


print(len(count))


# In[86]:


count[1].text


# In[87]:


column=[ct.text[:-1] for ct in count]
print(column)


# In[88]:


row_data=android_table.findAll('tr')[1:]


# In[89]:


print(len(row_data))


# In[98]:


row=row_data[0]


# In[96]:


print(row.text)


# In[150]:


table_rows=[]
for row in row_data:
    current_row=[]
    rows=row.findAll('td',{})
    
    for idx,data in enumerate(rows):
        if idx==0:
            current_row.append(data.text[:-1].split(":")[-1])
        elif idx!=1 or idx!=3:
            current_row.append(data.text[:-1])
        else:
            current_row.append(data.text)
    table_rows.append(current_row)


# In[151]:


print(table_rows)


# In[152]:


filename="android_version_history.csv"
with open(filename,'w',encoding='utf-8') as f:
    headerstring=','.join(column)
    headerstring+='\n'
    f.write(headerstring)
    for row in table_rows:
        rowin=""
        rowin=','.join(row)
        rowin+='\n'
        f.write(rowin)
        
        
    


# In[153]:


import pandas as pd

df=pd.read_csv('android_version_history.csv')


# In[155]:


df


# In[157]:


df.head(10)


# In[172]:


df.iloc[0][1]


# In[ ]:




