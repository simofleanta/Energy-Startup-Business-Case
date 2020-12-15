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
opp=pd.read_csv('staff.csv')
print(opp.columns)
df=DataFrame(opp.head(800))
print(df.head(5))

#print(df.to_markdown())

s=pd.read_csv('energy_startup.csv')
print(s.columns)
df=DataFrame(s.head(800))
print(df.head(700))

#unique client region
unique_region=df.Client_Region.unique()

#what were top sales revenue generating products? top room household and region
#geeration by revenue generation

toprev=df.groupby(['Client_Room_household','Client_Region']).sum().round(2).sort_values(['Sales_rev'], ascending=False)
print(toprev.head(10))





