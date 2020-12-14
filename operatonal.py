
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
#analyzed the business
#using corrs we built on the analysis
#merged in a separate section, the business analysis and the energy consumption to understand the trends 


#open file the energy file
startup=pd.read_csv('Staff.csv')
print(startup.columns)
df=DataFrame(startup.head(700))
print(df.head(700))