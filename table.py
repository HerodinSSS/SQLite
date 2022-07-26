import sqlite3, functions

con = sqlite3.connect('dataTable.db')
cur = con.cursor()

#Creating a DataTable
#function.createTABLE(cur)

#functions.insertColumn(cur)

#csv 
functions.createCSV(cur)

#Showing the table
#functions.showTable(cur)

#Saving
con.commit()

#Closing the aplication
con.close()