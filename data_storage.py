#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:35 2024

@author: ndivhuwo
#
#Storing data
#1.
#2.Dictionaries
#3. Data Frames
#"""

age = [30,25,29,46,22]

average = sum(age)/len(age)

print(average)

"""
Dictionaries
"""

grades = {"Denga":"9","Mukundi":"2"}

print(grades["Denga"])

"""
Data Frame

"""

fruit = {'Banana','orange','grapes'}
type_fruit = {'non_citrus','citrus','citrus'}
              
 market_fruit = {fruit:'type_fruit'}
 
 print(market_fruit)