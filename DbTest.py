import mysql.connector

#Making database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="user_registration" #Database name on localhost
)
mycursor = mydb.cursor()


# funtion to Create user
def adduser():
    count = int(input("Enter number of users do you want to insert"))
    for x in range(count):
        print("User Number %s" % x)
        user = input("Enter Username:  ")
        fName = input("Enter First Name:  ")
        lName = input("Enter Last Name:  ")
        address = input("Enter Address:  ")
        pas = input("Enter Password:  ")
        sql = "INSERT INTO user (Username, Firstname, Lastname, address, Password) VALUES (%s, %s,%s, %s,%s)"
        val = (user, fName, lName, address, pas)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        count += 1


# funtion to view user table
def viewUser():
    mycursor.execute("SELECT * FROM user ")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


# funtion to update a user address
def updateUser():

    username = input("Enter username you want to update: ")
    address = input("Enter new address: ")
    sql = "UPDATE user SET address = %s WHERE Username = %s"
    val = (address, username)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


# function to delete a user by username
def deleteUser(user):

    sql = "DELETE FROM user WHERE Username = %s"
    val = (user,)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

viewUser()