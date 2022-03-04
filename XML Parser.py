#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET


# In[2]:


tree = ET.parse('records.xml')
root = tree.getroot()


# In[13]:


for student in root.findall("student"):
    first_name = student.find('name/first_name').text
    last_name = student.find('name/last_name').text
    email = student.find('email').text
    print(first_name," ",last_name, " : ",email)


# In[36]:


for student in root.find("student"):
    print(student)


# In[41]:


for student in root.find("student"):
    print(student.tag)


# In[45]:


n = input("Enter a name : ")
for student in root.findall("student"):
    first_name = student.find("name/first_name").text
    if(n == first_name):
        print(first_name , student.find("name/last_name").text ," - ", student.find("email").text)


# In[ ]:




