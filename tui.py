"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'COVID-19 (January) Data'.
    The welcome message should contain dashes above and below the title.
    The number of dashes should be equivalent to the number of characters in the title.

    :return: Does not return anything.
    """
    # TODO: Your code here
def welcome_message():
    print('-----------------------')
    print('COVID-19 (January) Data')
    print('-----------------------')
#welcome_message()


def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
    """
    # TODO: Your code here

def error(message):
    print(f'Error!{message}')
#error('Sorry, an error occured. Your request cannot be further processed at this time')



def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100
    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """
    # TODO: Your code here
def progress(operation, value):
    operation = 'The data processing report:'
    if value == 0:
        status = 'The process has started'
        print(f'{operation} {status}')
    elif 0 < value < 100:
        status = 'The process is in progress'
        print(f'{operation} {status} ({value}%) completed')
    elif value == 513:
        status = 'The process is completed.'
        print(f'{operation} {status} ')
        print(f'The data has been loaded')
    #else:
        #print('Put in a number from 0 to 100')
#progress('operation',80)



#def menu(variant=0):
"""
    Task 4: Display a menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    should be displayed:

    '[1] Process Data', '[2] Query Database', '[3] Visualise Data' and '[4] Exit'

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
    '[4] Summarise Records'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Setup database',
    '[2] Retrieve all countries in alphabetical order from the database',
    '[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database',
    '[4] Retrieve top 5 countries for confirmed cases from the database from the database',
    '[5] Retrieve top 5 countries for deaths for specific observation dates form the database'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # TODO: Your code here

# List of operations that can be done on the Data
def menu(variant):
    #user_input = int(input(f'Proceed to select from the options below: '))
    if variant == 0 or variant == '':
        print('[1] Process Data', '[2] Query Database', '[3] Visualise Data' 'and' '[4] Exit')
        print()
        user_input = int(input(f'Proceed to select from the menu options above: '))
        return f'{user_input}'
        return f'You have selected option {user_input}'
        if user_input == 1:
            return f'{user_input}: is for processing data'
        elif user_input == 2:
            return f'{user_input}: is for querying data'
        elif user_input == 3:
            return f'{user_input}: is for visualizing data'
        elif user_input == 4:
            return f'{user_input} : you are about to exit this page'
        else:
            print(f'An error occurred. option {user_input} is not available')
            menu(variant)

# Data processing interface
    elif variant == 1:
        record_by_serial_number = f'Record by Serial Number'
        records_by_observation_date = f'Records by Observation Date'
        group_record_by_country = f'Group Records by Country/Region'
        record_summary = f'Summarise Records'
        print('[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region', '[4] Summarise Records')
        print()
        user_input = int(input(f'Proceed to select from the above options: '))
        return(f'You have selected option {user_input}')
        print()
        if user_input == 1:
            print(f'{user_input} is for {record_by_serial_number}')
        elif user_input == 2:
            return f'{user_input} is for {records_by_observation_date}'
        elif user_input == 3:
            return f'{user_input} is for {group_record_by_country}'
        elif user_input == 4:
            return f'{user_input} is for {record_summary}'
        elif user_input > 4:
            return f'Error! option {user_input} is not available'
            menu(variant)

# The database interface
    elif variant == 2:
        d_setup = f'Setup database'
        all_countries_alph = f'Retrieve all countries in alphabetical order from the database'
        cases_for_obs = f'Retrieve confirmed cases, deaths and recoveries for an observation from the database'
        top_5_countries_for_conf_cases = f'Retrieve top 5 countries for confirmed cases from the database'
        death_top_5_countries = f'Retrieve top 5 countries for deaths for specific observation dates form the database'
        print(d_setup)
        print(all_countries_alph)
        print(cases_for_obs)
        print(top_5_countries_for_conf_cases)
        print(death_top_5_countries)
        print()
        user_input = int(input(f'Proceed to select from the above options: '))
        return f'You have selected option {user_input}'
        print()

        if user_input == 1:
            return f'{user_input} is to {d_setup}'
        elif user_input == 2:
            return f'{user_input} is to {all_countries_alph}'
        elif user_input == 3:
            return f'{user_input} is to {cases_for_obs}'
        elif user_input == 4:
            return f'{user_input} is to {top_5_countries_for_conf_cases}'
        elif user_input == 5:
            return f'{user_input} is to {death_top_5_countries}'
        elif user_input > 5:
            print(f'Error! option {user_input} is not available')
            menu(variant)

# The Data visualization interface
    elif variant == 3:
        country_pie_chart = f'Country/Region Pie Chart'
        observations_chart = f'Observations Chart'
        animated_summary = f'Animated Summary'
        print()
        print('Visualize the data via: ')
        print()
        print('[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary')
        print()

        user_input = int(input(f'Proceed to select select from the above options: '))
        return f'You have selected option {user_input}'

        if user_input == 1:
            return f'{user_input} will display the {country_pie_chart}'
        elif user_input == 2:
            return f'{user_input} will display the {observations_chart}'
        elif user_input == 3:
            return f'{user_input} will display the {animated_summary}'
        elif user_input > 3:
            print(f'Error! option {user_input} is not available')
    elif variant > 3:
        print(f'Sorry! Please, select either option 0, 1, 2 0r 3')
        menu(variant)

#r_statement =menu(0)
#print(r_statement)


def total_records(num_records):
    f"""
    Task 5: Display the total number of records in the data set.
    
    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function
    
    :param num_records: the total number of records in the data set
    :return: Does not return anything
    """
    # TODO: Your code here

#The total number of records in the data set

def total_records(num_records):
    num_records = (num_records)
    if num_records <= 0:
        print('This is not valid')
    elif num_records >513:
        print('Invalid number')
    else:
        print(f'There are {num_records} records in the data set')

#total_records(1)

def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """
    # TODO: Your code here

# Selecting the serial number

def serial_number():
    select_a_serial_no = int(input('Enter a serial number for a record: '))
    #select_a_serial_no <= 513
    print()
    #print(f'You have selected serial number {select_a_serial_no}')
    return select_a_serial_no

#serial_number()
#print(r_s)


def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format mm/dd/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    # TODO: Your code here

# Selecting desired observation dates


def observation_dates():
    select_an_observation_date = input('Enter some observation dates in the format mm/dd/yyyy: ').split()
    return select_an_observation_date
#observation_dates()




def display_record(record, cols=None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a movie
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
# Displaying a specific column indexes
def display_record(record, cols):
    new = []
    if cols == [] or cols == None:
        new = record
    else:
        for column_index in cols:

            new.append(record[column_index])
    print(new)

# Displaying each index record in a list of records
#
#def display_records():
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a movie will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here

def display_records(records, cols):
    new_list = []
    for record in records:
        if cols == None or cols == []:
            print(record)
        else:
            for index in cols:
                new_list.append(record[index])
    print(new_list)
#display_records()
