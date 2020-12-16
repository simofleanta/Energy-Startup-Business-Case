
# Startup "Light bulb Energy" 
#We are dealing with a startup that is working on an light bulb electric energy monitoring app for households and in the future for businesses. 
This is an electric energy consumption analysis is present in more regions, Berlin, Groningen and Amsterdam Aarhurs  
#the data is taken from an people living in different households, that are using this app 
#we are interested to understand their Kwt consumption behaviour not only in different regions but aso in different households, for years 2018-2019
so we can help them take better decisions in their wish to optimize electri consumption. 
#Anlyzing the Kwt behaviour accross the units, regions and its seasonality, may help us better understand how they waste energy or save energy and therefore optimize costs and even be more evironmentally conscous.

# How we dealth with the data   
#formula to estimate consumption is number of lightbulbs of normally 60 W in the unit
#then the result multiplied by number of hours it is switched on 
#then divide by 1000. 0.50 euro per h. 
#=> rooms 5 - 9(will consider more since there'll be other applicences) just to make it easier to estimate 
#=> rooms 4 - 8
#=> rooms 3 - 7 -7*60w (each lighting applience)
#=> rooms 2 - 6
#=> rooms 1 - 5

# Consumption Analysis
#ex formula for 5 rooms to find out kwt hhours used for 9 60 watt bulbs kwh
#watts= 60*9=540 W
#kwh= 540 * 6h:1000
#kwh=3240 :1000
#kwh=3,24
#To find the monthly energy usage, multiply the result by 30.
#monthly kWh = 3.24 kWh × 30
#monthly kWh = 97.2 kWh

# KwH cost calculation
#price = kWh × cost per kWh
#price = 97.2 kWh × .50
#kWh = 48.6

# The analysis wil take part in three stages
#-part I - Active Kwt behaviour 
#-part II - economic startup context 
#-part III - Costs and investment analysis coming soon. 


# Part I - electric energy behaviour 


