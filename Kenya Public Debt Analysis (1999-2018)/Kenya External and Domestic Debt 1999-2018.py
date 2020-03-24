# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:42:42 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import matplotlib.ticker as mtick
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel(r'C:\Users\KIRIMI\.spyder-py3\My Projects\Kenya Public Debt Analysis (1999-2018)\Data\Public Debt (Ksh Million).xlsx', Sheet=1)
df.head(4)
df.tail(4)
df.shape
df['Total Debt']= df.loc[:,['Domestic Debt', 'External Debt']].sum(axis=1)
df.drop('Total', axis=1, inplace=True)
df.isnull().sum().sum()
df.dtypes
df['Dates'] = pd.to_datetime(df['Year'].astype(str)  + df['Month'], format='%Y%B')
df.dtypes
df.head(10)
df.drop(['Year', 'Month'], axis=1, inplace=True)
df = df.round({'Domestic Debt':0, 'External Debt':0, 'Total Debt':0})
df.head(4)
# yourdate = '2003-01-01'
# print((df['Dates'] == yourdate).any())
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10,18))
plt.style.use('bmh')

#PLOT NO1-Kenya's Domestic and External Debt, September 1999-March 2018
line1 = ax1.plot(df['Dates'], df['Domestic Debt'], label='Domestic Debt')
line2 = ax1.plot(df['Dates'], df['External Debt'], label='External Debt')
date_formatter_1 = mdates.DateFormatter('%Y')
locator1 = mdates.YearLocator()
ax1.set(xlabel='Dates', ylabel='Amount in $', xlim = ['1999-09-01', '2018-03-01'])
ax1.xaxis.set_major_locator(locator1)
ax1.xaxis.set_major_formatter(date_formatter_1)
def new_tick_value(tick_value, pos):
    new_tick_value = tick_value/1000000
    new_tick_format = '{}M'.format(new_tick_value)
    return new_tick_format
ax1.yaxis.set_major_formatter(mtick.FuncFormatter(new_tick_value))
ax1.set_title('Kenya Domestic and External Debt, (September 1999 - March 2018)')
ax1.legend(loc='best')

#PLOT NO2-Kenya's 2nd President, President Mwai Kibaki Tenure Domestic and External Debt Analysis 2nd Term (January 2003-April 2013)
ax2.plot(df['Dates'], df['Domestic Debt'], label='Domestic Debt')
ax2.plot(df['Dates'], df['External Debt'], label='External Debt')
ax2.set(xlabel='Dates', ylabel='Amount in $', xlim = ['2003-01-01', '2013-04-01'])
date_formatter_2 = mdates.DateFormatter('%Y')
locator2 = mdates.YearLocator()
ax2.xaxis.set_major_locator(locator2)
ax2.yaxis.set_major_formatter(mtick.FuncFormatter(new_tick_value))
ax2.xaxis.set_major_formatter(date_formatter_2)
ax2.set_title('President Mwai Kibaki Tenure Domestic and External Debt, (Jan 2003-April 2013)')
ax2.legend(loc='best')
#PLOT NO3-Kenya's 3rd President, President Uhuru Kenyatta Tenure Domestic and External Debt Analysis (January 2003-January 2008)
ax3.plot(df['Dates'], df['Domestic Debt'], label='Domestic Debt')
ax3.plot(df['Dates'], df['External Debt'], label='External Debt')
ax3.set(xlabel='Dates', ylabel='Amount in $', xlim = ['2013-05-01', '2018-03-01'])
date_formatter_3 = mdates.DateFormatter('%Y')
locator3 = mdates.YearLocator()
ax3.xaxis.set_major_locator(locator3)
ax3.xaxis.set_major_formatter(date_formatter_3)
ax3.yaxis.set_major_formatter(mtick.FuncFormatter(new_tick_value))
ax3.set_title('President Uhuru Kenyatta Tenure Domestic and External Debt (January 2013-March 2018)')
ax3.legend(loc='best')
plt.tight_layout()
plt.show()
