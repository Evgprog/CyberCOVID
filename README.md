 # CyberCovid

 ## Project's aims: 
 
 Short Description 
 
 

Current project demonstrates an ability to perform data download, cleaning, choosing machine learning model and its application in real life situation.
In the following case data based on Covid 19 spread in Israeli cities is utilized in order to perform a prediction of its spread in the future n different cities
After checking several approaches a logistic regression model was chosen since it was a more fit to follow the data which represented in the cases as a linear growth
In the following analysis two models of data representation were used:
-	An internal representation of four cities with the highest model score of patient’s prediction. The branch called “master” showing four cities as an example. In this case prediction model was use for every city and a threshold of 0.8 was used for filtering the data  
-	Display of a specific city prediction upon the selection of a user. Only specific city will be chosen and then displayed via “Dash” application, based upon local host


(https://user-images.githubusercontent.com/74383608/107421801-14af6b00-6b23-11eb-9fe4-d5061293034f.PNG)





 The structure of analysis :
 The structure of analysis :
 
 # Project's aims:
# Prediction of COVID 19 patients number in Israeli cities.
# DATA SOURCE:
# The data set taken from Israeli Health ministry and was uploaded from :
# https://raw.githubusercontent.com/idandrd/israel-covid19-data/master/CityData.csv
# Project's value:
# Early identification potential of Covid 19 spread in certain Israeli city.
# Earlier detection should allow a more proactive measures to take place in order to stop the spread of Covid 19
Branch A (master) 
1. Data upload from a website that contains a history of patient’s dynamics per city
2. Data insertion into a panda’s dataframework
3. Cleaning and preparing of dataframe for analysis
4. Creating several models and classes for linear regression analysis and predictions
5. Creating a Threshhold for data set on 08 score
6. Applying models for each city dataset


Branch B (with dash)

# Code structure:
# 1. Getting data regarding number of patients by city from github dataset
# 2. Normalizing data, fixing mistakes
# 3. Creating functions for dash, models for dates, regression analysis
# 4. Creating predictions for spreading rate per city
# 5. Display the prediction spread by city chosen by user






