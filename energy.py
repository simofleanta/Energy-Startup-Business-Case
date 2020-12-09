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

energy=pd.read_csv('energy.csv')
print(energy.columns)
df=DataFrame(energy.head(500))
print(df.head(500))

energy_s=pd.read_csv('energy_startup.csv')
print(energy_s.columns)
df=DataFrame(energy_s.head(500))
print(df.head(500))