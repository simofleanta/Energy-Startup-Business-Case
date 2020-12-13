#PART I+ PARTII =...

#add energy data and merge with x 

energy=pd.read_csv('energy.csv')
#print(energy.columns)
df=DataFrame(energy.head(500))
#print(df.head(500))

#Make copies of dfs to make easier to read it in a table
x=energy_df[['Year','Month','Profitablity','ROI_2019','ROI_2018','Client_Room_household','Sales_rev']].copy()
y=df[['Year','Month','kwh','Region']].copy()

#merge x+y 
z=pd.merge(x,y)
print(z)

#perform correlations between business analysis and energy 
plt.figure(figsize=(10,10))
plt.title('Sales_rev- Client_Room_household', y=1.05, size=15)
sns.heatmap(z.corr(),linewidths=0.1,vmax=1.0, square=True, 
            cmap='CMRmap', linecolor='white', annot=True)
plt.show()

#quiet many corrs:
#profitability of the app with client house hold, profitability, sales_rev, roi but not with active kwt
#active kwt with client room household and roi but, not with sales 
#sales_rev with client room house, profitability,roi but not with kwt
#roi with profitability and sales 
#client room household with kwt, sales and profitability and roi but not with 

#pairplots for correlation understanding

pairplot = sns.pairplot(z, vars=['Client_Room_household','kwh'])
plt.show()
#the higher the number of rooms a client has , the more energy consumes.

#=> a stronger profitability of the app
pairplot = sns.pairplot(z, vars=['Profitablity','Client_Room_household'])
plt.show()

pairplot = sns.pairplot(z, vars=['Profitablity','Client_Room_household'])
plt.show()

#the app should make client understand not only how much kwt are active during evening or end of the week
# /month, but also how much energy they could save. 
# figure out a for that calculation now that the data was merged into z df. that is an a separate section



