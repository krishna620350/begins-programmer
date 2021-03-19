#!/usr/bin/env python
# coding: utf-8

# # range datatype
#     it is a datatype of class range

# In[1]:


#range datatype
x=range(0,20)
print(x)
print(type(x))


# In[2]:


for i in range(0,20):
    print(i)


# In[3]:


for i in range(0,20,2):
    print(i)


# # set datatype
#     it do not allows duplicate values
#     insertion order is not presurve
#     we cannot perform slicing and indexing
#     mutiable in nature
#     important for compatitave exam

# In[7]:


l=[1,1,1,1,1,1]
x=list(set(l))
print(type(x),x)
#print(add(x))


# In[5]:


s={1,2,3,4,5,6,7,8,9}
x=frozenset(s)
print(x)
x.add(5)


# # dictonary
#     it is another type of data structure
#     in this it has two value 1 is data and 2 is key
#     key will not be duplicate data can be anything and even duplicate also
#     ordring and indixing is not applicable on dictonary
#     you access the values on the basis of keys
#     dictonary is mutable in nature

# In[8]:


t=(1,1,11,1)
print(t)


# In[9]:


d={1:"tanay",2:"aman",3:"prakash"}
print(d)


# # None data type
#     place holder variable

# # operator
#     areithmetic operator
#         exponent oprator
#         division
#             normal division is consider as floting point division
#             floor division depand on data type
#                 floor division operator give float value return if any value is float

# In[14]:


print(2**3)
print(5/2)
print(5//2)
print(5.0//2)


# # string with A.O
#     only two operator used with string one is + and *
# 

# In[16]:


s="kris"
c="hna"
print(s+c)
print("krishna"+1)


# In[18]:


print(50*"-")
print("-"*10)


# # tuple 
#     it is in inmutable in nature so it is used as key in dictonary

# In[19]:


d={(1,2,3):"krishna"}


# # relational operator
#     it always return boolean values 'True' or 'False'
#     in  string it compare where string is not same
#     == it only compare data not check its type

# In[20]:


a="rahul"
b="krishna"
a>b


# In[21]:


a="krisrahul"
b="krishna"
a>b


# In[22]:


print(True+1)


# In[23]:


10<20>30<40


# # logical operator
#     and,or,not

# In[24]:


True and False


# In[25]:


not True


# In[26]:


10 and 20
#in the case of integer if x and y is evaluted if x is false than it return x otherwise y


# In[28]:


10 and 10
0 and 20


# In[29]:


1 or 20


# In[30]:


0 or 19


# # bitwise operator 

# In[33]:


print(4&5)
print(4|5)
print(4<<1)
print(4>>1)


# In[37]:


# assignment operator
a=6
# compound assignment operator
a+=5
a
# multiple value assigment
a,b,c=4,5,6
print(a,b,c)
# list[] unpacking
# tuple() unpacking
a,b,c =[1,2,3]
print(a,b,c)
#in python return multiple value but in single object
# their is no increement,decreement and ternery operator in python


# In[40]:


#ternary operator
a,b,c,d=20,10,30,40
x=30 if a<b else 60 if c<d else 50
print(x)


# In[42]:


a,d,c=10,20,30
x=a if a>b else b if b>c else c
print(x)


# In[ ]:




