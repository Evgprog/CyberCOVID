 # CyberCovid (Branch "Dash")

 ## Project's aims: 
 
Short Description:
 
This project demonstrates an ability to build a prediction model based upon data downloading, cleaning and choosing a machine learning model and its application in real life situation.
In the following case, data based on Covid -19 spread in Israeli cities is utilized in order to create a prediction model that could foresee its spread in the different cities.
 After checking several approaches a linear regression model was chosen since it was more appropriate, because the data represented in this case showed a linear growth.
As the result the following analysis two models of data representation were used: 
- {Master} A prediction model based upon linear regression analysis was used for each city. After performing regression analysis, a score of 8.0 was chosen as threshold. Based on matplotlib four cities with the highest model score were chosen. The branch called “master” shows four cities as an example.
- {Dash} Allows display of a specific city prediction selected from the combo-box y the user.  Consequently, only the specific city will be selected and then displayed in the local browser via “Dash” based application, upon local host



The following picture represents an example of prediction based on data of Jerusalem:

![Cappture2](https://user-images.githubusercontent.com/74383608/107421801-14af6b00-6b23-11eb-9fe4-d5061293034f.PNG)

The structure of analysis :
 
Branch B (with dash)

 ## Code structure:
 1. Getting data regarding number of patients by city from github dataset
 2. Normalizing data, fixing mistakes
 3. Creating functions for dash, models for dates, regression analysis
 4. Creating predictions for spreading rate per city
 5. Display the prediction spread by city chosen by the  user






