import pymysql
import cgi
import sys

connection = pymysql.connect(host='localhost', user='root',
                             password='pass', db='bank_system',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
'''
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : {} ".format(data)) '''

'''
Queries :
          1. Select * from TableName
          2. insert into TableName values ( Column1_Value, Column2_Value, Column3_Value, Column4_Value, .....)
          3. create table TableName (Column1 datatype(size), Column2 datatype(size), Column3 datatype(size), ....)
          4. select ColumnName from TableName where ColumnName = ColumnNameValue
          5. DELETE FROM table_name [WHERE Clause]

          Sample : select FirstName, LastName from Persons where city = 'kharagpur'
'''
##ques 1.Select all the columns from actor table.
##ques 2.Insert into category
##sql = "insert into category values(17, 'ISE', NOW())"
##ques 3.Count the number of each rental_duration where the count is more than 200.
##sql = "select count(*) as c, rental_duration from sakila.film group by rental_duration having c > 200"
##ques 4.Find out the list of English movies...Hint: Film, Language....(using joining).
##sql = "select * from film as f join sakila.language as l on f.language_id = l.language_id where l.name = 'English'"
##ques 4 using nested query.
##sql = "select * from film where language_id in (select language_id from sakila.language as l where l.name like 'Eng%')"



query1 = "SELECT name from customer WHERE customer_id IN (SELECT customer_id FROM account WHERE branch_id=8 HAVING count(DISTINCT branch_id) = 1);"
query2 = "SELECT name from customer WHERE customer_id IN (SELECT DISTINCT customer_id FROM account WHERE customer_id NOT IN (SELECT customer_id from account WHERE account_id IN (SELECT account_id FROM loan)));"
query3 = "SELECT MIN(balance), MAX(balance), AVG(balance), SUM(balance) from account WHERE customer_id IN (SELECT customer_id from customer WHERE name='Dhiraj Barnwal');"
query4 = "SELECT name from customer WHERE customer_id IN (SELECT customer_id from account WHERE account_id IN (SELECT account_id from loan WHERE account_id IN (SELECT account_id from account WHERE branch_id IN (SELECT branch_id from branch WHERE bank_id IN (SELECT bank_id from bank WHERE bank_name='Citi Bank')))));"
query5 = "SELECT bank_name from bank WHERE bank_id NOT IN (SELECT bank_id from branch WHERE address!='XYZ');"

print("Select one of the options below\n")
print("1. Find all customers who have only one account at a specific branch.\n2. Find all customers who have an account at the bank, but do not have any loan.\n3. Find minimum, maximum, average, and total balance of a specific customer.\n4. Find the details of the customer having loan in a specific bank.\n5. Find the banks not having any branch at a specific location. ")

cont = 'Y'

while(cont=='Y' or cont=='y'):
    try:
        choice = int(input("\nEnter your choice\n"))
    except:
        print("Please input an integer. Closing!!!")
        sys.exit()

    if choice == 1:
        cursor.execute(query1)
        result = cursor.fetchall()
        fields = cursor.description
        i = 1
        print("\nSl No.     Name\n")
        for res in result:
            print(i, "   \t", res["name"])
            print("\n")
            i = i + 1
    elif choice == 2:
        cursor.execute(query2)
        result = cursor.fetchall()
        fields = cursor.description
        i = 1
        print("\nSl No.     Name\n")
        for res in result:
            print(i, "   \t", res["name"])
            print("\n")
            i = i + 1
    elif choice == 3:
        cursor.execute(query3)
        result = cursor.fetchall()
        fields = cursor.description
        i = 1
        for res in result:
            for i in res:
                print(i, res[i])
            print("\n")
    elif choice == 4:
        cursor.execute(query4)
        result = cursor.fetchall()
        fields = cursor.description
        i = 1
        print("\nSl No.     Name\n")
        for res in result:
            print(i, "   \t", res["name"])
            print("\n")
            i = i + 1
    elif choice == 5:
        cursor.execute(query5)
        result = cursor.fetchall()
        fields = cursor.description
        i = 1
        print("\nSl No.     Bank Name\n")
        for res in result:
            print(i, "   \t", res["bank_name"])
            i = i + 1
    else:
        print("Invalid choice!!!!\n")
    cont = input("Do you want to continue? Press Y for yes\n")

##connection.commit()
cursor.close()
connection.close()
