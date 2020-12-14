
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
opp=pd.read_csv('Staff.csv')
print(opp.columns)
df=DataFrame(opp.head(800))
print(df.head(800))


#where is the money mostly spent?

opperational=df
df = px.data.tips()
fig = px.pie(opperational, values='Monthly_costs', names='General_Expenditures', color_discrete_sequence=px.colors.sequential.RdBu)
plotly.offline.plot(fig, filename='kwt')

#1.staff
#2.Marketing 
#R&D

#Who is best paid?

#open file the energy file
opp=pd.read_csv('Emps.csv')
print(opp.columns)
df=DataFrame(opp.head(800))
#print(df.head(800))

p=df
df= px.data.tips()
figure=px.pie(p, values='Employee_cost', names='Employees', color_discrete_sequence=px.colors.sequential.RdBu)
#plotly.offline.plot(figure, filename='em')

#Soft_eng
#Lawyers
#BI