![dist](https://user-images.githubusercontent.com/47668423/102016514-bd2e9200-3d61-11eb-82a8-4769a9ea3bac.png)

Figure 1. showing Active Kwh per month distributed across the four seasons for 1-5 room households. 

#The graph shows that Active Kwh per month increases along with the number of rooms in households, and it becomes higher for autumn and winter seasons. 



![Month](https://user-images.githubusercontent.com/47668423/102016528-c15aaf80-3d61-11eb-90be-c3579faf2ab6.png)

Figure 2. showing KwH distributed across months for 2018 and 2019. 

#Since electric energy onsumption increases in autumn and winter, in this graphs can be observed that winter months are more active than the summer ones,
up to April, we consider the months to be winter months since the day is still short. The graphs shows that 2019 was mor active than 2018 in terms of electric energy consumption. 


![Figure_1](https://user-images.githubusercontent.com/47668423/102064320-725f5980-3df7-11eb-9b7f-32f0a26f4988.png)

Figure 3. showing active Kwh behaviour during the da in December. 

#Light bulb electric energy consumption increases most during Midday, which shows tht arround 15:40 or earlier it gets darker.
#People are determined to switch lights on more often.


![fixed corr](https://user-images.githubusercontent.com/47668423/102065176-8192d700-3df8-11eb-9b27-ca79a70d9fb8.png)

Figure 4. showing electric energy consumption correlations 

The correlations are not so strong however they are to be considered when taking decisions. 
There is a correlations between Room household and Actve Kwh per month - 1 which confirms that the larger the number of rooms the higher the consumption.
The same correlation could be found between Kwh and Room Household. 


![Client](https://user-images.githubusercontent.com/47668423/102069460-1ba94e00-3dfe-11eb-96ef-21d97ee0cb20.png)

Figure 5. showing energy consumption in 1-5 rooms households, across different client regions. 

Came out that Luxembourg and Hgue have most 5 room household than other regions. Therefore consumption will be highest in Luxembourg in Hague. 
The lowes consumption are Berlin and Groningen. 


![client year](https://user-images.githubusercontent.com/47668423/102069934-b7d35500-3dfe-11eb-8dea-c7f0204523fa.png)

Figure 6. Showing Kwh distribution across regions in both years.

This shows that 2019 was most active in terms of consumption but Hague and Luxembourg consumes most in 2018 compared to other regions that are very active in 2019.



# Part II

# Business Analysis plots


![Money](https://user-images.githubusercontent.com/47668423/102071967-8019dc80-3e01-11eb-8396-04f5723b7aed.png)


Fig 1. showing where the sales revenue increase from. 

Sales Revenue increase from Luxembourg and Hague; where the consumption is higher and number of rooms is 4-5. 


![Lux](https://user-images.githubusercontent.com/47668423/102073155-2e725180-3e03-11eb-8126-23bd093dd3f0.png)

Figure 2. showing sales revenue benchamrk across regions. 

Luxembourg had a higher sale revenue in 2018, over 40000 but in 2019, Berlin over passes Luxembourg with over 40000. In 2019 Groningen reached a sale revenue of 60000 euro. 

![Figure_7](https://user-images.githubusercontent.com/47668423/102016583-ed763080-3d61-11eb-835c-823fa21022e5.png)

Figure 3. showing correlations between sales revenue and room households. 

There is  a weak but significant correlation between sales revenue and room household. 
Also there is a correlation between return of investment and rooms.


![sales_kwh](https://user-images.githubusercontent.com/47668423/102016638-3201cc00-3d62-11eb-8317-03d12b2127f4.png)

Figure 4. showing the relationship between sales revenue and KwH per month consumption. 

This shows that there is a around 80 KwH per month consumptin at a over 45000 euro sales revenue. 
For over 90 KwH per month consumption sales revenue. may reach over 50000 euro. 

![Room per year](https://user-images.githubusercontent.com/47668423/102076333-dab63700-3e07-11eb-8582-ceac655bc9c9.png)

Fig 5. showing revenues distributed across rooms household.

It is clear that revenue increases with consumtion and household room nuber.
In this figure 5 room households bring over 60000 sales revenue. And therefore a higher profitability too. 


![sum](https://user-images.githubusercontent.com/47668423/102079077-4dc1ac80-3e0c-11eb-81bf-04822334739c.png)

Figure 6. showing sum of sales_revenues across months and the room household distribution. 

3 room households bring more sales revenue and in autumn months. 

![Mean](https://user-images.githubusercontent.com/47668423/102079310-bf99f600-3e0c-11eb-8e73-d998088051df.png)

Figure 7. showing mean of sales_revenues across weekdays and the room household distribution. 

Beginning of the week seems more profitable. 


![Winter_M](https://user-images.githubusercontent.com/47668423/102080399-a98d3500-3e0e-11eb-9ff7-adb52c4e2264.png)

Figure 8. showing mean of sales_revenues across months and the room household distribution. 

February and January are most profitable. 



# Part III - Operational Costs
#Where the money is mostly invested on?

<img width="807" alt="operational costs" src="https://user-images.githubusercontent.com/47668423/102113314-2e8d4400-3e39-11eb-861b-bffba0301ff9.png">

#1.staff
#2.Marketing 
#R&D


#Who is best paid in the startup?

<img width="779" alt="employees" src="https://user-images.githubusercontent.com/47668423/102113585-7f9d3800-3e39-11eb-9137-8e423cdfb793.png">

|     |   Year | Month   | Employees          |   Employee_cost |
|----:|-------:|:--------|:-------------------|----------------:|
|   0 |   2019 | Jan     | Soft_engineer      |            5000 |
|   1 |   2019 | Jan     | BI_Analyst         |            4300 |
|   2 |   2019 | Jan     | Accountant         |            1600 |
|   3 |   2019 | Jan     | CEO                |            3000 |
|   4 |   2019 | Jan     | Business_developer |            2700 |

#Soft_eng
#Lawyers
#BI

# Top sales revenue generated; top selling country

<img width="788" alt="Focus on Hague" src="https://user-images.githubusercontent.com/47668423/102235742-f1858800-3ef2-11eb-9de7-d05f581fb3b0.png">

Figure 1. Showing top 10 sales by country

Focus app sales on Hague and 4 and five room units 



|   Client_Region   | Number_clients | Costs | Sales_rev | 
|:------------------|:-------------- |:------|:--------- |
| (4, 'Hague')      | 1800           |351850 |  973000   |   
| (1, 'Aarhus')     | 1811           |363300 |  905500   |
| (2, 'Luxembourg') | 1770           |371550 |  885000   |       
| (3, 'Berlin')     | 1714           |385400 |  857000   |
| (5, 'Groningen')  |  83            |22450  |  41500    | 


# Conclusions 

The app is supposed enable clients better monitor their light electric energy consumption and therefore optimize household costs. 
It came out that sales revenues of the startup rise from people with 5 room who therefore are more likely to consume more electricity. This shows a need of people to optimize their high costs. 
Electric cnsumption increases along with the season and months, suggesting that days shorten whch shows a need to switch on lights, more ofter. According to the 
Household rooms, there are a numner of lightbulbs which determine a  specfic energy consumption behaviour. 
The correlations between household rooms and electric consumption and between profitability and consumption although weak, they are worth looking at and acte upon:
Also the money goes mostly into Staff marketing, and R&D, this shows the development of the business.
Software engineer is best paid, along with BI. this shows a potential development and innovation in the electric energy.

# General Suggestions

focus sales in regions having more room households
focus sales during autumn and winter because this is when people need to optimize energy costs. 
In order to optimize costs, it ok to recommend a specific light bulb for larger households.
The graphs show lower sales scores in 2018 compared to 2019, this sugggest that the use of app increase in 2019 by people having larger households. Although 5 rooms were not 
so many units but the consumption and need was high enough to compensate the previous year. 
As a startup it could be a beehive for graduates that could bring new ideas to the de development of the startup and bring new investment opportunities. 


# Product design sugesstions 
It may be possible to desigh a light bulb, linked to the app that allows clients using the app, to better focus on saving energy. 
Design a device that automates 
lights withches on and off according to the day's lighting midday dark or smth. 





 






