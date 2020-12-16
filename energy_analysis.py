
#We are dealing with a startup that is working on an electric energy monitoring app for households and in the future for businesses 
# This is an electric energy consumption analysis for threee regions, Berlin, GronIngen and Amsterdam.  
#the data is taken from an people living in dofferent households, that are using this app 
#we are interested to understand the Kwt consumption behaviour not only in different regions but aso in different households, for years 2018-2019
#Anlyzing the Kwt behaviour accross the units, regions and its seasonality, may help us better understand how we waste energy or we save energy and therefore 
#optimize costs and even be more evironmentally conscous. 

#the analysis wil take part in two stages
#-part I - Active Kwt behaviour 
#-part II - economic startup context 
#-part III-costs and investents 


"""Part I"""

#we did:
#exploratory data analysis 
#pivotations 
#correlations
#pairplots that helped us understand the correlations
#2d histogram to follow ditribution hourly kwt consumptipn accorss day, month or region
#extracted the data according to region, month or number of room household and performed further analysis 


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

#mean kwh in a season 
#mean kwh/mnth in a month
kwt_season=df.groupby(['Month','Season'])[['Active_kwh_month', 'Kwh']]
print(kwt_season.mean())

kwt_week=df.groupby(['weekday'])[['Kwh']]
print(kwt_week.mean())

#sum of kwh/hour in a weekday keeping in mind that appliances are kept on 6.5 h a day for room 5 unit
room5=df[df.Room_household==5]
kwt_week=room5.groupby(['weekday'])[['Kwh']]
print(kwt_week.sum())

#sum of kwh/hour in a weekday keeping in mind that appliances are kept on 6.5 h a day for room 2 unit
room2=df[df.Room_household==2]
kwt_week=room2.groupby(['weekday'])[['Kwh']]
print(kwt_week.sum())

#Aggregate
operations=['mean','sum','min','max']
kwt_agg=df.groupby(['Year','Month'], as_index=False)[['Kwh']].agg(operations)
print(kwt_agg.reset_index())

#--------------Graphs---------------------------

#when is the kwt consumption more dense in December

#filter december
December=df[df.Month=='Dec']
#aggregate data in charts
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
December.groupby('Day_Time')['Kwh'].count().sort_values().plot(kind='line')
plt.ylabel('Active_kwh_month')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the day in Deceember')
plt.show()

#Midday most consumption as it gets darker earlier 

#daytime kwt consumption in December is during midday
fig, ax=plt.subplots(figsize=(6,4))
sns.set_style('darkgrid')
December.groupby('weekday')['Active_kwh_month'].count().sort_values().plot(kind='line')
plt.ylabel('Active_kwh_month')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Kwt consumption during the week in Deceember')
plt.show()

#Does 2019 mean more electric consumption? 
df.groupby('Year')['Active_kwh_month'].sum().plot(kind='bar')
plt.ylabel('Active_kwh_month')
plt.title('2019-2018 comparison')
plt.show()

#Does 2019 mean more kwh consumption? 
df.groupby('Year')['Kwh'].sum().plot(kind='bar')
plt.ylabel('Active_kwh_month')
plt.title('2019-2018 comparison')

#answer is yes but2018 modre dense. 


#--------------PIVOTTIONS----------------------

