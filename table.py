import sqlite3
import functions

#Creating the connection between python the sqlite
con = sqlite3.connect('data.db')
cur = con.cursor()

#Menu
while True:
    #con.commit() #Save the Datatable
    print("( 1 ) Create a Table \n( 2 ) Add another row \n( 3 ) Change Value \n( 4 ) Show table \n( 5 ) Create a CSV file or uptade \n( 99 ) Exit")
    question = int(input(""))
    if question == 1:
        functions.createTABLE(cur)
    elif question == 2:
        functions.addRow(cur)
    elif question == 3:
        functions.changeValue(cur)
    elif question == 4:
        functions.showTable(cur)
    elif question == 5:
        functions.createCSV(cur)
    elif question == 99:
        con.close() # Close the Datatable and your will have to open again
    else:
        pass

    con.commit() #Save the Datatable
