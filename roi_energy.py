
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

#2019 ROI
#filtering the year

startup=pd.read_csv('energy_startup.csv')
print(startup.columns)
df=DataFrame(startup.head(700))
print(df.head(700))

year2019=df[df.Year==2019]
print(year2019)