pivotday=df.pivot_table(index='weekday',columns='Kwh', aggfunc={'Kwh':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

#filter december
December=df[df.Month=='Dec']
print(December.tail(4))
pivotday=December.pivot_table(index='weekday',columns='Kwh', aggfunc={'Kwh':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

pivotday=December.pivot_table(index='Year',columns='Active_kwh_month', aggfunc={'Active_kwh_month':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_1=df[df.Room_household==1]

pivotday=Room_1.pivot_table(index='Year',columns='Kwh', aggfunc={'Kwh':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_2=df[df.Room_household==2]

pivotday=Room_2.pivot_table(index='Year',columns='Active_kwh_month', aggfunc={'Active_kwh_month':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_3=df[df.Room_household==3]

pivotday=Room_3.pivot_table(index='Year',columns='Active_kwh_month', aggfunc={'Active_kwh_month':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_4=df[df.Room_household==4]

pivotday=Room_4.pivot_table(index='Year',columns='Active_kwh_month', aggfunc={'Active_kwh_month':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)

Room_5=df[df.Room_household==5]
Room_4=df[df.Room_household==4]

pivotday=Room_5.pivot_table(index='Year',columns='Active_kwh_month', aggfunc={'Active_kwh_month':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)



#----------------------CORRELATIONS--per months----------------
#corr graphs 
#Watching correlations 
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()
#region with kwh
#kwh household and kwh per month


#December corrs
plt.figure(figsize=(8,5))
sns.heatmap(December.corr(),annot=True,cmap='Blues_r',mask=np.triu(df.corr(),k=1))
plt.show()
#region with kwh
#kwh household and kwh per month
#kwh with day


#Jan corrs
January=df[df.Month=='Jan']
plt.figure(figsize=(8,5))
sns.heatmap(January.corr(),annot=True,cmap='viridis',mask=np.triu(df.corr(),k=1))
plt.show()
#region with kwh
#kwh household and kwh per month
#kwh year not with day

#whole corr heatmap
plt.figure(figsize=(10,10))
plt.title('Active_kwh_month - Room', y=1.05, size=15)
sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()
#region with kwh
#kwh household and kwh per month
#region with number of rooms 
#kw with number of rooms 
#day corred with h
#day with active per mth but not with kwh

# CORRELATION IN A MONTH, DEC
plt.figure(figsize=(10,10))
plt.title('Active_kwh_month - Room December', y=1.05, size=15)
sns.heatmap(December.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()


#PAIRPLOTS
#Now that these two correlate, a pair plot will show the consumption behaviour 
pairplot = sns.pairplot(df, vars=['Room_household','Active_kwh_month'])
plt.show()
#the more rooms we have, the larger the consumption per month

pairplot = sns.pairplot(December, vars=['Room_household','Kwh'])
plt.show()
#same tendency 

#kwh per season
#The more we head to winter, we consume more 
Regional_vissual = sns.lmplot(data=December, x='Season', y='Active_kwh_month',
                 fit_reg=False)
plt.show()

#scatters on energy per week
vissual = sns.lmplot(data=df, x='weekday', y='Kwh',
                 fit_reg=False)
plt.show()
#the further we move in the week, the more consumption we have 


#----------------Corrs for house hold rooms


Room_3=df[df.Room_household==3]
Room_5=df[df.Room_household==5]
Room_4=df[df.Room_household==4]


#correlation showing kwt consumption for household with 3 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwt-day correlation (3 room household)', y=1.05, size=15)
sns.heatmap(Room_3.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()

#correlation table  kwt-day is correlated 0.14


#correlation showing kwt consumption for household with 4 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwh_month-day correlation (4 room household)', y=1.05, size=15)
sns.heatmap(Room_4.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()

#stronger correlations thatn with day, hour are stronger than in the 3 room household


#correlation showing kwt consumption for household with 5 rooms
plt.figure(figsize=(10,10))
plt.title('Active_kwh_month-day correlation (4 room household)', y=1.05, size=15)
sns.heatmap(Room_5.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='viridis', linecolor='white', annot=True)
plt.show()
#no correlations due to the fact that there were not enough households

region_corr=df[['Active_kwh_month','Region','Season','Room_household']].copy()
plt.figure(figsize=(10,10))
plt.title('Region - Active_kwh_month correlations', y=1.05, size=15)
sns.heatmap(region_corr.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='Blues', linecolor='white', annot=True)
plt.show()
#correlation kwt-rooms  0.39 


#--------------------------Pairplots

#in order to see kwt consumption behavious for rooms with different number of rooms, pairplots will be displyed. 

pairplot = sns.pairplot(Room_4, vars=['Hour','Active_kwh_month'])
plt.show()

pairplot = sns.pairplot(Room_3, vars=['Hour','Active_kwh_month'])
plt.show()

pairplot = sns.pairplot(region_corr, vars=['Region','Active_kwh_month'])
plt.show()



#--------------------REGIONS----Watching kwt behaviour in regions

Regional_vissual = sns.lmplot(data=December, x='Region', y='Active_kwh_month',
                 fit_reg=False)
plt.show()

#Amsterdam region got more kwt consumption

Regional_vissual = sns.lmplot(data=Room_4, x='Region', y='Active_kwh_month',
                 fit_reg=False)
plt.show()

kwt=df
df = px.data.tips()
fig = px.density_heatmap(Room_4, x="Region", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
#plotly.offline.plot(fig, filename='kwt')
#In Amsterdam we have  25 units with 4 rooms  consuming 4800 kwt
#In Groningen we have 40 units with 4 rooms consuming 4800  kwt
#Berlin consumes least. with for rooms 


#Amsterdam kwt in Winter 
Season=Room_4[Room_4.Season=='winter']
Amsterdam=Season[Season.Region=='Amsterdam']

#Amsterdam in weekday in 4 room units
df = px.data.tips()
fig = px.density_heatmap(Amsterdam, x="weekday", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
#plotly.offline.plot(fig, filename='kwt')

Berlin=Season[Season.Region=='Berlin'] 
df = px.data.tips()
fig = px.density_heatmap(Berlin, x="weekday", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
#plotly.offline.plot(fig, filename='kwt')

df = px.data.tips()
fig = px.density_heatmap(Berlin, x="Hour", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
plotly.offline.plot(fig, filename='kwt')
#In Berlin not so many units with 4 rooms but those that are consumme consistently. 
#in the weekend kwt consumption stays the same but the number consumming that much increases. People are more at home. 

#----------------HOURLY behaviour

# hourly distribution of kwt for 4 rooms household, in winter. 

Season=Room_4[Room_4.Season=='winter']
df = px.data.tips()
fig = px.density_heatmap(Season, x="Hour", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
plotly.offline.plot(fig, filename='kwt')
#In winter the day is short as it darkens at arounf 15. Therefore kwt consumption in 4 room units, 
# starts to increase at around 15, up to 4800 Actve kwt ad 17 5600 kwt. 

Season=Room_4[Room_4.Season=='winter']
df = px.data.tips()
fig = px.density_heatmap(Season, x="weekday", y="Active_kwh_month", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Kwt consumption distribution accross the regions')
plotly.offline.plot(fig, filename='kwt')




























