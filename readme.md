
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








# Energy plots

<img width="188" alt="agg kwh" src="https://user-images.githubusercontent.com/47668423/102016513-bacc3800-3d61-11eb-87df-ca8f521a2912.png">


![Figure_3](https://user-images.githubusercontent.com/47668423/102016515-bdc72880-3d61-11eb-8ced-449996cfa0f6.png)

![Figure_4](https://user-images.githubusercontent.com/47668423/102016516-be5fbf00-3d61-11eb-870f-c339c2d5436b.png)

![Figure_5](https://user-images.githubusercontent.com/47668423/102016517-be5fbf00-3d61-11eb-8ade-507b9965b296.png)

![Figure_6](https://user-images.githubusercontent.com/47668423/102016519-bef85580-3d61-11eb-86bd-c0b30cc38b21.png)

![Figure_7](https://user-images.githubusercontent.com/47668423/102016521-bef85580-3d61-11eb-801c-f73fdd7f5091.png)

![Figure_8](https://user-images.githubusercontent.com/47668423/102016522-bf90ec00-3d61-11eb-9583-fbb6a46328f2.png)

![Figure_9](https://user-images.githubusercontent.com/47668423/102016523-bf90ec00-3d61-11eb-9b1d-cbbd01fcb50e.png)

![Figure_10](https://user-images.githubusercontent.com/47668423/102016524-c0298280-3d61-11eb-8b4a-5aca18a35153.png)

![Figure_11](https://user-images.githubusercontent.com/47668423/102016525-c0298280-3d61-11eb-8f01-540483c5e2a8.png)

<img width="175" alt="kwh season" src="https://user-images.githubusercontent.com/47668423/102016526-c0c21900-3d61-11eb-8e73-89b9a8d0e1c5.png">

<img width="255" alt="max en" src="https://user-images.githubusercontent.com/47668423/102016527-c0c21900-3d61-11eb-960a-baaf7cf0eb95.png">



<img width="496" alt="room 4 kw dec" src="https://user-images.githubusercontent.com/47668423/102016529-c15aaf80-3d61-11eb-88b5-02f906cc24d5.png">

<img width="146" alt="weekday kwh" src="https://user-images.githubusercontent.com/47668423/102016531-c1f34600-3d61-11eb-9d22-8236424fd5c6.png">

![sales_kwh](https://user-images.githubusercontent.com/47668423/102016638-3201cc00-3d62-11eb-8317-03d12b2127f4.png)

![Sales_room distribution](https://user-images.githubusercontent.com/47668423/102016639-329a6280-3d62-11eb-9a59-10e6ef103f80.png)


# Part II

# Business Analysis plots

<img width="799" alt="app performance in Groningen" src="https://user-images.githubusercontent.com/47668423/102016569-e9e2a980-3d61-11eb-82c4-facb6cc4bbc8.png">
<img width="932" alt="fig 8" src="https://user-images.githubusercontent.com/47668423/102016573-eb13d680-3d61-11eb-8bc8-4988b2b5e20f.png">

![Figure_1](https://user-images.githubusercontent.com/47668423/102016575-ebac6d00-3d61-11eb-85b0-6134189d2a18.png)

![Figure_2](https://user-images.githubusercontent.com/47668423/102016577-ebac6d00-3d61-11eb-81b1-1eb60f14e9ea.png)


![Figure_3](https://user-images.githubusercontent.com/47668423/102016578-ec450380-3d61-11eb-874b-aded0fb2c977.png)

![Figure_4](https://user-images.githubusercontent.com/47668423/102016579-ec450380-3d61-11eb-8162-5370b76860e8.png)

![Figure_5](https://user-images.githubusercontent.com/47668423/102016580-ecdd9a00-3d61-11eb-9b92-6503183c8f2a.png)

![Figure_6](https://user-images.githubusercontent.com/47668423/102016581-ecdd9a00-3d61-11eb-96ce-9aea21ae40ad.png)

![Figure_7](https://user-images.githubusercontent.com/47668423/102016583-ed763080-3d61-11eb-835c-823fa21022e5.png)

<img width="663" alt="Jan scores" src="https://user-images.githubusercontent.com/47668423/102016584-ed763080-3d61-11eb-87d1-1ee433b42fdc.png">

<img width="504" alt="merge season" src="https://user-images.githubusercontent.com/47668423/102016585-ee0ec700-3d61-11eb-9427-5b0db77bb203.png">

<img width="668" alt="roi_profit" src="https://user-images.githubusercontent.com/47668423/102016587-eea75d80-3d61-11eb-8d09-dc39919991bc.png">

<img width="798" alt="s rev countries" src="https://user-images.githubusercontent.com/47668423/102016588-eea75d80-3d61-11eb-9280-1acd13551b02.png">

<img width="279" alt="s rev in month rest of mths" src="https://user-images.githubusercontent.com/47668423/102016589-ef3ff400-3d61-11eb-8c91-e47aeb113ff0.png">

<img width="274" alt="s rev in mth" src="https://user-images.githubusercontent.com/47668423/102016590-ef3ff400-3d61-11eb-8742-5790012de47a.png">

<img width="767" alt="s rev in weekday in generl" src="https://user-images.githubusercontent.com/47668423/102016591-ef3ff400-3d61-11eb-8f87-da141438dc04.png">

<img width="798" alt="sale rev in countries" src="https://user-images.githubusercontent.com/47668423/102016592-efd88a80-3d61-11eb-874f-1fd43a4500b1.png">

<img width="790" alt="winter app" src="https://user-images.githubusercontent.com/47668423/102016593-f0712100-3d61-11eb-8b72-ffa319a8954e.png">

# Merged Business and Energy Analysis 


![dots distribution](https://user-images.githubusercontent.com/47668423/102016630-2f9f7200-3d62-11eb-9567-e0395f789bdc.png)

![Figure_1](https://user-images.githubusercontent.com/47668423/102016632-30d09f00-3d62-11eb-9748-d5b40b69cf6f.png)

![Figure_2](https://user-images.githubusercontent.com/47668423/102016633-31693580-3d62-11eb-859b-f656920a54aa.png)

![Figure_5](https://user-images.githubusercontent.com/47668423/102016635-31693580-3d62-11eb-87bd-7337aebe32d2.png)

![prof_kwh](https://user-images.githubusercontent.com/47668423/102016636-3201cc00-3d62-11eb-8a9d-a6c68aa0039c.png)

# Part III - soon 
-code beautify
-add thir part
-add info for 
-regplot
-decisions

 


