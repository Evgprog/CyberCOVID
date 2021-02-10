 # CyberCovid(Master)
 
Current project demonstrates an ability to perform data download, cleaning, choosing machine learning model and its application in real life situation.
In the following case data based on Covid 19 spread in Israeli cities is utilized in order to perform a prediction of its spread in the future n different cities
After checking several approaches a logistic regression model was chosen since it was a more fit to follow the data which represented in the cases as a linear growth
In the following analysis two models of data representation were used:
1) "Master" Branch - An internal representation of four cities with the highest model score of patient’s prediction. The branch called “master” showing four cities as an example. In this case prediction model was use for every city and a threshold of 0.8 was used for filtering the data  
2) "Dash" Branch - Display of a specific city prediction upon the selection of a user. Only specific city will be chosen and then displayed via “Dash” application, based upon local host

 ![Covid19git](https://user-images.githubusercontent.com/74383608/106588428-708e5880-6553-11eb-8bf9-462a42890218.png)
 
 The structure of analysis :
  
Branch A (master) 

1. Data upload from a website that contains a history of patient’s dynamics per city
2. Data insertion into a panda’s Dataframework
3. Cleaning and preparing of Dataframework for analysis
4. Creating several models and classes for linear regression analysis and predictions
5. Creating a Threshold for data set on 08 score
6. Applying models for each city Dataset

Branch B (with dash)

# Code structure:
# 1. Getting data regarding number of patients by city from github dataset
# 2. Normalizing data, fixing mistakes
# 3. Creating functions for dash, models for dates, regression analysis
# 4. Creating predictions for spreading rate per city
# 5. Display the prediction spread by city chosen by user


