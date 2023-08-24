

def dbconnection():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="gunjan@091099",
        database="emp_management")
    mycursor = mydb.cursor()
    return mydb, mycursor

