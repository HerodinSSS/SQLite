import csv

#Creates a DataTable
def createTABLE(curs):
    try:
        curs.execute(f"""CREATE TABLE test
                                        (id integer, brand test, name text, quantity integer, price integer, total real, url text, notes text, unit text)""")
    except:
        print("You already have this data table")

#Create a Column
def crateColumn(curs):
    table = input("What is the table tha you want to add a Column?")
    colmn = input("What is the name of the column: ")
    typ = input("INTEGER: REAL: TEXT: BLOB: ")
    curs.execute(f"ALTER TABLE test ADD COLUMN {colmn} {typ}")



#Create a CSV file
def createCSV(curs):
    table = input("What is the name of the table that you want create a csv file with? ")
    with open('data.csv', 'w') as csvfile:
        filewrite = csv.writer(csvfile, delimiter=',')
        for row in curs.execute(f"SELECT * FROM {table}"):
            li = []
            li.clear()
            li.append(row)
            filewrite.writerow(row)

#Adds another row
def addRow(table):
    id = int(input("Id = "))
    brand = input("Brand = ")
    name = input("Name = ")
    quantity = int(input("Quantity = "))
    price = int(input("Price = "))
    total = quantity * price
    url = input("Url = ")
    notes = input("Notes = ")
    unit = input("Unit = ")
    table.execute(f"INSERT INTO test VALUES({id}, '{brand}', '{name}', {quantity}, {price}, {total}, '{url}', '{notes}', '{unit}')")

# You change the of a specific row by the id number
def changeValue(curs):
    colum = input("What colum is the value that you want to change(brand, name, quantity, value, url, notes, unit)\n")
    change = input("New value = ")
    id = input("What its id : ")
    try: 
        curs.execute(f"UPDATE test SET {colum.lower()} = '{change}' WHERE id = {id};")
    except:
        print("There is a error. Your value does not macht with the data.")

#Change any data in the table
def deleteRow(curs):
    table = input("Which table? ")
    item = input("What is the name of the item that you want to delete? ")
    try:
        curs.execute(f"DELETE FROM {table} WHERE Brand = {item};")
    except: 
        print(f"Your item does no exist in the {table}")

#Printing the dataTable
def showTable(curs):
    for row in curs.execute(f"SELECT * FROM test"):
        for eachData in row:
            print(f"{eachData}", end=(" " * (5 - len(str(eachData)[-1]))))
        print("\n")