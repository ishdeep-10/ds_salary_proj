# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 00:24:51 2021

@author: acer
"""
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])

minus_K = salary.apply(lambda x: x.replace('K','').replace('$',''))

minus_hr = minus_K.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))


df['avg_salary'] = (df['min_salary'] + df['max_salary'] ) / 2

# company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3] , axis=1)


# state field 

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()



df.columns
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0,axis=1)

# age of company
df['age'] = df.Founded.apply(lambda x: x if x<0 else 2021-x)

# parsing of job description
#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()
#r studio
df['rstudio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
# spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)


df.drop('Unnamed: 0',axis=1,inplace=True)






