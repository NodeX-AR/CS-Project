# This project is created by Aswanth R
# For any reference or corrections please post and comment of out respo
# Here is link https://github.com/NodeX-AR/CS-Project/
# For better function of script please close with the code of project rather than manual closing !
import mysql.connector as sqlcon

#connection
db=sqlcon.connect(
    host='localhost',
    user='root',
    password='Aswanth@2009', # Change this
    database='mysql'
    )

#checking connection
if db.is_connected() == False:
    print("================== E R R O R =====================")
    print("Please check your connection of MySQL with Python!")
    print("To check your connection please run the connection")
    print("test script given in the same respo and crosscheck")
    print("error code and fix in our respo or google.")
    print("GitHub Respo Link =>")
    print("https://github.com/Nodex-AR/CS-Project")

#checking configs for project   
cursor=db.cursor()
cursor.execute("show databases")
t_db=cursor.fetchall()
configdb = ('library',)
if configdb in t_db:
    print("All Configs already set !")
    cursor.execute("USE library")
    
#doing configs for project   
else:
    print("Please wait till we make changes !")
    cursor.execute("CREATE DATABASE library")
    print("+---------------------------------------------------------+")
    print("| SETIING CONFIGS..........                               |")
    print("+---------------------------------------------------------+")
    print("| [0000000                                      ][ 20 % ] |")
    cursor.execute("USE library")
    print("| [00000000000000000                            ][ 40 % ] |")
    db.commit()
    print("| [0000000000000000000000000                    ][ 60 % ] |")
    cursor.execute("CREATE table list ( student_name Varchar(50) , book Varchar(100) , status Varchar(30)) ")
    print("| [0000000000000000000000000000000              ][ 80 % ] |")
    db.commit()
    print("| [000000000000000000000000000000000000000000000][ 100% ] |")
    
#registry section    
def registry():
    cursor.execute("SELECT * FROM `list`")
    total_students = cursor.fetchall()
    
    cursor.execute("SELECT * FROM `list` WHERE status = 'Book Issued'")
    books_out = cursor.fetchall()
    print("|                 Library Statistics                      |")
    print("+---------------------------------------------------------+")
    print("| Total Registered Students: ",len(total_students))
    print("| Books Currently Issued:    ",len(books_out))
    
#section to add a new student
def new():
    n=input("Enter the name of new student:")
    query = "INSERT INTO `list` (student_name) VALUES (%s)"

    cursor.execute(query,(n,))
    db.commit()
    print("Student",n,"is sucessfully added.")
    
#section to return book
def breturn():
    n=input("Enter the name of new student:")
    query = "UPDATE `list` SET status = 'Book Returned', book = NULL WHERE student_name = %s"
    cursor.execute(query,(n,))
    db.commit()
    print("Student",n," has retured the book. Status Updated !")
    
#section to issue a book
def issue():
    n=input("Enter the name of new student:")
    cursor.execute("SELECT status FROM `list` WHERE student_name = '%s'"%(n))
    result = cursor.fetchone()
    if result is None:
        print("Student not found.")
        return
    

    elif result[0] == "Book Issued":
        print("The student",n,"has already been issued a book.")
        return
    
    b=input("Enter the book name:")
    query = "UPDATE `list` SET status = 'Book Issued', book = %s WHERE student_name = %s"
    cursor.execute(query,(b,n))
    db.commit()
    print("Book",b,"issued to",n,"successfully!")


#section to check the status of a student
def status():
    n=input("Enter the name of new student:")
    query = "SELECT status,book FROM `list` WHERE student_name = %s"
    cursor.execute(query,(n,))
    result = cursor.fetchone()
    if result is None:
        print("Student not found.")
        
    elif result[0] == "Book Issued":
        print("The student",n,"has been issued a book ")
        print("The book issued is ",result[1])
        return
    
    elif result[0] == "Book Returned":
        print("The student",n,"has already returned the book.")
        
    else:
        print("The student",n,"has never taken a book.")
        
#master reset section ! 
def reset():
    ans = input("|Are You Sure About reset [Y/N] :").lower()
    print("+---------------------------------------------------------+")
    if ans == 'y':
        cursor.execute("Drop database library")
        check = cursor.fetchall()
        print("|Reset Protocol Executed Successfully. Now Please restart!|")
        db.commit()
        print("+---------------------------------------------------------+")
    else:
        print("|Exiting Reset Protocol. Please restart this program !    |")
        print("+---------------------------------------------------------+")

#main workflow        
def main():
    print("+---------------------------------------------------------+")
    print("|               LIBRARY MANAGEMENT SYSTEM                 |")
    while True:
        print("+---------------------------------------------------------+")
        print("|Options :                                                |")
        print("+---------------------------------------------------------+")
        print("|1.Issue of book.                                         |")
        print("|2.Show the registry.                                     |")
        print("|3.Add new student.                                       |")
        print("|4.Return of book.                                        |")
        print("|5.Check the status of a student.                         |")
        print("|6.Close the system.                                      |")
        print("|7.Master Reset.                                          |")
        print("+---------------------------------------------------------+")
        opt=input("|Enter the option index number :")
        print("+---------------------------------------------------------+")
        if opt == "1" :
            issue()
        
        elif opt == "2":
            registry()
            
        elif opt == "3":
            new()
            
        elif opt == "4":
            breturn()
            
        elif opt == "5":
            status()

        elif opt == "6":
            break
        
        elif opt == "7":
            reset()
            break
        else:
            print("Please enter a valid option")
            continue
    print("|             Thank You using our program :)              |")
    print("+---------------------------------------------------------+")
    db.close()
    
#start section          
if __name__ == "__main__":
    main()

#Please don't do any change without knowing what your are doing !
