import sqlite3, functions

con = sqlite3.connect('dataTable.db')
cur = con.cursor()

#Menu
while True:
    print("( 1 ) Create a Table \n( 2 ) Create a new Colum \n( 3 ) Create a CSV file or uptade \n( 4 ) Add another row \n( 5 ) NONE \n( 6 ) Show table")
    question = int(input(""))
    if question == 1:
        functions.createTABLE(cur)
    elif question == 2:
        functions.crateColumn(cur)
    elif question == 3:
        functions.createCSV(cur)
    elif question == 4:
        functions.addRow(cur)
    elif question == 5:
        pass
    elif question == 6:
        functions.showTable(cur)
    else:
        pass

#Saving
con.commit()

#Closing the aplication
con.close()