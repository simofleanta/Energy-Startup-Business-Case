
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


#open file the energy file
energy=pd.read_csv('energy.csv')
print(energy.columns)
df=DataFrame(energy.head(500))
print(df.head(500))

startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
sdf=DataFrame(startup.head(700))
print(sdf.head(700))

#December=df[df.Month=='Dec']
#plt.scatter(df.Kwh, df.Active_kwh_month)
#interest=sales_rev and kwh


#taking info from both datasets into one df. #merge 

startup_df=sdf[['Year','Month','Sales_rev','Season','Month_Profit','Client_Region','Client_Room_household']].copy()
endf=df[['Year','Month','Active_kwh_month','Kwh']].copy()
z_merge=pd.merge(startup_df,endf)
print(z_merge)


#x=sns.relplot('Sales_rev','Month_Profit',data=z_merge,hue='Season', size='Year')
#plt.show()

December=z_merge[z_merge.Month=='Dec']
sp=sns.stripplot(December.Sales_rev, December.Client_Region)
plt.show()











