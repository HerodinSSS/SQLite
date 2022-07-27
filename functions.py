import csv

#Creates a DataTable
def createTABLE(curs):
    name = input("What is the name of the Table: ")
    coname = input("What is the name of the name of the first column: ")
    typ = input("INTEGER: REAL: TEXT: BLOB: ")
    curs.execute(f"""CREATE TABLE {name}({coname}{typ.upper()})""")

#Create a Column
def crateColumn(curs):
    table = input("What is the table tha you want to add a Column?")
    colmn = input("What is the name of the column: ")
    typ = input("INTEGER: REAL: TEXT: BLOB: ")
    curs.execute(f"ALTER TABLE {table} ADD COLUMN {colmn}{typ}")

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
    table = input("What is the table's name that you want to add another row? ")
    brand = input("Brand = ")
    item = input("Item = ")
    quantity = input("Quantity = ")
    price = int(input("Price = "))
    total = int(quantity) * price # The total is the total price of the item (item x price = total)
    url = input("URL = ")
    id = int(input("ID = "))
    note = input("Note =  ")
    table.execute(f"INSERT INTO {table} VALUES('{brand}', '{item}', '{quantity}', {price}, {total}, '{url}', '{note}', {id})")

#Change any data in the table
def deleteRow(table):
    table = input("Which table? ")
    item = input("What is the name of the item that you want to delete? ")
    try:
        table.execute(f"DELETE FROM {table} WHERE Brand = {item};")
    except: 
        print(f"Your item does no exist in the {table}")

#Printing the dataTable
def showTable(table):
    table = input("Which table? ")
    for row in table.execute(f"SELECT * FROM {table}"):
        for eachData in row:
            print(f"{eachData}", end=(" " * (5 - len(str(eachData)[-1]))))
        print("\n")