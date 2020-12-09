#you have an app that monitors the electricity - kwtdata
#you want it to show you how much you save or not 
#you want to it to show the distrib of your app accross the regions and benchmark with another similar app 

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

#analysis on two parts, energy, the statup aspects

#ENERGY ASPECT

#open file the energy file
energy=pd.read_csv('energy.csv')
print(energy.columns)
df=DataFrame(energy.head(500))
print(df.head(500))

#Seeing trends by grouping kwt per season ans weekday as well as aggs
kwt_season=df.groupby(['Season'])[['Active_kwt']]
print(kwt_season.mean())

kwt_week=df.groupby(['weekday'])[['Active_kwt']]
print(kwt_week.mean())

#Aggregate
operations=['mean','sum','min','max']
kwt_agg=df.groupby(['Year','Month'], as_index=False)[['Active_kwt']].agg(operations)
print(kwt_agg.reset_index())

#seeing trends per month with violins
sns.violinplot(x=df["Month"], y=df["Active_kwt"], palette="Blues")
#plt.show()

#when is the kwt consumption more dense in general?
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
df.groupby('Day_Time')['Active_kwt'].count().sort_values().plot(kind='bar')
plt.ylabel('Active_kwt')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the day')

#when is the kwt consumption more dense in December

#filter december
December=df[df.Month=='Dec']

#aggregate data in charts
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
December.groupby('Day_Time')['Active_kwt'].count().sort_values().plot(kind='bar')
plt.ylabel('Active_kwt')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the day in Deceember')


fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
December.groupby('weekday')['Active_kwt'].count().sort_values().plot(kind='bar')
plt.ylabel('Active_kwt')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the week in Deceember')


#Does 2019 mean more electric consumption? answer is yes 
df.groupby('Year')['Active_kwt'].sum().plot(kind='bar')
plt.ylabel('Active_kwt')
plt.title('2019-2018 comparison')


#--------------PIVOTTIONS----------------------

pivotday=df.pivot_table(index='weekday',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#filter december
December=df[df.Month=='Dec']
print(December.tail(4))
pivotday=December.pivot_table(index='weekday',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

pivotday=December.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#----------------------CORRELATIONS--per months----------------
#corr graphs 
#Watching correlations 
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()

#December corrs
plt.figure(figsize=(8,5))
sns.heatmap(December.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()

#Jan corrs
January=df[df.Month=='Jan']
plt.figure(figsize=(8,5))
sns.heatmap(January.corr(),annot=True,cmap='viridis',mask=np.triu(df.corr(),k=1))

#whole corr heatmap
plt.figure(figsize=(10,10))
plt.title('Active_kwt - Room', y=1.05, size=15)
sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()

#correlation table for December 

plt.figure(figsize=(10,10))
plt.title('Active_kwt - Room', y=1.05, size=15)
sns.heatmap(December.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()
#Active kwt and rooms correlate

#scatters on energy per week

vissual = sns.lmplot(data=df, x='weekday', y='Active_kwt',
                 fit_reg=False)
plt.show()

#the further we move in the week, the more consumption we have 











