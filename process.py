"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""


"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here

# def retrieve_records_with_serial_no(records):
#     serial_no = tui.serial_number() - 1  # One is subtracted in order to index appropriately.
#     retrieved_record = records[serial_no]
#     print(records)


# Function to retrieve the total number of loaded records
import csv
import tui
import main
def total_records(records):
    records = main.covid_records
    return(f'{len(records)} data has been loaded') #total number of records retrieved as a list
    #print(records)
#total_records('records')

# Function to retrieve the records with serial number
def retrieve_records_with_serial_no(records):
    records = main.covid_records
    serial_no = tui.serial_number() - 1  # One is subtracted in order to index appropriately.
    retrieved_record = records[serial_no]
    return retrieved_record
#retrieve_records_with_serial_no('records')

# Retrieving the records for the observation dates as specified by the user.
def retrieved_records_by_date(covid_records):
    dates = tui.observation_dates()
    records_needed = main.covid_records
    for contents in records_needed:
        for date in dates:
            if contents[1] == date:
                return contents
#retrieved_records_by_date('covid_records')

# Function to retrieve records grouped by countries/region
def records_grouped_by_country(covid_19_data ):
    new_list = {}
    covid_19_data = main.covid_records
    for data in covid_19_data:
        if data[3] not in new_list:
            new_list[data[3]] = []  # Setting each country as the dictionary key
            new_list[data[3]].append(data)
    return new_list

    needed_list = []
    for record in new_list:   # Iterating through the keys (i.e countries)
        for contents in new_list[record]:       # Iterating through the values in each key(i.e to attach each
            needed_list.append(contents)
    return needed_list
#records_grouped_by_country('covid_19_data')

# Function to retrieve the summary of records for all countries
def display_record(records):
    confirmed_record = []   # List of confirmed cases
    death_record = []   # List of recorded death
    recovered_record = []   # List record of recovered cases
    confirmed_cases = 0     # Total confirmed cases
    total_death = 0     # Total death
    recovered_cases = 0     # Total recovered cases

    records = main.covid_records
    for data in records:
        confirmed_record.append(data[5])
        death_record.append(data[6])
        recovered_record.append(data[7])
    for values in confirmed_record:
        integer_values = int(values) #Converting each values in the confirmed_cases list to an integer
        confirmed_cases = confirmed_cases + integer_values
    print(f'Total confirmed cases: {confirmed_cases}')
    for figures in death_record:
        death_record_integer = int(figures)
        total_death = total_death + death_record_integer
    print(f'Total recorded deaths: {total_death}')
    for numbers in recovered_record:
        recovered_record_integer = int(numbers)
        recovered_cases = recovered_cases + recovered_record_integer
    print(f'Total recovered cases: {recovered_cases}')
#display_record('record')



#main run
#the_records = total_records([])
#records = total_records([])
#retrieve_records_with_serial_no(records)
#retrieved_records_by_date([])
#total_records([])
















