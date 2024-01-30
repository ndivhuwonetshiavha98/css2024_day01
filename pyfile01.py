#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:45:52 2024

@author: ndivhuwo
"""

print('My first python file')
#This is my first python comment
 
import pandas

file = pandas.read_csv("country_data.csv")
print(file)

print(file.info())

print(file.describe())

column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
file2 = pandas.read_csv("housing_data.csv",names=column_names)
print(file2)
print(file2.info())
#file3 = pandas.read_csv("diab_data.csv")
#print(file3)

print(type(file2))

file7 = pandas.read_csv('insurance_data.csv',skiprows=(5))
print(file7)
