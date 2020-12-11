
# Startup "Light bulb Energy" 
#We are dealing with a startup that is working on an electric energy monitoring app for households and in the future for businesses. 
This is an electric energy consumption analysis for threee regions, Berlin, GronIngen and Amsterdam.  
#the data is taken from an people living in dofferent households, that are using this app 
#we are interested to understand the Kwt consumption behaviour not only in different regions but aso in different households, for years 2018-2019
#Anlyzing the Kwt behaviour accross the units, regions and its seasonality, may help us better understand how we waste energy or we save energy and therefore optimize costs and even be more evironmentally conscous. 

#The analysis wil take part in two stages
#-part I - Active Kwt behaviour 
#-part II - economic startup context 


#formula to estimate consumption is number of lightbulbs of normally 60 W in the unit
#then the result multiplied by number of hours it is switched on 
#then divide by 1000. 0.50 euro per h. 
#=> rooms 5 - 9(will consider more since there'll be other applicences) just to make it easier to estimate 
#=> rooms 4 - 8
#=> rooms 3 - 7 -7*60w (each lighting applience)
#=> rooms 2 - 6
#=> rooms 1 - 5

#CONSUMPTION ANALYSIS MADE ON THE DATABASE
#ex formula for 5 rooms to find out kwt hhours used for 9 60 watt bulbs kwh
#watts= 60*9=540 W
#kwh= 540 * 6h:1000
#kwh=3240 :1000
#kwh=3,24
#To find the monthly energy usage, multiply the result by 30.
#monthly kWh = 3.24 kWh × 30
#monthly kWh = 97.2 kWh

#--------------------------------COST CALCULATIONS
#price = kWh × cost per kWh
#price = 97.2 kWh × .50
#kWh = 48.6
