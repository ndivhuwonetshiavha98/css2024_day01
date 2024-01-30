#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:57:13 2024

@author: ndivhuwo
"""

import pandas as pd


file = pd.read_csv("insurance_data.csv",skiprows=(5))

print(file)


file1 = pd.read_csv("iris.csv")

print(file1)

