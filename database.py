"""
This module is responsible for setting up and querying the database.
"""
import main
import tui

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""

# TODO: Your code here

# Setting up the database
import sqlite3
import csv

def setup_database(covid_19_data):
    db = sqlite3.connect('Covid.db')
    cursor = db.cursor()
    covid_19_data = main.covid_records
    for data_records in covid_19_data:
        covid_table = f"INSERT INTO Covid_data_table(country, observ_date, confirmed_cases, death_cases, recovered_cases) VALUES('{data_records[3]}','{data_records[1]}','{data_records[5]}','{data_records[6]}','{data_records[7]}');"
        cursor.execute(covid_table)
        db.commit()
    db.close()
setup_database ('covid_19_data.csv')


#Functions to query the database
#def retrieve_names_of_unique_countries():
    #list_of_countries = []
    #db = sqlite3.connect('Covid.db')
    #cursor = db.cursor()

# The the SQL query to group the countries uniquely
    #group_of_countries = "SELECT country,count(country) FROM Country_table GROUP by country HAVING count(country);"
    #cursor.execute(group_of_countries)
    #country_list = cursor.fetchall()
    #for countries in country_list:
        #list_of_countries.append(countries)
    #print()
    #print(f'The {len(country_list)} countries are:')
    #print()
    #print(f'{list_of_countries}')
    #db.close()
#retrieve_names_of_unique_countries()

#def retrieve_confirmed_cases_deaths_cases_and_recovered_cases():
    #record_list = []
    #db = sqlite3.connect('Covid.db')
    #cursor = db.cursor()

# The Query to retrieve confirmed,deaths and recovered cases by observation/serial_no
#     needed_record = f"SELECT confirmed_cases,death_cases,recovery_cases FROM Covid_Table WHERE serial_no = '{tui.serial_number()}';"
#     cursor.execute(needed_record)
#     retrieved_record = cursor.fetchall()
#     for data in retrieved_record:
#         record_list.append(data)
#     #return record_list
    #print(f'The confirmed cases are {data[0]}')
    #print(f'The recorded death is {data[1]}')
    #print(f'The recovery_cases is {data[2]}')
#retrieve_confirmed_cases_deaths_cases_and_recovered_cases()









