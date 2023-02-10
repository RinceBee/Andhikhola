# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:12:49 2023

@author: kumar
"""
import pandas as pd
a=350000.
b=170
pp=1700
hd=3600
w=1500
ca=4200

        
#1.5 ounces is about 44 milliliters
#5 ounces of wine is about 148 milliliters
#12 ounces of beer is about 354 milliliters
#Duration of party would be 4 hours, means , 140+3*(100*140/150)
d=b+1*(100*b/150)
e=round((0.25*d*44/750),0)
f=round((0.25*d*148/750),0)
g=round((0.5*d*354/(750*12)),0)
L=e*hd+f*w+g*ca
print(b*pp,L,b*pp+L)
print (e,"hd",f,"w",g,"c")
if b*pp+L < a:
    print("ok")
elif b*pp+L > a:
    print("not ok")
print("p",pp)
print("g",b)
print(round(L*100/(b*pp),1),"%")