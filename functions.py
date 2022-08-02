import csv
from logging import exception

#Creates a DataTable
def createTABLE(curs):
    name = input("What is the name of the new table?")
    try:
        curs.execute(f"""CREATE TABLE {name}
                                        (id integer, brand test, name text, quantity integer, price integer, total real, url text, notes text, unit text)""")
        print("\nTable created with success\n")
    except:
        print("\nYou already have this data table\n")

#Create a CSV file
def createCSV(curs):
    name = input("What is the name of the table that you want create a csv file with? ")
    try:
        with open('data.csv', 'w') as csvfile:
            filewrite = csv.writer(csvfile, delimiter=',')
            for row in curs.execute(f"SELECT * FROM {name}"):
                li = []
                li.clear()
                li.append(row)
                filewrite.writerow(row)
                print("\nCSV created with success\n")
    except: 
        print("There was an error")

#Adds another row
def addRow(table):
    tables_name = input("What is the table's name?")
    id = int(input("Id = "))
    brand = input("Brand = ")
    name = input("Name = ")
    quantity = int(input("Quantity = "))
    price = int(input("Price = "))
    total = quantity * price
    url = input("Url = ")
    notes = input("Notes = ")
    unit = input("Unit = ")
    try:
        table.execute(f"INSERT INTO {tables_name} VALUES({id}, '{brand}', '{name}', {quantity}, {price}, {total}, '{url}', '{notes}', '{unit}')")
        print("\nRow added with successs\n")
    except:
        print(f"\nThere was an error\n {exception}\n\n")

#You change the of a specific row by the id
def changeValue(curs):
    name = input("What is the name of the table? ")
    colum = input("What colum is the value that you want to change(brand, name, quantity, value, url, notes, unit)\n")
    change = input("New value = ")
    id = input("What its id : ")
    try: 
        curs.execute(f"UPDATE {name} SET {colum.lower()} = '{change}' WHERE id = {id};")
        print("\nChange made with success\n")
    except:
        print("\nThere is a error. Your value does not macht with the data\n")

#Change any data in the table
def deleteRow(curs):
    table = input("Which table? ")
    id = int(input("What is the id of the item that you want to delete? "))
    an = input("Are you sure??")
    if an.lower() == 'yes':
        try:
            curs.execute(f"DELETE FROM {table} WHERE id = {id};")
        except: 
            print(f"Your item does no exist in the {table}")
    else:
        pass

#Printing the dataTable
def showTable(curs):
    name = input("What is the name of the table?")
    for row in curs.execute(f"SELECT * FROM {name}"):
            print("Tem algo")
            for eachData in row:
                if eachData == "":
                    print("Data Empty")
                    break
                print(f"{eachData}", end=(" " * (5 - len(str(eachData)[-1]))))
            print("\n")


#To be done: add alert if table is empty
#generate ID numbers when making a new row
#Make a loop to ensure that all data types are correct, prompt the user with "this should be a number/word where needed"
#Maybe add try excepts when entering data 
#Show list of tables
