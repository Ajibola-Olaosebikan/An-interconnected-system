df={}
df['mainland']=[[11,'adfa','main','adasd'],[112,'dad','maim']]
df['asd']=[3,4]
df['232ew']=[5,6]
#
dl = []
#for recs in df:
#     for i in df[recs]:
#         dl.append(i)
# #print(dl)
#
# import csv
# import tui
#
# def total_records(covid_19_data ):
#
#     covid_records = []
#
#
#     with open(covid_19_data) as covid_data:
#         covid_data_records = csv.reader(covid_data)
#         next(covid_data_records)
#         for data in covid_data_records:
#             covid_records.append(data)
#         #print(covid_records)
#         tui.display_record(covid_records,1)
#         print(covid_records)
# #tui.display_record(['covid_records'],[0] )
#
#
# #total_records('covid_19_data.csv')
#
# def display_record(record, cols):
#     new = []
#     if cols == [] or cols == None:
#         new = record
#     else:
#         for column_index in cols:
#
#             new.append(record[column_index])
#     print(new)
# #display_record(['2','ear','bread'], [1])
#import tui
import csv
def display_record(record):
    covid_records = []  # List of records
    confirmed_record = []   # List of confirmed cases
    death_record = []   # List of recorded death
    recovered_record = []   # List record of recovered cases
    confirmed_cases = 0     # Total confirmed cases
    total_death = 0     # Total death
    recovered_cases = 0     # Total recovered cases
    covid_19_data = 'covid_19_data.csv'
    with open(covid_19_data) as covid_data:
        covid_data_records = csv.reader(covid_data)
        next(covid_data_records)
        for data in covid_data_records:
            confirmed_record.append(data[5])
            death_record.append(data[6])
            recovered_record.append(data[7])
        #print(recovered_record)
        for values in confirmed_record:
            integer_values = int(values) #Converting each values in the new_list to an integer
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




            # def chain(*iterables):
            #     # chain('ABC', 'DEF') --> A B C D E F
            #     for it in iterables:
            #         for element in it:
            #             yield element

            #covid_records.append(data)

        #str(sum(int(x) for x in ages))

            #y=sum(con_date)
            #if con_date==4:
                #obser_date+=1
            #print(y)        #print(f'{con_date} cases were confirmed')
#display_record('record')
#print('The combined age of all in the list is ' + str(sum(int(x) for x in ages)) + '.

def total_records(covid_19_data ):
    covid_records = []
    new_list = {}
    list = []
    with open(covid_19_data) as covid_data:
        covid_data_records = csv.reader(covid_data)
        next(covid_data_records)
        for data in covid_data_records:
            covid_records.append(data)
            if data[3] not in new_list:
                new_list[data[3]] = []  # Setting each country as the dictionary key
            new_list[data[3]].append(data)
            for values in new_list.values():
                list.append(values)

                #print(values)
#total_records('covid_19_data.csv')


def getList(dict):
    list = []
    for values in dict.values():
        list.append(values)

    return list


# Driver program
dict = {1: 56, 2: 4, 3: 5}
#print(sum(getList(dict)))
# def error_message(error):
#     for lets in error:
#         print(lets)
#error_message('good message')




# def display_records(records, cols):
#     new_list = []
#     r_list = []
#     for record in records[0:]:
#         if cols == None or cols == []:
#             print(records)
#
#         else:
#             for index in cols:
#                 new_list.append(record[index])
    #print(new_list[0:])
    #print(new_list[1:])
#display_records([['2','1','eat','ram'],['45','wet','65']], [0,1,2])

r = [['eat', '43', 'rat', 'book'], ['tea','45','tap','sat','55']]
u = []
for content in r:
    u.append(content[1])
    #print(u)
i = ['2','4','eat']
r = len(i)
#print(r)

j = ['3','2','6','7']
t = 0
for fig in j:
    needed_fig = int(fig)
    t = t + needed_fig
#print(t)

import sqlite3
# import csv
import main
import tui

# def setup_database(covid_19_data):
#     db = sqlite3.connect('Covid.db')
#     cursor = db.cursor()
#     covid_records = []
#     with open(covid_19_data) as covid_data:
#         covid_data_records = csv.reader(covid_data)
#         next(covid_data_records)
#         for data in covid_data_records:
#             covid_records.append(data)
#         print(covid_records)
#setup_database ('covid_19_data.csv')

def display_records(records, cols):
    new_list = []
    for record in records:
        #if cols == None or cols == []:
            #print(record)
        #else:
            for index in cols:
                new_list.append(record[index])
    #print(new_list)
#display_records([(['eat', '4', 'yam']), (['thief', '90', 'bet'])], None)


def retrieved_records_by_date(covid_19_data):
    dates = tui.observation_dates()
    y =  main.covid_data_records

    # covid_records = []
    # covid_19_data = 'covid_19_data.csv'
    # with open(covid_19_data) as covid_data:
    #     covid_data_records = csv.reader(covid_data)
    #     next(covid_data_record)

    for contents in y:

         for date in dates:
#
#              if contents[1] == date:
#
#                  print(contents)
# retrieved_records_by_date('covid_records')

if __name__ == '__main__':
    main.run()
