#!/usr/bin/env python
# coding: utf-8

# # Basic Stack Implementation

# In[1]:


# Stack in python
# TODO - Create the three functions ie push, pop, print!

class Stack:
    
  
  def __init__(self):
    self.items = []
  
  def push(self, i):
    self.items.append(i) 

  
  def pop(self):
        return self.items.pop()
    
  
  def print(self):
  
    for x in range(len(self.items)):
        print(self.items[x])


# ### Main Function to call the stack class

# In[ ]:


# Initializing the object
stack = Stack()
value = 1
while value>0:
   
  task = int(input("Enter what you want to do\n 1 for pushing the element\n 2 for poping the element\n 3 for printing the stack\n"))
 
  if(task == 1):
  
    value = int(input("Enter the element\n"))
    stack.push(value)
    
 
  elif(task == 2):
    
    stack.pop()
   
  elif(task == 3):
  
    stack.print()

## Once Done Run the class        


# In[ ]:




