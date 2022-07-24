#!/usr/bin/env python
# coding: utf-8

# # Inheritance

# In[55]:


# Base class

class Animals():
    
    def __init__(self):
        print("Animal class created (base)")
    def breed(self):
        print("Breed method is a part of base class")


# In[56]:


# methods in Animals can be reused in this class 
class Cats(Animals):
    
    def __init__(self):
        Animals.__init__(self)
        print("Cats class created which as Animals (class) as the base")
    def breed(self):
        print("Breed method is overwritten in Cats class")


# In[57]:


myCat = Cats()


# In[58]:


myCat.breed()


# # Polymorphism 
# 
# 

# In[59]:


class Pen():
    def __init__(self, company):
        self.company= company
    def purpose(self):
        print("This Pen's company is : {}".format(self.company))


# In[60]:


class Pencil:
    def __init__(self, company):
        self.company = company
    def purpose(self):
        print("This Pencil's company is : {}".format(self.company))


# In[61]:


pen = Pen("Cello")
pencil = Pencil("Apsara")


# In[62]:


pen.purpose()


# In[63]:


pencil.purpose()


# In[64]:


for item in [pen, pencil]:
    print(item.purpose())


# In[65]:


def purposes(item):
    return item.purpose()


# In[66]:


purposes(pen)


# In[67]:


purposes(pencil)


# In[68]:


class items:
    
    def __init__(self, name):
        self.name = name
    def purpose(self):
        raise NotImplementedError("The base class can't use it , it has to overwritten by subclasses")
        


# In[69]:


bottle = items("Milton bottle")


# In[70]:


# bottle.purpose() # will not do anything here
#subclass has to inherit Animal class and overwrite this methos


# In[52]:


#creating a subclass

class Bottle(items):
#     def __init__(self, name):
#         items.__init__(self, name)
#         self.name = name 
    def purpose(self): # method inherited from Base class : items()
        return self.name + " : Thermosteel "


# In[53]:


myBottle = Bottle("Milton")


# In[54]:


myBottle.purpose()


# In[ ]:




