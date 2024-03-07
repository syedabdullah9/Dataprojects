#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
from datetime import datetime, timedelta
input_file = "input.csv"
df = pd.read_csv(input_file)

def transform_data(df):
    transformed_data = []

    for index, row in df.iterrows():
        employee_code = row['Employee Code']
        manager_employee_code = row['Manager Employee Code']
        compensation_1 = row['Compensation 1']
        compensation_2 = row['Compensation 2']
        compensation_1_date = datetime.strptime(row['Compensation 1 date'], '%Y-%m-%d') if pd.notnull(row['Compensation 1 date']) else None
        compensation_2_date = datetime.strptime(row['Compensation 2 date'], '%Y-%m-%d') if pd.notnull(row['Compensation 2 date']) else None

        review_1 = row['Review 1']
        review_2 = row['Review 2']
        review_1_date = datetime.strptime(row['Review 1 date'], '%Y-%m-%d') if pd.notnull(row['Review 1 date']) else None
        review_2_date = datetime.strptime(row['Review 2 date'], '%Y-%m-%d') if pd.notnull(row['Review 2 date']) else None
        
        engagement_1 = row['Engagement 1']
        engagement_2 = row['Engagement 2']
        engagement_1_date = datetime.strptime(row['Engagement 1 date'], '%Y-%m-%d') if pd.notnull(row['Engagement 1 date']) else None
        engagement_2_date = datetime.strptime(row['Engagement 2 date'], '%Y-%m-%d') if pd.notnull(row['Engagement 2 date']) else None
        
        date_of_joining = datetime.strptime(row['Date of Joining'], '%Y-%m-%d')
        date_of_exit = datetime.strptime(row['Date of Exit'], '%Y-%m-%d') if pd.notnull(row['Date of Exit']) else datetime.now()
        
        periods = [(date_of_joining, date_of_exit), (compensation_1_date, compensation_2_date), 
                   (review_1_date, review_2_date), (engagement_1_date, engagement_2_date)]
        
        for i in range(len(periods) - 1):
            start_date, end_date = periods[i]
            next_start_date, next_end_date = periods[i + 1]
            
            if start_date is None:
                continue
            
            end_date = next_start_date - timedelta(days=1) if next_start_date else datetime(2100, 1, 1)
            
            last_compensation = compensation_1 if i == 0 else compensation_2
            compensation = compensation_1 if i == 0 else compensation_2
            last_pay_raise_date = date_of_joining if i == 0 else compensation_1_date
            performance_rating = review_1 if i == 0 else review_2
            engagement_score = engagement_1 if i == 0 else engagement_2
            
            transformed_data.append([employee_code, manager_employee_code, last_compensation, compensation, last_pay_raise_date, None, None, performance_rating, engagement_score, start_date, end_date])
        
        last_period_end_date = periods[-1][1]
        last_compensation = compensation_2
        last_pay_raise_date = compensation_2_date
        performance_rating = review_2
        engagement_score = engagement_2
        
        transformed_data.append([employee_code, manager_employee_code, last_compensation, None, last_pay_raise_date, None, None, performance_rating, engagement_score, last_period_end_date, datetime(2100, 1, 1)])
    
    return transformed_data


transformed_data = transform_data(df)


output_df = pd.DataFrame(transformed_data, columns=['Employee Code', 'Manager Employee Code', 'Last Compensation', 'Compensation', 'Last Pay Raise Date', 'Variable Pay', 'Tenure in Org', 'Performance Rating', 'Engagement Score', 'Effective Date', 'End Date'])

output_file = "output.csv"
output_df.to_csv(output_file, index=False)


# In[16]:


output_df 


# In[3]:





# In[4]:





# In[5]:





# In[6]:





# In[7]:





# In[8]:





# In[ ]:





# In[ ]:




