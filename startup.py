
"""Part II"""

import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px

#Business ASPECT
#currency-euro

#open file the energy file
startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
df=DataFrame(startup.head(700))
print(df.head(700))

#I Aggregate revs by house hold rooms

operations=['mean','sum','min','max']
sales_household=df.groupby(['Month','Client_Room_household'], as_index=False)[['Sales_rev']].agg(operations)
print(sales_household.reset_index())

#After aggregation, values could be better seen in a bar chart 
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df.groupby(['Client_Room_household','Month'])['Sales_rev'].sum().sort_values().plot(kind='bar')
plt.ylabel('Sales_rev')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Sum of sale revenues according to household unit throughout months')

#it seems that the more rooms a houldhold has, the higher the sales revs.
#summer autumn seem to have higher scores.

sales_season=df[df.Season=='winter']
winter_months=sales_season[sales_season.Month=='Dec']

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
sales_season.groupby(['Client_Room_household','Month'])['Sales_rev'].sum().sort_values().plot(kind='bar')
plt.ylabel('Sales_rev')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Sum of sale revenues according to household unit throughout months')

#Mean sales revs in units in the winter season weekdays
sales_season=df[df.Season=='winter']

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
sales_season.groupby(['Client_Room_household','weekday'])['Sales_rev'].mean().sort_values().plot(kind='bar')
plt.ylabel('Sales_rev')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Mean sale revenues according to household unit throughout winter months')

#aggregation winter weekdays

sales_season=df[df.Season=='winter']
winter_months=sales_season[sales_season.Month=='Dec']
autumn_season=df[df.Season=='autumn']
autumn_Sales=autumn_season[autumn_season.Month=='Nov']

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
sales_season.groupby(['Client_Room_household','Month'])['Sales_rev'].sum().sort_values().plot(kind='bar')
plt.ylabel('Sales_rev')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Sum of sale revenues according to household unit throughout months')

#-------------PIVOTS

#since autumn winter is highest in scores we will pivot max values for season and months and weekdays  

print(winter_months.tail(4))
pivotday=winter_months.pivot_table(index='weekday',columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

print(sales_season.tail(4))
pivotday=sales_season.pivot_table(index='Month',columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#in winter season Monday is more profitable
#in winter season most profitable Mar, Feb, December

#autumn season 
autumn_season=df[df.Season=='autumn']
print(autumn_season.tail(4))
pivotday=autumn_season.pivot_table(index='Month',columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

autumn_Sales=autumn_season[autumn_season.Month=='Nov']
print(autumn_Sales.tail(4))
pivotday=autumn_Sales.pivot_table(index='weekday',columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#thursday seems highest in scores
#Nov seems best in autumn season

#aggregations per region

autumn_season=df[df.Season=='autumn']
print(autumn_season.tail(4))
pivotday=autumn_season.pivot_table(index=['Month','Client_Room_household.1'],columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#Arhus is best

winter_months=df[df.Season=='winter']
print(winter_months.tail(4))
pivotday=winter_months.pivot_table(index=['Month','Client_Room_household.1'],columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#Hague, Groningen are best in winter. 














