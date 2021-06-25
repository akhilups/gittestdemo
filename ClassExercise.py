# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:41:58 2020

@author: admin
"""


'1. Number Of White Spaces In a sentence

Counter = 0
Inputline = "This is the line input"
for i in inputline:
    if (i.isspace()):
        Counter = Counter+1   
print(Counter)

'2. print only the first letter of every word in the given sentence.


Inputline2 = "This is the Second Exercise"

for word in Inputline2.split(): 
    print(word[0])
    
'3. for the give word abcdef  swap the string    

Inputline3="abcdef" 
temp=len(Inputline3) 
Final=Inputline3[temp::-1] 
print (Final) 

'4. print the average min , max and median in the given array.

import numpy as np


Inputline4 = [10,13,12,16,23,87,98]

mean = np.mean(Inputline4)
medi = np.median(Inputline4)
mini = np.min(Inputline4)
maxi = np.max(Inputline4)
print ("mean of the given array is",mean)
print ("median of the given array is",medi)
print ("Minimum of the given array is",mini)
print ("Maximum of the given array is",maxi)
