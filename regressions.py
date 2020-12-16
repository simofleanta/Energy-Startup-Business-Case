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

e=pd.read_csv('energy.csv')
print(startup.columns)
sdf=DataFrame(e.head(700))
print(sdf.head(700))


startups=df[['Year','Day','Month','Client_Region','Month_Profit','Sales_rev']].copy()
energys=sdf[['Year','Month','Kwh','Room_household','Active_kwh_month','Room_household']].copy()

for_regressions=pd.merge(startups,energys)
print(for_regressions)

x=for_regressions.to_csv("reg.csv")
#print(x)

e=pd.read_csv('reg.csv')
print(startup.columns)
rdf=DataFrame(e.head(700))
print(rdf.head(700))

print(rdf.columns)


for_regressions=df
df = px.data.tips()
fig = px.scatter(for_regressions, x="Month_Profit", y="Costs", trendline="m")
#plotly.offline.plot(fig, filename='m')













