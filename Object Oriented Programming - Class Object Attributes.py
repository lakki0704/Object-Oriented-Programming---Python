#!/usr/bin/env python
# coding: utf-8

# # Class Objects , Atrributes and Methods

# In[50]:


#OOP python
class Phone():
    
    operating_sys = "Andriod" #class object attribute
    def __init__(self, brand, RAM , Camera_px):
        #attributes
        self.brand= brand
        self.RAM = RAM
        self.camera= Camera_px
    
    #methods
    def design(self, ROM):
        print("Brand of this phone is {}".format(self.brand))
        print("It has Sleek design")
        print("The ROM size is {}".format(ROM)) #no need to write self here as it is given as a parameter to design()
        print("OS : {}".format(self.operating_sys)) # this also has to be called using self.


# In[51]:


myPhone = Phone("Realme7","8GB", "64MP")


# In[52]:


print(myPhone.brand) #no paranthesis requires for attributes 
print(myPhone.RAM)
print(myPhone.camera)

print(myPhone.operating_sys, ", This will always be same though it's not defined under fucnation int")


# In[53]:


myPhone.design("64GB") 
#it will not display anything unless paranthesis is given 
#for method , call it using ()
# we can pass as many params as we want


# In[ ]:





# In[ ]:




