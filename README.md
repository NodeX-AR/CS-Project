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
First copy and run main.py.  
Once run for first time the program is ready.  
Now for better performance direct to file in powershell or cmd.     
The cmd for this is `cd <the file path>` eg: "cd D:\PythonProjects"  
Then do `python project.py` (here file name is project.py)  
If `python project.py` fails do `py project.py`
If they above way don't work you can manually run the program.
If program runs smoothly porject is ready.  
If not go back to some AI and fix the problem in connectivity  
Because this code here is error free.  

**This project is proprietary and confidential. See the LICENSE file for full details.**
----------------------------------------------------------------------------------------
## Library Management System - Demo Output

```bash
PS C:\Users\ASWANTH> python "project cs.py"
All Configs already set !
+---------------------------------------------------------+
|               LIBRARY MANAGEMENT SYSTEM                 |
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :1
+---------------------------------------------------------+
Enter the name of new student:Aswanth
Enter the book name:Wings of Fire
Book Wings of Fire issued to Aswanth successfully!
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :2
+---------------------------------------------------------+
|                 Library Statistics                      |
+---------------------------------------------------------+
| Total Registered Students:  1
| Books Currently Issued:     1
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :3
+---------------------------------------------------------+
Enter the name of new student:Abhinav
Student Abhinav is sucessfully added.
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :4
+---------------------------------------------------------+
Enter the name of new student:Aswanth
Student Aswanth has retured the book. Status Updated !
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :5
+---------------------------------------------------------+
Enter the name of new student:Aswanth
The student Aswanth has already returned the book.
+---------------------------------------------------------+
|Options :                                                |
+---------------------------------------------------------+
|1.Issue of book.                                         |
|2.Show the registry.                                     |
|3.Add new student.                                       |
|4.Return of book.                                        |
|5.Check the status of a student.                         |
|6.Close the system.                                      |
|7.Master Reset.                                          |
+---------------------------------------------------------+
|Enter the option index number :6
+---------------------------------------------------------+
|             Thank You using our program :)              |
+---------------------------------------------------------+
```
