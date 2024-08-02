#!/usr/bin/env python
# coding: utf-8

# ## To load the scraped data into SQL Server, follow these steps:

# ## Install Required Packages
# 

# In[1]:


import pandas as pd
import pyodbc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, UniqueConstraint, text


# ## Set Up SQL Server Connection
# Establish a connection to the SQL Server instance.

# In[2]:


# Define your connection string
server = 'localhost'  # Replace with the IP address or hostname of your SQL Server instance
database = 'amdaridb'
username = 'sa'
password = 'amdaripassword_01'
driver = '{ODBC Driver 18 for SQL Server}'


# In[3]:


# Create the connection string with TrustServerCertificate
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}&TrustServerCertificate=yes'


# In[4]:


# Create the SQLAlchemy engine
engine = create_engine(connection_string)


# In[5]:


# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("Connection successful:", result.fetchall())
except Exception as e:
    print("Error connecting to the database:", str(e))


# In[ ]:


# Create the university table if it doesn't exist
with engine.connect() as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS university (
            id BIGINT IDENTITY(1,1) PRIMARY KEY,
            country NVARCHAR(255) NOT NULL,
            university NVARCHAR(255) NOT NULL,
            founded INT NOT NULL,
            type NVARCHAR(255) NOT NULL,
            enrollment BIGINT NOT NULL,
            link NVARCHAR(255) NOT NULL,
            UNIQUE (country, university)
        );
    """)


# In[ ]:


# Create metadata object
metadata = MetaData()


# ## Create the Table Schema
# Define the table schema in SQL Server and create the table.

# In[ ]:


# Define the university table
university = Table('university', metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('country', String(255), nullable=False),
    Column('name', String(255), nullable=False),
    Column('founded', Integer, nullable=False),
    Column('type', String(255), nullable=False),
    Column('enrollment', BigInteger, nullable=False),
    Column('link', String(255), nullable=False),
    UniqueConstraint('country', 'name', name='unique_combination')
)

# Create the table in the database
metadata.create_all(engine)
print("Table 'university' created successfully.")


# In[ ]:


df = pd.read_csv('universities_clean.csv')


# In[ ]:


# Insert the DataFrame into the university table
with engine.connect() as connection:
    for index, row in df.iterrows():
        insert_statement = f"""
        INSERT INTO university (country, name, founded, type, enrollment, link)
        VALUES ('{row['country']}', '{row['name']}', {row['founded']}, '{row['type']}', {row['enrollment']}, '{row['link']}')
        ON CONFLICT (country, name) DO UPDATE
        SET founded = EXCLUDED.founded,
            type = EXCLUDED.type,
            enrollment = EXCLUDED.enrollment,
            link = EXCLUDED.link;
        """
        connection.execute(insert_statement)

print("Data loaded successfully!")


# In[ ]:


# Check the data in the SQL Server database
query = "SELECT * FROM university"
df_check = pd.read_sql(query, engine)
print(df_check.columns)


# In[ ]:


df_check.shape

