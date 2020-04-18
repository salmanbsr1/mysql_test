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
In this function i am using set query to update address, we can update whole record or any other record by username.
i am taking input for username and address from user

# function to delete a user
In my delete function i am using delete query which will delete record according to username since that is our unique key
i am taking imput for username from user 
