import csv
import mysql.connector
from datetime import datetime
import os
import re 


def update_courses():
    # open excel sheet
    for file in os.listdir(os.getcwd()):
        if re.match(r"UPDATE_org_fields_data.*\.csv", file):
            filename = file
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) #uncomment to skip a line

        # connect to MySQL database
        conn = mysql.connector.connect(host='',
                                        user='',
                                        password='',
                                        db='',
                                        charset='')
        cursor = conn.cursor()

        #IF(condition, value_if_true, value_if_false)
        sql_update_courses =""" UPDATE new_table 
                                SET 
                                    table_column1=IF(LENGTH(%(table_column1)s)=0, Value, %(table_column1)s), 
                                    table_column2=IF(LENGTH(%(table_column2)s=0, email, %(table_column2)s) 
                                WHERE id=%(id_IN)s """


        # loop through rows of each sheet
        
        item_Dict = {}
        for item in reader:
            if ''.join(item).strip():
                item_Dict['id_IN'] = item[0]
                item_Dict['table_column1'] = item[1]
                item_Dict['table_column2'] = item[2]
                cursor.execute(sql_update_courses, item_Dict)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    update_courses()