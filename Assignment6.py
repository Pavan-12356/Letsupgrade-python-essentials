#!/usr/bin/env python
# coding: utf-8

# In[59]:



class BankAccount:
    def __init__(self,ownerName,Balance):
        self.owner = ownerName
        self.Balance = Balance
        
    def deposit(self, Balance):
        self.Balance+= Balance
        print("Available Balance",self.Balance)
    
    def withdraw(self,Balance):
            if self.Balance >=Balance:
                self.Balance-=Balance
            else:
                print("withdraw is not Possible only " + str(self.Balance)+    'is avaliable')
            print(self.Balance)
        


# In[60]:


xaccount=BankAccount('pavan',500)


# In[61]:


xaccount.deposit(2000)


# In[62]:


xaccount.withdraw(3000)


# In[63]:


xaccount.withdraw(1000)


# In[75]:


import math
class cone:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def volume(self):
        self.volume = math.pi * self.radius * self.radius *(self.height/3)
        print("volume is:",self.volume)
    def surface_area(self):
        base = math.pi * self.radius*self.radius
        side = math.pi * self.radius*math.sqrt(self.radius**2 + self.height**2)
        self.surface_area=base + side
        print("surface area is:",self.surface_area)


# In[76]:


cone1=cone(9,8)


# In[77]:


cone1.volume()


# In[78]:


cone1.surface_area()


# In[ ]:




