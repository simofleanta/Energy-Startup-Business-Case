
#We are dealing with a startup that is working on an electric energy monitoring app for households and in the future for businesses 
# This is an electric energy consumption analysis for threee regions, Berlin, GronIngen and Amsterdam.  
#the data is taken from an people living in dofferent households, that are using this app 
#we are interested to understand the Kwt consumption behaviour not only in different regions but aso in different households, for years 2018-2019
#Anlyzing the Kwt behaviour accross the units, regions and its seasonality, may help us better understand how we waste energy or we save energy and therefore 
#optimize costs and even be more evironmentally conscous. 

#the analysis wil take part in two stages
#-part I - Active Kwt behaviour 
#-part II - economic startup context 


"""Part I"""

#we did:
#eda
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

#Business ASPECT

#open file the energy file
startup=pd.read_csv('energy.csv')
print(startup.columns)
df=DataFrame(startup.head(300))
print(df.head(300))


