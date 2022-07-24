#!/usr/bin/env python
# coding: utf-8

# # Special Methods

# In[17]:


class Books():
    
    def __init__(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages
  
    def __str__(self): #special method , this returns strings. Whenever print() is called, it looks if the class has any __str__method
        #if yes, it returns the value that the __str__ method returns
        return f"{self.title} is written by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted !")


# In[18]:


novel = Books("Mahashweta", "Sudha Murthy" , 300)


# In[19]:


print(novel) #it looks in the class if it has any __str__ method (it's a special function)


# In[20]:


len(novel) #checks in the class if it has any __len__ method 


# In[21]:


# del novel ==> this will delete the object from the  memory

# we can also define it as a method inside the class by returning a print statement


# In[22]:


del novel


# In[ ]:




