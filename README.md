
# Data Science Salary Estimator: Project Overview
   1. Created a tool that estimates data science salaries  to help data scientists negotiate their income when they get a job.<br>
2 . Scraped over 1000 job descriptions from glassdoor using python and selenium. <br>
3 . Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.<br>
4 . Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.<br>
5 . Built a client facing API using flask.<br>

## Code and Resources
Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle <br>
For Web Framework Requirements: pip install -r requirements.txt <br>
Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium <br>
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 <br>
Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2 <br>

## Web Scraping

We scraped the data from glassdoor using our selenium scraper for the job postings of "Data Scientist" in the United States.
Following features were extracted from the web : 
1. Job title <br>
2. Salary Estimate <br>
3. Job Description <br>
4. Rating <br>
5. Company <br>
6. Location <br>
7. Company Headquarters <br>
8. Company Size <br>
9. Company Founded Date <br>
10. Type of Ownership <br>
11. Industry <br>
12. Sector <br>
13. Revenue <br>
14. Competitors <br>

## Data Cleaning , EDA and Feature Engineering
The following steps were taken for cleaning our data and making it ready for model building.
### Data Cleaning : 
1. Removed rows without salary
2. Parsed numeric data out of salary
3. Added a column for if the job was at the company’s headquarters
4. Made columns for if different skills were listed in the job description

### EDA 
Looked into distributions for the numerical columns and made bar charts/pivot tables to understand the categorical data too. Also made a correlation plot to check the dependency between our columns.



### Feature Engineering
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

## Model Building and Performance
I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

1.Multiple Linear Regression – Baseline for the model<br>
2.Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.<br>
3.Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.<br>

### Performance :
The Random Forest model far outperformed the other approaches on the test and validation sets.
1. Random Forest : MAE = 11.06
2. Linear Regression : MAE = 18.85
3. Lasso Regression : MAE = 19.66

## Model Production
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

