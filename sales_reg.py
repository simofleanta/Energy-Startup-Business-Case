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

c=pd.read_csv('sales_kwh.csv')
print(c.columns)
salesdf=DataFrame(c.head(700))
print(salesdf)


df = px.data.tips()
fig = px.scatter(salesdf, x="Sales_rev", y="Active_kwh_month", trendline="ols")
plotly.offline.plot(fig, filename='m')


