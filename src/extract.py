#!/usr/bin/env python
# coding: utf-8

# ## Task Overview
# In this task, I extracted data about the largest universities from Wikipedia. I then saved the data in CSV and JSON formats and loaded it into a Pandas DataFrame for further analysis. 

# ## Tech stack Used
# Programming Language: Python
# 
# Libraries: requests, BeautifulSoup, pandas, csv, json
# 
# IDE: VS Code

# ## 1. Data Extraction
# I used the requests library to send a GET request to the Wikipedia page and BeautifulSoup to parse the HTML content and extract data.

# In[32]:


# import necessary libraies
import requests
from bs4 import BeautifulSoup


# In[33]:


# Send a GET request to the Wikipedia page
response = requests.get('https://en.wikipedia.org/wiki/List_of_largest_universities')


# In[34]:


response.content
soup = BeautifulSoup(response.content)


# In[36]:


# Find the table with the class 'sortable'
table = soup.find('table', attrs={'class' : 'sortable'})
trs= table.findAll('tr')


# In[38]:


# Extract column headers
columns = []
for item in trs[0].findAll('th'):
    print(item.text.strip())
    columns.append(item.text.strip())


# In[39]:


# check the items in the columns
columns


# In[40]:


# Extract the text from each table header cell, remove any leading/trailing whitespace,
# and convert the list of header names into a list.
# Update the last column header to 'Link'

columns = list(map(lambda x: x.text.strip(), trs[0].findAll('th')))
columns[-1] ='Link'


# In[41]:


# check if the 'ref' column has been updated as 'Link'
columns


# In[1]:





# ## 2. Extracting Row Data
# I defined a function to extract data from each row, adding a link to the university’s Wikipedia page.
# 
# 

# In[44]:


def extract_row(tr):
    row_soup_list = tr.findAll('td')
    row = list(map(lambda x: x.text.strip(), row_soup_list))
    if len(row) < 6:
        row.append('')
        print(row)

    link= row_soup_list[1].a.attrs['href'].lstrip('/')
    row[-1] = f'https://en.wikipedia.org/{link}' if link else ''
    #print("Link: ", link)
    return row


# In[ ]:


rows = trs[1:]
rows[0].findAll('td')[1].a.attrs['href'].lstrip('/')


# In[45]:


extract_row(rows[35])


# In[ ]:


# Extract data from each row
data = [extract_row(tr) for tr in rows]


# In[ ]:





# ## 3. Saving Data
# I saved the extracted data in CSV and JSON formats.
# 
# 

# In[48]:


# import libraries
import csv
import json


# In[49]:


# Save data to CSV
with open('universities.csv', 'w',newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(columns)
    csvwriter.writerows(data)


# In[ ]:


# Save data to JSON
with open('universities.json', 'w') as f:
    json.dump(data, f, indent=4)  # Write JSON data with indentation


# ## 4. Loading Data into a DataFrame
# I loaded the data into a Pandas DataFrame for analysis.

# In[2]:


# import necessary libraries
import pandas as pd


# In[52]:


# create a dataframe from the scraped data
df = pd.DataFrame(data= data, columns = columns)


# In[53]:


df


# ## Conclusion
# Extracted Data: Successfully scraped the data of the largest universities from Wikipedia.
# 
# Data Formats: Saved the data as universities.csv and universities.json.
# 
# Data Analysis: Loaded the data into a Pandas DataFrame for further analysis and manipulation.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[ ]:




