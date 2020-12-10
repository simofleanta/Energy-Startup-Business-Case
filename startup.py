
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
pivotday=autumn_season.pivot_table(index=['Month','Client_Region'],columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)
#Arhus is best

winter_months=df[df.Season=='winter']
print(winter_months.tail(4))
pivotday=winter_months.pivot_table(index=['Month','Client_Region'],columns='Sales_rev', aggfunc={'Sales_rev':'max'}).fillna(0)
pivotday['Max']=pivotday.idxmax(axis=1)
print(pivotday)
#Hague, Groningen are best in winter. 

#-----------------------------CORRelations

#correlation showing kwt consumption for household in December 
plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(winter_months.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()
#not correlated in december 

plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(autumn_season.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#not correlated

plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#not corred.

Client_Region=df[df.Client_Region=='Hague']
g=df[df.Client_Region=='Groningen']
Aarhus=df[df.Client_Region=='Aarhus']
plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(Client_Region.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#----------------Sales and Profit distributions

df = px.data.tips()
fig = px.density_heatmap(Client_Region, x="weekday", y="Month_Profit", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Monthly profit distribution in weekdays, in Hague')
#plotly.offline.plot(fig, filename='kwt')

df = px.data.tips()
fig = px.density_heatmap(Client_Region, x="weekday", y="Month_Profit", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Monthly profit distribution in weekdays, in Hague')
plotly.offline.plot(fig, filename='kwt')

df = px.data.tips()
fig = px.density_heatmap(g, x="weekday", y="Month_Profit", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Monthly profit distribution in weekdays, in Groningen')
#plotly.offline.plot(fig, filename='kwt')

df = px.data.tips()
fig = px.density_heatmap(Aarhus, x="weekday", y="Sales_rev", nbinsx=30, nbinsy=20, color_continuous_scale="RdBu",title='Monthly profit distribution in weekdays, in Groningen')
#plotly.offline.plot(fig, filename='kwt')

#-----------------------Roi


#After seeing correlations and the max, means values pivots, we can now see the ROI on different months or seasons, keeping in mind that sales 
#sale revenues increase autumn winter. 

#reopen file
startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
df=DataFrame(startup.head(700))
print(df.head(700))

#2019 ROI
#filtering the year

investment=100000
year2019=df[df.Year==2019]

costs=Costs=year2019['Costs']
loss=Loss=year2019['Loss']

#netprofit calculation
net_profit19=costs*12-loss

def generateROI(investment,costs,loss):
    """function generating ROI for 2019"""
    return net_profit19/investment*100
print(generateROI(investment,costs,loss))

#see roi per month 
Month2019=df[df.Month=='Dec']
investment_dec=89000

costs_dec=Costs=Month2019['Costs']
loss_dec=Loss=Month2019['Loss']

net_p_dec=costs_dec*12-loss_dec
print(net_p_dec)

def ROI_dec(investment_dec,costs_dec,loss_dec):
    """function generating ROI for 2019"""
    return net_p_dec/investment_dec*100
print(ROI_dec(investment_dec,costs_dec,loss_dec))


#2018 YEAR ROI
#filtering the year
investment=70000
year2018=df[df.Year==2018]

#netprofit calculation
net_profit18=costs*12-loss

#set costs and loss
Costs=Costs=year2018['Costs']
Loss=Loss=year2018['Loss']


#generate function roi
def generateROI(investment,Costs,Loss):
    """function generating ROI for 2018"""
    return net_profit18/investment*100
print(generateROI(investment,Costs,Loss))

#-------------------------------------------------

#roi in December month

#extract month
Month2018=df[df.Month=='Dec']

#set costs and loss
Costs_18=Costs=Month2018['Costs']
Loss_18=Loss=Month2018['Loss']

#netprofit calculation DEC 18
net_profit18_dec=Costs_18*12-Loss_18

#roi function
def generateROI_dec18(investment,Costs,Loss):
    """function generating ROI for dec 2018"""
    return net_profit18_dec/investment*100
print(generateROI_dec18(investment,Costs_18,Loss_18))

#---------------------------------------------------------------------

#calculate profitability

df['Cost_to_produce']=4000*df.Sale_frequency
df['Profitablity']=df.Cost_to_produce-df.Sales_rev
df['ROI_2019']=net_profit19/investment*100
df['ROI_2018']=net_profit18/investment*100

#subset with roi so I can decide whether to use the energy app for more rooms husehold. 

#After calculations, print columns to see calculations added to the dataframe
print(df.head(5))
energy_df=df
print(energy_df.columns)

#so after subsetting, will try a corr between roi and sales or househlds

#make a df copyright
x=energy_df[['Profitablity','ROI_2019','Client_Room_household','Sales_rev']].copy()

#correlation heatmap

plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(x.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#profitability with corr 0.054
#roi client household   0.0092
#roi with sales rev 0.054
#not corr profitability with client householld or very close to being corred
#overall very weak correlations 

#-------------------MERGE STARTUP ASPECT ANALYSIS AND ENERGY ANALYSIS 
#PART I+ PARTII =...

#add energy data and merge with x 

energy=pd.read_csv('energy.csv')
#print(energy.columns)
df=DataFrame(energy.head(500))
#print(df.head(500))

#Make copies of dfs to make easier to read it in a table
x=energy_df[['Year','Month','Profitablity','ROI_2019','ROI_2018','Client_Room_household','Sales_rev']].copy()
y=df[['Year','Month','Active_kwt','Region']].copy()

#merge x+y 
z=pd.merge(x,y)
print(z)

#perform correlations between business analysis and energy 
plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(z.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#quiet many corrs:
#profitability with client house hold, profitability, sales_rev, roi but not with active kwt
#active kwt with client room household and roi but, not with sales 
#sales_rev with client room house, profitability,roi but not with kwt
#roi with profitability and sales 
#client room household with kwt, sales and profitability and roi but not with 

#pairplots for correlation understanding

#the app should make client understand not only how much kwt are active during evening or end of the week
# /month, but also how much energy they could save. 
# figure out a for that calculation now that the data was merged into z df.














