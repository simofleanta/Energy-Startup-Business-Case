
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


#open file
startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
df=DataFrame(startup.head(700))
print(df.head(700))

#2019 ROI
#filtering the year

investment=100000
year2019=df[df.Year==2019]
Month2019=df[df.Month=='Dec']


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

#2018 ROI
#filtering the year

investment=70000
year2018=df[df.Year==2018]
Month2018=df[df.Month=='Dec']

#roi in dec 2018

#netprofit calculation
net_profit18=costs*12-loss

Costs=Costs=year2018['Costs']
Loss=Loss=year2018['Loss']

def generateROI(investment,Costs,Loss):
    """function generating ROI for 2018"""
    return net_profit18/investment*100
print(generateROI(investment,Costs,Loss))

Month2018=df[df.Month=='Dec']

Costs_18=Costs=Month2018['Costs']
Loss_18=Loss=Month2018['Loss']

#netprofit calculation
net_profit18_dec=Costs_18*12-Loss_18

def generateROI_dec18(investment,Costs,Loss):
    """function generating ROI for dec 2018"""
    return net_profit18_dec/investment*100
print(generateROI_dec18(investment,Costs_18,Loss_18))

#-------------------------------------------------------------------------

#profitability 


df['Cost_to_produce']=4000*df.Sale_frequency
df['Profitablity']=df.Cost_to_produce-df.Sales_rev
df['ROI_2019']=net_profit19/investment*100
df['ROI_2018']=net_profit18/investment*100

#After calculations, print columns to see calculations added to the dataframe
print(df.head(5))
energy_df=df
print(energy_df.columns)



#-------------------Merge part 1 and 2 and obtain month consumption calculation

#After calculations, print columns to see calculations added to the dataframe
print(df.head(5))
energy_df=df
print(energy_df.columns)

x=energy_df[['Profitablity','ROI_2019','ROI_2018','Client_Room_household','Sales_rev']].copy()

energy=pd.read_csv('energy.csv')
#print(energy.columns)
df=DataFrame(energy.head(500))
#print(df.head(500))

#Make copies of dfs to make easier to read it in a table
x=energy_df[['Year','Day','Month','Profitablity','ROI_2019','ROI_2018','Sales_rev']].copy()
y=df[['Year','Month','Kwh','Active_kwh_month','Room_household','Region']].copy()

#merge x+y 
z=pd.merge(x,y)
print(z)

#--------------------------------COST CALCULATIONS per month
#price = kWh × cost per kWh
#price = 97.2 kWh × .50
#kWh = 48.6

z['kwh_consumption_cost_month']=z.Active_kwh_month*0.84

#print the new data frame
print(z.head(20))























