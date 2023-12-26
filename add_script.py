''' Imports data from .csv file into MySQL database (.test in filename means this is for the test sever) '''
import csv
import mysql.connector
from datetime import datetime
import os
import re


def add_courses():
    # open excel sheet
    for file in os.listdir(os.getcwd()):
        if re.match(r"ADD_org_fields_data.*\.csv", file):
            filename = file


    with open(filename, 'r') as file:
        reader = csv.reader(file)

        #next(reader) to skip lines

        # connect to MySQL database
        conn = mysql.connector.connect(host='',
                                        user='',
                                        password='',
                                        db='',
                                        charset='')
        cursor = conn.cursor()

        sqlInsert = """ INSERT INTO table_name (table_column1, table_column2, table_column3, table_column4, table_column5, table_column6, table_column7, table_column8)
                            VALUES (%(table_column1)s, %(table_column2)s, %(table_column3)s, %(table_column4)s, %(table_column5)s, %(table_column6)s, %(table_column7)s, %(table_column8)s); """


        # loop through rows of each sheet
        header = next(reader)
        item_Dict = {}
        for item in reader:
            if ''.join(item).strip():
                item_Dict['table_column1'] = item[0]
                item_Dict['table_column2'] = item[1]
                item_Dict['table_column3'] = item[2]
                item_Dict['table_column4'] = item[3]
                item_Dict['table_column5'] = item[4]
                item_Dict['table_column6'] = item[6]
                item_Dict['table_column7'] = item[7]
                item_Dict['table_column8'] = item[5]


                clean_Data(item_Dict)

                cursor.execute(sqlInsert, item_Dict)

    conn.commit()
    cursor.close()
    conn.close()

def clean_Data(data_Dict):
    # If cell was empty, set the value to None (NULL)
    if data_Dict['table_column1'] == '':
        data_Dict['table_column1'] = None
    if data_Dict['table_column2'] == '':
        data_Dict['table_column2'] = None
    if data_Dict['table_column3'] == '':
        data_Dict['table_column3'] = None

    if data_Dict['date_IN'] != None and len(data_Dict['date_IN']) == 0:
        data_Dict['date_IN'] = None

    elif data_Dict['date'] != None and data_Dict['date'].count('/') == 2:
        formatted_issue_date = datetime.strptime(data_Dict['date'], "%m/%d/%Y").strftime('%Y-%m-%d')
        data_Dict['date'] = formatted_issue_date

    if data_Dict['table_column4'] != None and len(data_Dict['table_column4']) == 0:
        data_Dict['table_column4'] = None



if __name__ == '__main__':
    add_courses()
