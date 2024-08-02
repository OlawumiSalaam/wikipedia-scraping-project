#!/usr/bin/env python
# coding: utf-8

# ## Loading Scraped Data into MySQL Database
# This notebook I loaded cleaned university data into a MySQL database. The data is first read from a CSV file, and then inserted into a MySQL database using SQLAlchemy and pymysql.
# 
# Dependencies: Python installed with pandas, pymysql, and SQLAlchemy libraries.
# 
# MySQL server running and accessible.
# 
# Cleaned data available in universities_clean.csv.
# 
# SQL script files mysql_create_table.sql and mysql_upsert.sql for creating and upserting data into the MySQL table.

# ## 1. Import Libraries

# In[2]:


import pandas as pd     # for data manipulation
import pymysql          # pymysql to connect to MySQL
from sqlalchemy import create_engine       # to create the database engine


# ## 2. Read the Cleaned Data

# In[3]:


# read the data into df
df = pd.read_csv('universities_clean.csv')


# In[4]:


# display the first 5 rows
df.head()


# ## 3. Establish Connection to MySQL Database

# In[ ]:


# define the parameters and set up the connection to the database
conn = pymysql.connect(
    host='localhost',  # Hostname 
    port=3306,  # Port number of the MySQL server
    user='amdariuser',  # Username for the MySQL database
    password='amdariuserpassword',  # Password for the MySQL database
    database='amdaridb'  # Name of the database to connect to
)
  # Create a cursor object to execute SQL queries
cursor = conn.cursor()


# ## 4. Verify Connection and Database State

# In[7]:


# Execute SQL command to show all databases
cursor.execute('SHOW DATABASES;')


# In[8]:


# check the results to verify the connection
cursor.fetchall()


# In[9]:


# Execute SQL command to show all tables in the current database
cursor.execute('SHOW TABLES;')


# In[10]:


# check the results to verify the connection
cursor.fetchall()


# ## 5. Create Table in MySQL

# In[22]:


# create table
create_query_file = open('./sql/mysql_create_table.sql')
create_query = create_query_file.read()
create_query


# In[23]:


cursor.execute(create_query)


# ## 6. Prepare Data for Insertion

# In[31]:


data = list(df.itertuples(index=None, name=None))


# In[32]:


data


# ## 7. Create SQLAlchemy Engine

# In[27]:


engine = create_engine('mysql+pymysql://', creator=lambda:conn)


# In[28]:


pd.read_sql('SELECT * FROM university;', con=engine)


# ## 8. Load Data into the Database
# Open and read the SQL script file 'mysql_upsert.sql'. The script contains the SQL command for inseting the scraped data into the table.

# In[34]:


# load data into the database

merge_query_file = open('./sql/mysql_upsert.sql')
merge_query = merge_query_file.read()
merge_query


# In[35]:


cursor.executemany(merge_query, data)


# In[1]:


# save changes to the database
conn.commit()


# ## 9. Verify Data loading

# In[39]:


# read the contents of the university table again to verify that the data has been inserted successfully
pd.read_sql("SELECT * FROM university;", con= engine)


# ## Conclusion
# I loaded the cleaned data from a CSV file into a MySQL database using pandas, pymysql, and SQLAlchemy. I can efficiently manage and interact with your MySQL database.

# In[ ]:




