# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:39:33 2018

@author: jpmul
"""

import pandas as pd
import numpy as np

df = pd.read_csv('specific_heat_capacity_air.csv', sep=',')

z = np.polyfit(x=df.loc[:, 'temp_K'], y=df.loc[:, 'Cp_kjkgK'], deg=4)
cp_air = np.poly1d(z)

df[f'poly_cp_air'] = cp_air(df.temp_K)

print(df)




