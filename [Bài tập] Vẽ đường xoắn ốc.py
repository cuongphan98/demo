#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

c = int(input("nhap "))
a = 10
t= turtle.Turtle()
while True:
    t.forward(a)
    t.left(91)
    a +=1
    turtle.hideturtle()
    end = turtle.distance(t)
    print(int(end))
    if c == int(end):
        break
turtle.done()


# In[ ]:




