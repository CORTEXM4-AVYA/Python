#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[2,1,4]


# In[2]:


def mychoice():
    ch=-1
    while ch not in [0,1,2]:
        ch=int(input("Enter the choice from the list "))
        if ch not in [0,1,2]:
            print("wrong choice please enter again")
        else:
            return ch


# In[3]:


def replace_with(list1,ch):
    value= input('Enter the value you want to replace for the given choice')
    list1[ch]=value
    return list1
   


# In[ ]:


list1 
game=True
while game==True:
    position=mychoice()
    list2=replace_with(list1,position)
    print(list2)
    choice=input('Should we play press?? y/n')
    if choice=='y':
        game = True
    else:
        game= False
               


# In[ ]:





# In[ ]:




