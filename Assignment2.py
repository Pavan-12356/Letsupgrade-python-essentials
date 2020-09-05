#!/usr/bin/env python
# coding: utf-8

# In[18]:


for num in range(1,201):
   if num > 1:
       for i in range(2, num):
           if num%i==0:
            break
       else:
             print(num,end=' ')
          


# In[21]:


aptitude=int(input())
if aptitude<=1000:
    print('safe to land')
elif aptitude>1000 and aptitude<5000:
    print('Bring down to 1000')
else:
    print('turn around')


# In[ ]:




