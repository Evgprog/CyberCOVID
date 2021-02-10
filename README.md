 # CyberCovid(Master)
 
 Short Description:
 
This project demonstrates an ability to build a prediction model based upon data downloading, cleaning and choosing a machine learning model and its application in real life situation.
In the following case, data based on Covid -19 spread in Israeli cities is utilized in order to create a prediction model that could foresee its spread in the different cities.
 After checking several approaches a linear regression model was chosen since it was more appropriate, because the data represented in this case showed a linear growth.
As the result the following analysis two models of data representation were used: 
- {Master} A prediction model based upon linear regression analysis was used for each city. After performing regression analysis, a score of 8.0 was chosen as threshold. Based on matplotlib four cities with the highest model score were chosen. The branch called “master” shows four cities as an example.
-  {Dash} Allows display of a specific city prediction selected from the combo-box y the user.  Consequently, only the specific city will be selected and then displayed in the local browser via “Dash” based application, upon local host


The following picture represents the case of four cities with the highest score rate  

 ![Covid19git](https://user-images.githubusercontent.com/74383608/106588428-708e5880-6553-11eb-8bf9-462a42890218.png)
 
 The structure of analysis :
  
Branch A (master) 
1. Data upload from a website that contains a history of patient’s dynamics per city
2. Data insertion into a panda’s dataframework
3. Cleaning and preparing of dataframe for analysis
4. Creating several models and classes for linear regression analysis and predictions
5. Creating a threshold for data set on 08 score
6. Applying models for each city dataset



