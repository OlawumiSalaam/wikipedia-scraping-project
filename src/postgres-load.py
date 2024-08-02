#!/usr/bin/env python
# coding: utf-8

# ## Install Required Libraries
# 
# To load the scraped data from the wikipedia page saved as university_clean.csv into the PostgreSQL database, we will use Python along with the pandas, SQLAlchemy and psycopg2 libraries. psycopg2 library, is the most popular PostgreSQL adapter for Python.
# Using pip, Run the following command in the virtual environment:
# 
# pip install psycopg2-binary
# 
# 
# 

# ## Import the necessary libraries

# In[1]:


import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, UniqueConstraint
from sqlalchemy.dialects.postgresql import insert



# ## Connect to PostgreSQL 

# #### Connection Parameters:
# 
# dbname: The name of your PostgreSQL database.
# 
# user: The PostgreSQL username.
# 
# password: The PostgreSQL password.
# 
# host: The hostname or IP address where your PostgreSQL 
# server is running (use localhost if it's running on your local machine).
# 
# port: The port number on which your PostgreSQL server is listening (default is 5432).

# In[2]:


# Define your database connection parameters
db_params = {
    'dbname': 'amdaridb',
    'user': 'amdariuser',
    'password': 'amdariuserpassword',
    'host': 'localhost',  # Use 'localhost' when accessing from the host machine
    'port': '5432'        # Default PostgreSQL port
}



# ## SQLAlchemy Engine:
# 
# create_engine(connection_string): This function creates a new SQLAlchemy engine instance.

# In[3]:


# Create the connection string
connection_string = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)


# ## Metadata:
# 
# MetaData(): Holds a collection of Table objects and their associated schema constructs.

# In[4]:


# Define the metadata
metadata = MetaData()


# ## Table Definition:
# 
# Define the table structure using Table() and Column(), specifying the data types and constraints.

# In[5]:


df= pd.read_csv('universities_clean.csv')


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


# Rename DataFrame columns to lowercase
df.rename(columns=str.lower, inplace=True)


# In[9]:


df.columns


# In[10]:


# Define the university table
metadata = MetaData()
university = Table('university', metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('country', String(255), nullable=False),
    Column('university', String(255), nullable=False),
    Column('founded', Integer, nullable=False),
    Column('type', String(255), nullable=False),
    Column('enrollment', BigInteger, nullable=False),
    Column('link', String(255), nullable=False),
    UniqueConstraint('country', 'university', name='unique_combination'),
    extend_existing=True  # This allows redefining the table
)


# ## Create Table:
# 
# metadata.create_all(engine): This function creates the table in the database if it does not already exist.

# In[11]:


# Create the table in the database
metadata.create_all(engine)

print("Table 'university' created successfully.")


# In[12]:


# Check if the university table exists
with engine.connect() as connection:
    try:
        result = connection.execute(text("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'university');"))
        exists = result.scalar()
        if exists:
            print("The table 'university' still exists.")
        else:
            print("The table 'university' has been successfully deleted.")
    except Exception as e:
        print(f"Error checking table existence: {e}")


# In[13]:


# Check the data in the PostgreSQL database
query = "SELECT * FROM university"
df_check = pd.read_sql(query, engine)


# In[14]:


df_check.columns


# In[15]:


# Display the first few rows of the DataFrame
print(df_check.head())


# ## Insert the dataframe into the university table
# Insert the data into the university table using on_conflict_do_update to handle duplicates.

# In[16]:


# Check DataFrame columns
print("DataFrame columns:", df.columns)


# In[21]:


# Insert the DataFrame into the university table
with engine.begin() as connection:
    for index, row in df.iterrows():
        insert_statement = text("""
            INSERT INTO university (country, university, founded, type, enrollment, link)
            VALUES (:country, :university, :founded, :type, :enrollment, :link)
            ON CONFLICT (country, university)
            DO UPDATE SET
                founded = EXCLUDED.founded,
                type = EXCLUDED.type,
                enrollment = EXCLUDED.enrollment,
                link = EXCLUDED.link;
        """)
        params = {
            'country': row['country'],
            'university': row['university'],
            'founded': row['founded'],
            'type': row['type'],
            'enrollment': row['enrollment'],
            'link': row['link']
        }
        print(f"Executing: {insert_statement} with params: {params}")
        connection.execute(insert_statement, params)

print("Data loaded successfully.")


# In[20]:


# Insert the DataFrame into the university table
with engine.connect() as connection:
    for index, row in df.iterrows():
        insert_statement = text("""
            INSERT INTO university (country, university, founded, type, enrollment, link)
            VALUES (:country, :university, :founded, :type, :enrollment, :link)
            ON CONFLICT (country, university)
            DO UPDATE SET
                founded = EXCLUDED.founded,
                type = EXCLUDED.type,
                enrollment = EXCLUDED.enrollment,
                link = EXCLUDED.link;
        """)
        params = {
            'country': row['country'],
            'university': row['university'],
            'founded': row['founded'],
            'type': row['type'],
            'enrollment': row['enrollment'],
            'link': row['link']
        }
        print(f"Executing: {insert_statement} with params: {params}")
        connection.execute(insert_statement, params)

print("Data loaded successfully.")


# In[18]:


# Insert the DataFrame into the university table
with engine.connect() as connection:
    for index, row in df.iterrows():
        insert_statement = text("""
            INSERT INTO university (country, university, founded, type, enrollment, link)
            VALUES (:country, :university, :founded, :type, :enrollment, :link)
            ON CONFLICT (country, university)
            DO UPDATE SET
                founded = EXCLUDED.founded,
                type = EXCLUDED.type,
                enrollment = EXCLUDED.enrollment,
                link = EXCLUDED.link;
        """)
        connection.execute(insert_statement, {
            'country': row['country'],
            'university': row['university'],
            'founded': row['founded'],
            'type': row['type'],
            'enrollment': row['enrollment'],
            'link': row['link']
        })

print("Data loaded successfully.")


# ## Verify the Data

# In[22]:


# Check the data in the PostgreSQL database
query = "SELECT * FROM university"
df_check = pd.read_sql(query, engine)
print(df_check.columns)
print(df_check)


# In[23]:


df_check.head()


# In[24]:


df_check.shape


# In[ ]:


# Check for any missing data
print("Missing values:\n", df_check.isnull().sum())


# In[ ]:


# Check the types of data in each column
print("Data types:\n", df_check.dtypes)


# In[ ]:




