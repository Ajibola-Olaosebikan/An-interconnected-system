# """
# This module is responsible for visualising the data retrieved from a database using Matplotlib.
# """
#
# """
# Task 28 - 30: Write suitable functions to visualise the data as follows:
#
# - Display the top 5 countries for confirmed cases using a pie chart
# - Display the top 5 countries for death for specific dates using a bar chart
# - Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
# time. This could focus on a specific country/countries.
#
# Each function for the above should utilise the functions in the module 'database' to retrieve any data.
# You may add additional methods to the module 'database' if needed. Each function should then visualise
# the data using Matplotlib.
# """
#
# # TODO: Your code here
# import csv
# def total_records(covid_19_data):
#     observation_date = input('date needed: ').split()
#     covid_records = []
#     covid_19_data = 'covid_19_data.csv'
#     with open(covid_19_data) as covid_data:
#         covid_data_records = csv.reader(covid_data)
#         next(covid_data_records)
#         for data in covid_data_records:
#             covid_records.append(data)
#
#     for contents in covid_records:
#         for dates in observation_date:
#             if contents[1] == dates:
#                 print(contents)
#     total_records([])


#
#
#         #print(f'{len(covid_records)} data has been loaded') #total number of records retrieved as a list
#     #print(covid_records[0:])
# total_records([])

import csv
def total_records(covid_19_data ):
    covid_records = []
    new_list = {}

    with open(covid_19_data) as covid_data:
        covid_data_records = csv.reader(covid_data)
        next(covid_data_records)
        for data in covid_data_records:
            covid_records.append(data)
            if data[3] not in new_list:
                new_list[data[3]] = []  # Setting each country as the dictionary key
            new_list[data[3]].append(data)
        print(new_list)

        needed_list = []
        for record in new_list:   # Iterating through the keys (i.e countries)
            for contents in new_list[record]:     # Iterating through the values in each key(i.e to attach each
                needed_list.append(contents)
        print(needed_list)
total_records('covid_19_data.csv')

        #print(new_list)



#total_records('covid_19_data.csv')