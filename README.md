# mysql_test
CRUD operations in python with MySQL

# Making database connection 
Made connection with database called "user_registration"

in connected database I have table call "user"

before functions I made a DBConnection cursor name "mycursor" 

# funtion to Create user
In this function will ask user to input information in user table but before that it will ask for number of users you want to insert.
Then i just used insert query and pass it to the db using commit function (in a loop)

# funtion to view user table
This function simply just run a select query and fatch all the information from table
and print the record

# funtion to update a user address
In this function 
