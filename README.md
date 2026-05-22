# Library Management System – CBSE Class 12 CS Project

**Author:** Aswanth R  
**Subject:** Computer Science (Code 083)  

---
[![GitHub stars](https://img.shields.io/github/stars/NodeX-AR/CS-Project?style=social)](https://github.com/NodeX-AR/CS-Project/stargazers)

---  
## License

Educational Use License – see LICENSE file.  
Free for educational and evaluation purposes. Commercial use prohibited.

---

## How to Run

### Step 1 – Test MySQL Connection

1. Edit `connection-test.py` – set your MySQL host, user, password.
2. Run: `python connection-test.py`
3. If you see `✅ Connected successfully!`, go to Step 2.

### Common MySQL Errors

| Error Code | Problem | Fix |
|------------|---------|-----|
| 1045 | Access denied | Check username/password |
| 1049 | Unknown database | Create database or check name |
| 2003 | Cannot connect | Start MySQL/XAMPP |
| 1044 | Access denied to DB | Grant privileges |

### Step 2 – Run Main Project

Run: ```python project.py ```
If that fails, try: ``` py project.py ```

First run creates database `library` and table `list` automatically.

Menu options:
1. Issue book
2. Show registry
3. Add student
4. Return book
5. Check student status
6. Exit
7. Master reset (drops database)

---

## Demo Output (Sample)

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
