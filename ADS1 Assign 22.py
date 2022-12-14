# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:13:51 2022

@author: 1030 G2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solution(filename,countries,columns):
    df = pd.read_csv(filename,skiprows=4)
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries]
    return df,df.transpose()

filename = 'API_EN.ATM.GHGT.KT.CE_DS2_en_csv_v2_4748515.csv'
countries = ['Uganda','South Africa','Zimbabwe','Zambia','Tunisia','Tanzania','Nigeria','Togo']
columns = ['Country Name', '2014','2015','2016','2017','2018','2019']
 
cnty_GHG,year_GHG = solution(filename,countries,columns)

from matplotlib import pyplot
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_GHG .index,year_GHG[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend showing the pattern of GHG in the 8 countries')
plt.xlabel('Year')
plt.ylabel('Total Greenhouse Gas Emission ')
pyplot.show()


print(cnty_GHG.describe())

print(year_GHG.describe())

cnty_GHG.plot(kind='bar')
plt.title('Grouped bar for GHG emission for different countries over the years')
plt.xlabel('Countries')
plt.ylabel('GHG emission')
plt.rcParams["figure.dpi"] = 1000
plt.show()

year_GHG.plot(kind='bar')
plt.title('Grouped bar for GHG emission for different years across countries')
plt.xlabel('Years')
plt.ylabel('GHG emission')
plt.legend(bbox_to_anchor=(1.02, 0.7), loc='upper left', borderaxespad=0)
plt.rcParams["figure.dpi"] = 1000
plt.show()

year_GHG.corr()

plt.figure(figsize=(8,5))
sns.heatmap(year_GHG.corr(),annot=True)
plt.title('Correlation heatmap of the selected Africa Countries')
plt.show()