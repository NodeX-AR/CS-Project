# CS-Project
This project is owned by Aswanth R.  
This software is **Proprietary and Confidential**. Unauthorized use, distribution, or modification is strictly prohibited.  
# Steps 1
Copy and run `connection-test.py`.  
**Change varibales like  database,user,host and password.**  
Now check for output.  
If successfully connected move to step 2.  
If not, check the error code.  
Here some common error codes and fixes.  
Error | Code      	        | Meaning	What to fix  
1045  |	Access Denied	      | Your user or password is wrong.  
1049  |	Unknown Database	  | The database name you typed doesn't exist in MySQL yet.  
2003  |	Can't connect	      | MySQL server isn't started (Open your XAMPP/MySQL dashboard).  
1044  |	Access denied to DB | The user exists, but doesn't have permission for that specific DB.  
IF THESE DON'T FIX REFER SOME AI AND FIX AND MOVE TO STEP 2.  
# Step 2  
This is main project.  
First go to MySQL and do >>> `Create database library;`  
now do >>>`CREATE TABLE list (id INT NOT NULL AUTO_INCREMENT,student_name VARCHAR(100) NOT NULL,book VARCHAR(100) DEFAULT NULL,status VARCHAR(20) DEFAULT NULL,PRIMARY KEY (id));`   
Now copy and run main.py.  
Once run for first time the program is ready.  
Now for better performance direct to file in cmd   
The cmd for this is `cd /d <the file path>` eg: "cd /d D:\PythonProjects"  
Then do `python project.py` (here file name is project.py)  
If `python project.py` fails do `py project.py`
If program runs smoothly porject is ready.  
If not go back to some AI and fix the problem in connectivity  
Because this code here is error free.  

**This project is proprietary and confidential. See the LICENSE file for full details.**
----------------------------------------------------------------------------------------
This is a output of a example run:

PS C:\Users\ASWANTH> python test.py  
+---------------------------------------------------------+  
|               LIBRARY MANAGEMENT SYSTEM                 |  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :2  
+---------------------------------------------------------+  
(1, 'Aswanth', 'Wings of Fire', 'Book Issued')  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :3  
+---------------------------------------------------------+  
Enter the name of new student:Abhinav  
Student Abhinav is sucessfully added.  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :5  
+---------------------------------------------------------+  
Enter the name of new student:Abhinav  
Enter the book name:Harry Potter  
Book  Harry Potter  issued to  Abhinav  successfully!  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :6  
+---------------------------------------------------------+  
Enter the name of new student:Abhinav  
The student Abhinav has been issued a book  
The book issued is  Harry Potter  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :4  
+---------------------------------------------------------+  
Enter the name of new student:Abhinav  
Student Abhinav  has retured the book. Status Updated !  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :6  
+---------------------------------------------------------+  
Enter the name of new student:Abhinav  
The student Abhinav has already returned the book.  
+---------------------------------------------------------+  
|Options :                                                |  
+---------------------------------------------------------+  
|1.Close the system.                                      |  
|2.Show the entire registry.                              |  
|3.Add new student.                                       |  
|4.Return of book.                                        |  
|5.Issue of book.                                         |  
|6.Check the status of a student.                         |  
+---------------------------------------------------------+  
|Enter the option index number :1  
+---------------------------------------------------------+  
             Thank You using our program                  |  
+---------------------------------------------------------+  
