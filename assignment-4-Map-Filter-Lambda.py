#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


# In[1]:


a=int(input("Enter the number:" ))
result=lambda a:a+25
print(result(a))


# In[ ]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.


# In[7]:


def triple(a):
    return a+a+a
list1=[]
input_1=int(input("Enter the size of a list :"))
for i in range(input_1):
    list1.append(int(input("Enter the numbers: ")))
print(list1)
result=list(map(triple,list1))
print(result)


# In[ ]:


#Write a Python program to square the elements of a list using map() function.


# In[8]:


def square(a):
    return a*a
Sample_List=[]
list1=int(input("Enter the size of the sample list: "))
for i in range(list1):
    Sample_List.append(int(input("Enter the numbers: ")))
print(Sample_List)
output=list(map(square,Sample_List))
print(output)


# In[ ]:




