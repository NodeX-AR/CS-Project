# CS-Project
This project is owned by Aswanth R.  
This software is **Proprietary and Confidential**. Unauthorized use, distribution, or modification is strictly prohibited.  
# Steps 1
Copy and run `connection-test.py`.  
**Change varibales like user,host and password.**  
## Do not change the databse !  
Now check for output.  
If successfully connected move to step 2.  
If not, check the error code.  
## 🔧 Common MySQL Error Codes & Solutions

```bash
┌────────────┬─────────────────────┬──────────────────────────────────┐
│ Error Code │ Error               │ What to Fix                      │
├────────────┼─────────────────────┼──────────────────────────────────┤
│ 1045       │ Access Denied       │ ❌ Wrong username/password       │
│            │                     │ ✅ Check MySQL credentials       │
├────────────┼─────────────────────┼──────────────────────────────────┤
│ 1049       │ Unknown Database    │ ❌ Database doesn't exist        │
│            │                     │ ✅ Create DB or check name       │
├────────────┼─────────────────────┼──────────────────────────────────┤
│ 2003       │ Can't connect       │ ❌ MySQL server not running      │
│            │                     │ ✅ Start XAMPP/MySQL daemon      │
├────────────┼─────────────────────┼──────────────────────────────────┤
│ 1044       │ Access denied to DB │ ❌ User lacks DB privileges      │
│            │                     │ ✅ Grant permissions to user     │
└────────────┴─────────────────────┴──────────────────────────────────┘
```
IF THESE DON'T FIX REFER SOME AI AND FIX AND MOVE TO STEP 2.  
# Step 2  
This is main project.  
First copy and run main.py.  
Once run for first time the program is ready.  
Now for better performance direct to file in powershell or cmd.     
The cmd for this is `cd dir <the file path>` eg: "cd dir D:\PythonProjects"  
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
