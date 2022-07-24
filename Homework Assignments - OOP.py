#!/usr/bin/env python
# coding: utf-8

# # Homework Assignment
# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line. 

# In[8]:


# importing "math" for mathematical operations 
import math 

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1x = coor1[0]
        self.coor2x = coor2[0]
        self.coor1y = coor1[1]
        self.coor2y = coor2[1]
        pass
    
    def distance(self):
        x = abs(self.coor1x - self.coor2x)
        x_sq = x**2
        y = abs(self.coor1y - self.coor2y)
        y_sq = y**2
        distance = (x_sq + y_sq)**0.5
        return distance
        pass
    
    def slope(self):
        y_diff = self.coor1y - self.coor2y
        x_diff = self.coor1x - self.coor2x
        # slope = math.tan(y_diff/x_diff)
        slope = y_diff/x_diff
        return slope
        pass


# In[9]:


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)


# In[10]:


li.distance()


# In[11]:


li.slope()


# # Problem 2

# In[12]:


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius 
        pass
        
    def volume(self):
        vol = 3.14*(self.radius**2)*self.height
        return vol
        pass
    
    def surface_area(self):
        curved_area = 2*3.14* self.radius*self.height
        top_and_bottom = 2*3.14*(self.radius**2)
        tsa= curved_area+ top_and_bottom
        return tsa
        pass


# In[13]:


c = Cylinder(2,3)


# In[14]:


c.volume()


# In[15]:


c.surface_area()


# In[ ]:




