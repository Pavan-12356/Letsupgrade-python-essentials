#!/usr/bin/env python
# coding: utf-8

# In[24]:


oldnumber = 0
previousNumber = 1
print('1')
for i in range(0,10):
    newNumber = previousNumber +oldnumber
    oldnumber = previousNumber
    previousNumber = newNumber
    print(newNumber)


# In[25]:


def fibonacci(n):
    oldnumber = 0
    previousNumber = 1
    print('1')
    for i in range(0,n):
        newNumber = previousNumber +oldnumber
        oldnumber = previousNumber
        previousNumber = newNumber
        print(newNumber)


# In[26]:


# Decorator  Function 
def inputDecoFun(argFun):
    
    def newFun():
        num = int(input("Enter any Number - "))
        argFun(num)
    return newFun


# In[33]:


@inputDecoFun
def fibonacci(n):
    oldnumber = 0
    previousNumber = 1
    print('1')
    for i in range(0,n):
        newNumber = previousNumber +oldnumber
        oldnumber = previousNumber
        previousNumber = newNumber
        print(newNumber)


# In[35]:


fibonacci()


# In[36]:


try:
    file = open("letsupgrade.txt","r")
    file.write("Hello world")
    file.close() 
    print("success")
except Exception as e:
    print(e)
finally:
    print("I want to write something in it")


# In[ ]:




