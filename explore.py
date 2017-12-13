import json
import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('data/chaordic.db')
c = conn.cursor()

show_sql_commands = False

# Open and read the file as a single buffer
fd = open('data/create_tables.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands

    try:
        c.execute(command)
    except OperationalError:
        print ("Command skipped: ", command)

def do_insert(command):
    try:
        if True:
            print(command)

        c.execute(command)
    except OperationalError:
        print ("Command skipped: ", command)

def rec_obj(input_obj, key_list):

    if type(input_obj) is dict:

        for key, value in input_obj.items():

            if type(value) is dict:
                rec_obj(value,key)

            elif type(value) is list:
                rec_obj(value, key)

            else:
                key_name = key if key_list=="" else key_list+"_"+key
                #print(key_name, " => ", value)
                data_structured.append([key_name,value])

    elif type(input_obj) is list:

        for entry in input_obj:
            rec_obj(entry, key_list)

    else:

        #print(key_list, " => ", input_obj)
        data_structured.append([key_list, input_obj])

def InsertSQL(data_structured, table):

    if table == "transactions":

        fields = []
        values = []

        for entry in data_structured:
            if "items_" not in entry[0]:
                fields.append(entry[0])
                values.append(entry[1])
                if entry[0]=="id":
                    order_id = entry[1]
        sqlText = "Insert Into {} ({}) Values ({})".format(table,fields,values)
        sqlText = sqlText.replace("[","")
        sqlText = sqlText.replace("]", "")
        sqlText = sqlText.replace("None", "null")
        #print(sqlText+";")
        do_insert(sqlText)

        fields = ['id']
        values = [order_id]

        for entry in data_structured:

            if "items_" in entry[0]:

                fields.append(entry[0])
                values.append(entry[1])

                if entry[0] == "items_quantity":
                    sqlText = "Insert Into {} ({}) Values ({})".format(table+"_items", fields, values)
                    sqlText = sqlText.replace("[","")
                    sqlText = sqlText.replace("]", "")
                    sqlText = sqlText.replace("None", "null")
                    #print(sqlText+";")
                    do_insert(sqlText)
                    fields = ['id']
                    values = [order_id]

    if table == "clicks":

        fields = []
        values = []

        for entry in data_structured:
            fields.append(entry[0])
            values.append(entry[1])

        sqlText = "Insert Into {} ({}) Values ({})".format(table,fields,values)
        sqlText = sqlText.replace("[","")
        sqlText = sqlText.replace("]", "")
        sqlText = sqlText.replace("None", "null")
        #print(sqlText+";")
        do_insert(sqlText)

    if table == "pageviews":

        my_id = next(unique_sequence)
        fields = ['my_id']
        values = [my_id]

        for entry in data_structured:
            if "tags" not in entry[0]:
                fields.append(entry[0])
                values.append(entry[1])
        sqlText = "Insert Into {} ({}) Values ({})".format(table,fields,values)
        sqlText = sqlText.replace("[","")
        sqlText = sqlText.replace("]", "")
        sqlText = sqlText.replace("None", "null")
        #print(sqlText+";")
        do_insert(sqlText)

        fields = ['my_id']
        values = [my_id]

        for entry in data_structured:

            if "tags" in entry[0]:

                fields.append(entry[0])
                values.append(entry[1])

                if entry[0] == "tags":
                    sqlText = "Insert Into {} ({}) Values ({})".format(table+"_tags", fields, values)
                    sqlText = sqlText.replace("[","")
                    sqlText = sqlText.replace("]", "")
                    sqlText = sqlText.replace("None", "null")
                    #print(sqlText+";")
                    do_insert(sqlText)
                    fields = ['my_id']
                    values = [my_id]

    if table == "impressions":

        my_id = next(unique_sequence)
        fields = ['my_id']
        values = [my_id]

        for entry in data_structured:
            if "products" not in entry[0]:
                fields.append(entry[0])
                values.append(entry[1])
        sqlText = "Insert Into {} ({}) Values ({})".format(table,fields,values)
        sqlText = sqlText.replace("[","")
        sqlText = sqlText.replace("]", "")
        sqlText = sqlText.replace("None", "null")
        #print(sqlText+";")
        do_insert(sqlText)

        fields = ['my_id']
        values = [my_id]

        for entry in data_structured:

            if "products" in entry[0]:

                fields.append(entry[0])
                values.append(entry[1])

                if entry[0] == "products":
                    sqlText = "Insert Into {} ({}) Values ({})".format(table+"_products", fields, values)
                    sqlText = sqlText.replace("[","")
                    sqlText = sqlText.replace("]", "")
                    sqlText = sqlText.replace("None", "null")
                    #print(sqlText+";")
                    do_insert(sqlText)
                    fields = ['my_id']
                    values = [my_id]

def uniqueid():
    seed = 1 #random.getrandbits(32)
    while True:
       yield seed
       seed += 1

unique_sequence = uniqueid()

files_list = ['clicks','impressions','pageviews','transactions']

files_list = ['transactions']

for file_i in files_list:

    with open('data/'+file_i+'/'+file_i+'.json', 'r') as f:

        count = 0

        for line in f:

            data_structured = []

            count = count + 1

            json_objs = line.split("}{")

            if show_sql_commands:
                print(line)

            if len(json_objs)>=2:

                for obj in json_objs:

                    if obj[0]=="{":
                        obj2 = obj+"}"
                    else:
                        obj2 = "{"+obj

                    data_structured = []
                    data = json.loads(obj2)
                    rec_obj(data, "")
                    InsertSQL(data_structured, file_i)
            else:

                data_structured = []
                data = json.loads(line)
                rec_obj(data, "")
                InsertSQL(data_structured, file_i)

            #print (data)
            #print("------------------------------------------")

            #if count == 1000 and False:
            #    break

        print (count," rows inserted into ", file_i)

conn.commit()
c.close()
conn.close()


'''
1,182,979  rows inserted into  clicks
25,798,744  rows inserted into  impressions
30,367,495  rows inserted into  pageviews
109,171  rows inserted into  transactions
'''