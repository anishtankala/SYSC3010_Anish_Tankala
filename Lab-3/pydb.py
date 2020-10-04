import sqlite3

#connect to database file

dbconnect = sqlite3.connect("mydatabase.db");

#If we want to access columns by name we need to set

#row_factory to sqlite3.Row class

dbconnect.row_factory = sqlite3.Row;

#now we create a cursor to work with db

cursor = dbconnect.cursor();

#execute insert statement

cursor.execute('''insert into temps values (date('now'), time('now'), "kitchen", 22.7)''');

dbconnect.commit();

#execute simple select statement

cursor.execute('SELECT * FROM temps');

#print data

for row in cursor:

    print(row['tdate'],row['ttime'],row['zone'],row['temperature']);

#close the connection

dbconnect.close();
