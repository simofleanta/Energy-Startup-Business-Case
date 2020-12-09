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

#--------------Graphs---------------------------

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

#Midday most consumption

#daytime kwt consumption in December is during midday
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
December.groupby('weekday')['Active_kwt'].count().sort_values().plot(kind='bar')
plt.ylabel('Active_kwt')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the week in Deceember')

#Does 2019 mean more electric consumption? 
df.groupby('Year')['Active_kwt'].sum().plot(kind='bar')
plt.ylabel('Active_kwt')
plt.title('2019-2018 comparison')
#answer is yes 


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

Room_1=df[df.Room_household==1]

pivotday=Room_1.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_2=df[df.Room_household==2]

pivotday=Room_2.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_3=df[df.Room_household==3]

pivotday=Room_3.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_4=df[df.Room_household==4]

pivotday=Room_4.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_5=df[df.Room_household==5]
Room_4=df[df.Room_household==4]

pivotday=Room_5.pivot_table(index='Year',columns='Active_kwt', aggfunc={'Active_kwt':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#----------------------CORRELATIONS--per months----------------
#corr graphs 
#Watching correlations 
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))

#December corrs
plt.figure(figsize=(8,5))
sns.heatmap(December.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
#the only corrlation-room numbers and kwt consumption in Dec

#Jan corrs
January=df[df.Month=='Jan']
plt.figure(figsize=(8,5))
sns.heatmap(January.corr(),annot=True,cmap='viridis',mask=np.triu(df.corr(),k=1))
#the only corrlation-room numbers and kwt consumption in Jan

#whole corr heatmap
plt.figure(figsize=(10,10))
plt.title('Active_kwt - Room', y=1.05, size=15)
sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
#correlation table  kwt-rooms


plt.figure(figsize=(10,10))
plt.title('Active_kwt - Room December', y=1.05, size=15)
sns.heatmap(December.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
#Active kwt and rooms correlate december

#Now that these two correlate, a pair plot will show the consumption behaviour 
pairplot = sns.pairplot(df, vars=['Room_household','Active_kwt'])

# this shows that the more rooms are ther in house hold the bigger the kwt consumption with an exceptionfor 5 room house holdes,
#probably because they are not so many with 5 rooms:)

#scatters on energy per week
vissual = sns.lmplot(data=df, x='weekday', y='Active_kwt',
                 fit_reg=False)
#the further we move in the week, the more consumption we have 

#since we have a clear behaviour, a pairplot may show it better
pairplot = sns.pairplot(df, vars=['weekday','Active_kwt'])


#----------------Corrs for house hold rooms


Room_3=df[df.Room_household==3]
Room_5=df[df.Room_household==5]
Room_4=df[df.Room_household==4]


#correlation showing kwt consumption for household with 3 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwt-day correlation (3 room household)', y=1.05, size=15)
sns.heatmap(Room_3.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)

#correlation table  kwt-day is correlated 0.14

#correlation showing kwt consumption for household with 4 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwt-day correlation (4 room household)', y=1.05, size=15)
sns.heatmap(Room_4.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)

#stronger correlations thatn with day, hour are stronger than in the 3 room household

#correlation showing kwt consumption for household with 5 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwt-day correlation (4 room household)', y=1.05, size=15)
sns.heatmap(Room_5.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
#no correlations due to the fact that there were not enough households

#--------------------------Pairplots

#in order to see kwt consumption behavious for rooms with different number of rooms, pairplots will be displyed. 

pairplot = sns.pairplot(Room_4, vars=['Hour','Active_kwt'])


pairplot = sns.pairplot(Room_3, vars=['Hour','Active_kwt'])


#the later it is the higher is the consumption is 
#the later in the week the higher the kwt consumption
#-----------------------Watching kwt behaviour in regions

Regional_vissual = sns.lmplot(data=December, x='Region', y='Active_kwt',
                 fit_reg=False)


#Amsterdam region got more kwt consumption

Regional_vissual = sns.lmplot(data=Room_4, x='Region', y='Active_kwt',
                 fit_reg=False)


kwt=df
df = px.data.tips()
fig = px.density_heatmap(Room_4, x="Region", y="Active_kwt", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
#plotly.offline.plot(fig, filename='kwt')
#In Amsterdam we have  25 units with 4 rooms  consuming 4800 kwt
#In Groningen we have 40 units with 4 rooms consuming 4800  kwt
#Berlin consumes least. with for rooms 

# hourly distribution of kwt for 4 rooms household, in winter. 

Season=Room_4[Room_4.Season=='winter']
df = px.data.tips()
fig = px.density_heatmap(Season, x="Hour", y="Active_kwt", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
#plotly.offline.plot(fig, filename='kwt')
#In winter the day is short as it darkens at arounf 15. Therefore kwt consumption in 4 room units, 
# starts to increase at around 15, up to 4800 Actve kwt ad 17 5600 kwt. 

Season=Room_4[Room_4.Season=='winter']
df = px.data.tips()
fig = px.density_heatmap(Season, x="weekday", y="Active_kwt", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
plotly.offline.plot(fig, filename='kwt')






















