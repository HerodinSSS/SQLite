import csv

#Creates a DataTable
def createTABLE(curs):
    name = input("What is the name of the Table: ")
    coname = input("What is the name of the name of the first column: ")
    type = input("Type of the first row: ")
    curs.execute(f"""CREATE TABLE {name}({coname}{type})""")

#Create a new file
def insertColumn(curs):
    colmn = input("What is the name of the column: ")
    typ = input("INTEGER: REAL: TEXT: BLOB: ")
    curs.execute(f"ALTER TABLE inventory ADD COLUMN {colmn}{typ}")

#Create a CSV file
def createCSV(curs):
    with open('data.csv', 'w') as csvfile:
        filewrite = csv.writer(csvfile, delimiter=',')
        for row in curs.execute("SELECT * FROM inventory"):
            li = []
            li.clear()
            li.append(str(row))
            filewrite.writerow(row)




#Adds another row
def adds(table):
    brand = input("Brand = ")
    item = input("Item = ")
    quantity = input("Quantity = ")
    price = int(input("Price = "))
    total = int(quantity) * price # The total is the total price of the item (item x price = total)
    url = input("URL = ")
    id = int(input("ID = "))
    note = input("Note =  ")
    table.execute(f"INSERT INTO inventory VALUES('{brand}', '{item}', '{quantity}', {price}, {total}, '{url}', '{note}', {id})")


#Printing the dataTable
def showTable(table):
    for row in table.execute("SELECT * FROM inventory"):
        for eachData in row:
            print(f"{eachData}", end=(" " * (5 - len(str(eachData)[-1]))))
        print("\n")