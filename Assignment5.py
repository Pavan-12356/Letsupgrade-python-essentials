#!/usr/bin/env python
# coding: utf-8

# In[57]:


def getInput():
    tempList=[]
    i=0
    while i < 8:
        val = int(input(f"Enter number {i+1}: "))
        tempList.append(val)
        i+=1
    return tempList
def check(a):
    subList = [1,1,5]
    for i in a:
        for j in subList:
            if(len(subList)>=0 and j == i):
                subList.pop(0)
            else:
                break
    
    if len(subList)==0:
        return "It's a match"
    else:
        return "It's gone"
supList = getInput()        
print("Provided List is :",supList)
check(supList)


# In[71]:


def isprime(x):
    if (x < 2):
        return False
    for i in range(2,x):
        if (x % i == 0):
            return False
    return True

print(list(filter(isprime,range(2501))))


# In[50]:


strings=['hey sai this is letsupgrade','i am from mumbai']


# In[51]:


cap=map(lambda x: str.title(x),strings)


# In[52]:


cap


# In[53]:


list(cap)


# In[ ]:




