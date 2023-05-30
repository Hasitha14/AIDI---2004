#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pds,  numpy as np , seaborn as sns, ipywidgets
from scipy.stats import t, ttest_ind



flight_csv = pds.read_csv('flights.csv')

flight_csv.head()


# In[89]:





# In[89]:





# In[89]:





# In[90]:


#task 1 - present analysis and perform EDA on flights.csv


# In[91]:



print("no of rows and coloumn old",flight_csv.shape )
# Data cleaning

new_flight_csv = flight_csv.dropna()

print("no of rows and coloumn new",new_flight_csv.shape )


# In[92]:


print(new_flight_csv.duplicated())
new_flight_csv.drop_duplicates()
new_flight_csv.shape
print("No duplicate data")


# In[93]:


# Data Analysis- task 2

origin_count = new_flight_csv['origin'].value_counts()
print("origin \n",origin_count)
dest_count = new_flight_csv['dest'].value_counts()
print("Destination \n",dest_count)


# In[94]:


#visualize the data
import matplotlib.pyplot as plt 

new_flight_csv.hist(bins=50, figsize=(20,15))
plt.show()


# In[95]:


#task 3 create 2 new data sets using "ul" and "da"


# In[95]:





# In[96]:


# Task 3 - Create two new datasets (“dl” and “ua”) of 1000 observations each from the “pop_data” dataset 

# Filter for ua and dl
pop_data=new_flight_csv[(new_flight_csv['carrier'] == 'UA') | (new_flight_csv['carrier'] == 'DL')]

# rename coloumn carrier 
pop_data= pop_data.rename(columns={'carrier':'Company Name', 'arr_delay':'Delayed Arrival flights'})
pop_data = pop_data.filter(['Company Name','Delayed Arrival flights'],axis=1)
pop_data


# In[97]:


# Consider only 20000 records for the DL airline
pop_data_dl=pop_data[(pop_data['Company Name'] == 'DL' )]
pop_data_dl.head(20000)
print('DL sample data',pop_data_dl)

# Consider only 20000 records for the AU airline
pop_data_ua=pop_data[(pop_data['Company Name'] == 'UA' )]
pop_data_ua.head(20000)
print('UA Sample data',pop_data_ua)




# In[97]:





# In[98]:


# Task 4 - create dataframe with 1000 observations of DL

# Consider only 1000 records of the DL airline,assign sample id =1
dl=pop_data_dl.assign(sample_id=1)
dl=dl.head(1000)

#task 5 - create dataframe with 1000 observation of UA
# Consider only 1000 records of the UA airline,assign sample id =2
ua=pop_data_ua.assign(sample_id=2)
ua=ua.head(1000)

samples=pds.concat([dl, ua], axis=0)
print(dl, ua)


# In[98]:





# In[99]:


# task - 6 
# standard error calculation dl

se_dl = np.std(dl, ddof=0) / np.sqrt(np.size(dl))
se_dl =se_dl['Delayed Arrival flights']

print("Standard error deviation is :",se_dl)


# In[100]:


# standard error calculation ua

se_ua = np.std(ua, ddof=0) / np.sqrt(np.size(ua))
se_ua =se_ua['Delayed Arrival flights']

print("Standard error deviation is :",se_ua)


# In[100]:





# In[101]:




#Task 7 - confidence interval for UA
#Take 95% of confidence interval

ua1=ua[['Delayed Arrival flights']].copy()
ua_length=len(ua1)
print("Length of the UA dataset : ",ua_length)
m_ua = np.mean(ua1['Delayed Arrival flights'])
print("Mean of United Airlines:", m_ua)
print("Standard deviation:",se_ua)
flight_csv = ua_length - 1
tDistribution_value = t.ppf(0.95, flight_csv)
print("95% confidence T value : ", tDistribution_value)

ua_lower = m_ua - tDistribution_value * (se_ua / np.sqrt(ua_length))
print ("Lower value of UA : ", ua_lower)
ua_upper = m_ua + tDistribution_value * (se_ua / np.sqrt(ua_length))
print ("Upper Value of UA : ", ua_upper)


# In[101]:






# In[102]:


#Task 7 - confidence interval for DL

dl1=dl[['Delayed Arrival flights']].copy()
dl_length=len(dl1)
print("Length of the DL dataset : ",dl_length)
m_dl = np.mean(dl1['Delayed Arrival flights'])
print("Mean of Delta Arilines is :", m_dl)
print("Standard deviation is :",se_dl)

dl_lower = m_dl - tDistribution_value * (se_dl/ np.sqrt(dl_length))
print ("Lower value of DL : ", dl_lower)
dl_upper = m_dl + tDistribution_value * (se_dl / np.sqrt(dl_length))
print ("Upper Value of DL : ", dl_upper)


# In[102]:






# In[104]:


# Task 8 T-Test of ua and dl
means1=[ua_lower, m_ua, ua_upper]
means2=[dl_lower, m_dl, dl_upper]
print(np.var(means1), np.var(means2))
ttest_ind(a=means1, b=means2, equal_var=True)



