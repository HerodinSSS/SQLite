import csv

#Creates a DataTable
def createTABLE(curs):
    curs.execute(f"""CREATE TABLE test
                                        (id integer, brand test, name text, quantity integer, price integer, total real, url text, notes text, unit text)""")

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

    """table = input("What is the table's name that you want to add another row? ")
    brand = input("Brand = ")
    item = input("Item = ")
    quantity = input("Quantity = ")
    price = int(input("Price = "))
    total = int(quantity) * price # The total is the total price of the item (item x price = total)
    url = input("URL = ")
    note = input("Note =  ")
    table.execute(f"INSERT INTO {table} VALUES('{brand}', '{item}', '{quantity}', {price}, {total}, '{url}', '{note}')")"""

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
    table = input("Which table? ")
    for row in curs.execute(f"SELECT * FROM {table}"):
        for eachData in row:
            print(f"{eachData}", end=(" " * (5 - len(str(eachData)[-1]))))
        print("\n")