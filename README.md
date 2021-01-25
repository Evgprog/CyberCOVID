 #CyberCovid
 ##Project's aims: 
 To allow localizaton of quarantine policy measures due to early identification of covid spread
 Currently a more binary policy is being used where all or no cities are quarantied
 the measures for infectios deseace prevention were used on the number o admitted patients
 risk analysis is done on overall number of patients which were identified
 and earlier detection based on the  prediction of possible number off patients might allow a more proactive measure to take place
 The structure of analysis :
 Getting data regarding number of patients by city
 Normalizing data, fixing mistakes
 Creating predictions for spreading rate per city
 Using formula identified in the article x35
  The code performs predictions of potential spread of covid 19 in Israil's cities
  The codes's structure consist of the following parts:
1. Data upload from a website that contains a history of patients dinamycs  per city
2. Data  insertion into a pandas dataframework
3. Cleaning and prepearing of dataframe for analysis
4. Creating several models and classes for linear regression analysis and predictions
5. Creating a trashold for data set on 08 score
6. Applying models for each city dataset

