#!/usr/bin/env python
# coding: utf-8

# # Data structures and Objects
# 
# # what is data structures or objects?
# 
# #storing the data in our computer is known as data structures

# In[1]:


#Integer

#whole numbers
a=10
b=20


# In[2]:


a+b


# In[3]:


#to identify the type of data we can use type() function

type(a)


# In[4]:


#Data container for whole numbers will not work for floating numbers


# In[13]:


#floating numbers/float

c=1.2
d=2.6
e=8


# In[14]:


c+d


# In[15]:


type(e)


# In[16]:


type(e)


# In[17]:


#string 
#it is a datatype of which stores in meaninf of ascii


# In[39]:


ch='Pavan Kumar'
ch1='sami'


# In[40]:


ch1


# In[41]:


type(ch1)


# In[42]:


ch+" space  "+ch1


# # List
# 

# In[43]:


#list is a container which can hold different datatypes in it

#it is a oredered sequence


# In[77]:


lst=['Pavan',4,1.46,[1,3,'sai']]


# In[78]:


lst


# In[79]:


lst[3][1]


# In[80]:


lst[3][0]


# In[81]:


#List is a complex datatype which derived from list object

#List elements are always stored in ordered sequence of number starting from 0

#Every object will have some methods
#lets see List object's methods


# In[82]:


lst.append("sami")  #append will adds the element at athe end of the list


# In[83]:


lst


# In[84]:


lst.index(1)


# In[85]:


lst.index(4)


# In[86]:


lst[-2]


# In[87]:


lst[3][1]


# #  DICT-Dictionaries
# 

# In[1]:


#This is a key value pair data structure,it is complex
#it is a object of DICT class in python

#data is stored like

#{'KEY':'value'}


# In[6]:


dict={'name':'Pavan','study':'Btech','age':'19','num':'9586'}


# In[7]:


dict


# In[9]:


#get is used to retreive the data from dictionary
dict.get('study')


# In[11]:


dict.keys()


# In[12]:


dict.items()


# In[15]:


#to add a new value to dictionary
dict['school']='Little star'


# In[16]:


dict


# In[18]:


dict.update({'num':'9701'})


# In[19]:


dict


# In[20]:


type(dict)


# In[24]:


dict.setdefault('name')


# # sets
# 

# In[25]:


#sets are used for storing unique values in python
#Sets are complex data structures
#Sets are class in a python,whose objects can be derived
#sets are mostly used for finding UNION,disjoin and finding commons and uncommons in the python data types


# In[27]:


st={'pavan','shiri',1,2,34,44,1,1,2,2}


# In[28]:


st


# In[29]:


st1={'prasad','ravi',1,4,6,7,1,4}


# In[30]:


st.difference(st1)


# In[31]:


st.intersection(st1)


# In[35]:


st.intersection_update(st1)


# # Tuple

# In[36]:


#Tuples are ordered immutable collection of objects
#once the data is written it cannot be changed=(immutable)


# In[48]:


tup=('pavan',1,2,3,'ravi')


# In[49]:


tup


# In[50]:


tup.count(1)


# In[51]:


tup.index(3)


# In[52]:


tup.index('ravi')


# # Boolean

# In[53]:


#This is a basic data type which stores TRUE or FALSE


# In[54]:


abc=True


# In[55]:


xyz=False


# In[ ]:




