
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

fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
sales_season.groupby(['Client_Room_household','Month'])['Sales_rev'].sum().sort_values().plot(kind='bar')
plt.ylabel('Sales_rev')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Sum of sale revenues according to household unit throughout months')









