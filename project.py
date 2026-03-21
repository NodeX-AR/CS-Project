import mysql.connector as sqlcon
db=sqlcon.connect(
    host='localhost',
    user='root',
    password='<password>', # Change this
    database='library'    # Change this
    )
    
cursor=db.cursor()

def registry():
    cursor.execute("Select * from list")
    data=cursor.fetchall()
    for i in data:
        print(i)

def new():
    n=input("Enter the name of new student:")
    query = "INSERT INTO `list` (student_name) VALUES ('"+ n +"')"
    cursor.execute(query)
    db.commit()
    print("Student",n,"is sucessfully added.")

def breturn():
    n=input("Enter the name of new student:")
    query = "UPDATE `list` SET status = 'Book Returned', book = NULL WHERE student_name = '"+n+"'"
    cursor.execute(query)
    db.commit()
    print("Student",n," has retured the book. Status Updated !")

def issue():
    n=input("Enter the name of new student:")
    query = "SELECT status FROM `list` WHERE student_name = '"+n+"'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result == None:
        print("Student not found.")
        return
    elif result[0] == "Book Issued":
        print("The student",n,"has already been issued a book.")
        return
    b=input("Enter the book name:")
    query = "UPDATE `list` SET status = 'Book Issued', book = '"+b+"' WHERE student_name = '"+n+"'"
    cursor.execute(query)
    db.commit()
    print("Book ",b," issued to ",n," successfully!")

def status():
    n=input("Enter the name of new student:")
    query = "SELECT status,book FROM `list` WHERE student_name = '"+n+"'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result == None:
        print("Student not found.")
    elif result[0] == "Book Issued":
        print("The student",n,"has been issued a book ")
        print("The book issued is ",result[1])
        return
    elif result[0] == "Book Returned":
        print("The student",n,"has already returned the book.")
    else:
        print("The student",n,"has never taken a book.")
      
def main():
    print("+---------------------------------------------------------+")
    print("|               LIBRARY MANAGEMENT SYSTEM                 |")
    while True:
        print("+---------------------------------------------------------+")
        print("|Options :                                                |")
        print("+---------------------------------------------------------+")
        print("|1.Close the system.                                      |")
        print("|2.Show the entire registry.                              |")
        print("|3.Add new student.                                       |")
        print("|4.Return of book.                                        |")
        print("|5.Issue of book.                                         |")
        print("|6.Check the status of a student.                         |")
        print("+---------------------------------------------------------+")
        opt=input("|Enter the option index number :")
        print("+---------------------------------------------------------+")
        if opt == "1" :
            break
        elif opt == "2":
            registry()
        elif opt == "3":
            new()
        elif opt == "4":
            breturn()
        elif opt == "5":
            issue()
        elif opt == "6":
            status()
        else:
            print("Please enter a valid option")
            continue
    print("             Thank You using our program                  |")
    print("+---------------------------------------------------------+")
    db.close()
          
main()
