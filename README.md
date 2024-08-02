# Wikipedia Web Scraping Project

## Overview
This project involves extracting data about the largest universities from Wikipedia, saving the data in CSV and JSON formats, and loading it into various databases for further analysis. The main features include:
- Data extraction from Wikipedia using BeautifulSoup.
- Data storage in CSV and JSON formats.
- Data cleaning
- Loading cleaned data into MySQL, PostgreSQL, and SQL Server databases.

## Tech Stack Used
Programming Language: Python
Libraries: requests, BeautifulSoup, pandas, csv, json
IDE: VS Code
Databases: MySQL, PostgreSQL, SQL Server
## Setup Instructions
### Prerequisites
Python: Make sure you have Python installed on your system. You can download it from python.org.
Virtual Environment: It is recommended to use a virtual environment to manage dependencies.
Database Setup: Ensure you have MySQL, PostgreSQL, and SQL Server installed and running on your system.

### Installation Steps
1. Clone the Repository
	git clone https://github.com/OlawumiSalaam/wikipedia-scraping-project.git

	cd wikipedia-data-harvest

2. Set Up Virtual Environment

	python -m venv venv

	On Windows use `venv\Scripts\activate`

3. Database Configuration

MySQL: Create a database named universities in MySQL.

PostgreSQL: Create a database named universities in PostgreSQL.

SQL Server: Create a database named universities in SQL Server.

5. Environment Variables

Create a .env file in the project root and add your database configuration.

MYSQL_USER=<your_mysql_username>

MYSQL_PASSWORD=<your_mysql_password>

MYSQL_DB=<your_mysql_database>

MYSQL_HOST=<your_mysql_host>

POSTGRES_USER=<your_postgres_username>

POSTGRES_PASSWORD=<your_postgres_password>

POSTGRES_DB=<your_postgres_database>

POSTGRES_HOST=<your_postgres_host>

SQLSERVER_USER=<your_sqlserver_username>

SQLSERVER_PASSWORD=<your_sqlserver_password>

SQLSERVER_DB=<your_sqlserver_database>

SQLSERVER_HOST=<your_sqlserver_host>

## Usage

### Run the script to extract and save data from Wikipedia into CSV and JSON formats:
	python extract.py

### Clean the saved data:
	python data_cleaning.py
### Load Data into Databases
Load the data into MySQL:
	python mysql-load.py

Load the data into PostgreSQL:

	python postgres-load.py

Load the data into SQL Server:

	python sqlserver-load.py


### Optional: Run the notebooks:
Open Jupyter Notebook and run the cells in the provided notebooks in the notebooks directory for interactive interface






