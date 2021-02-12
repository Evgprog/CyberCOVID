 #  CyberCovid (Branch "Dash")
 ##  Disclaimer
  This project consists of two independent branches named " Dash " and " Master ". 
  See the section bellow for the description of each one of them.   
 ## Project's aims
 
 ###  Short Description
   
This project demonstrates an ability to build a prediction model based upon data downloading, cleaning and choosing a machine learning model and its application in real life situation.
In the following case, data based on Covid -19 spread in Israeli cities is utilized in order to create a prediction model that could foresee its spread in the different cities.
After checking several approaches a linear regression model was chosen since it was more appropriate, because the data represented in this case showed a linear growth.
While maintaining the same regression model for calculation purposes the visualization layer was separated in two branches "Master" and "Dash" .
The "Master" branch uses matplotlib library and the "Dash" uses plotly and enables the display of the results as an HTML page(currently only local host is supported) 


- {Master}     Shows four cities with the highest spread disease level based on prediction model. 
               The model applies a linear regression analysis and matplotlib library for the visualization.
               After performing regression analysis for each city, a score of 0.8 was chosen as threshold. 
               Consequently, four cities with the highest score are displayed in one picture


           
- {Dash}       Allows a display of the specific city prediction selected from the combo-box y the user. A combo box is filled with cities names 
               Consequently, only specific city will be selected and then displayed in the local browser via “Dash” based application, upon local host



The following picture represents an example of prediction model based on data of Jerusalem:

![Cappture2](https://user-images.githubusercontent.com/74383608/107421801-14af6b00-6b23-11eb-9fe4-d5061293034f.PNG)



 ## Code structure:
 
 1. Getting the data from public dataset concerning patients number per city (link : https://raw.githubusercontent.com/idandrd/israel-covid19-data/master/CityData.csv)
 2. Cleaning data, fixing mistakes
 3. Prepearing the dash model for data display 
 4. Upon selection of the city name it's calculation results are shown as an HTML page 




