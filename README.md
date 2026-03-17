Q 1. Grade Checker 
Step 1: Getting User Input
I started by using the input() function to ask the user for their marks. Since input usually comes in as text, I wrapped it in int() so Python can treat it as a number for the math.

Code: marks = int(input('Enter your marks \n'))

Step 2: Sorting Grades with if-elif
I created a series of checks. If the first condition isn't met, it moves to the next elif. If the marks are below 60, the else block triggers. 
I used elif so the program stops checking as soon as it finds the right grade, which makes the code more efficient.

Output 1 : 
Enter your marks 
95
your grade is:  A

Output 2 :
Enter your marks 
55
your grade is:  Fail
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q 2. Student Grades
Step 1: Creating the Catalogue
I used a dictionary called catlogue to store the student data. I like using dictionaries for this because they let you link a specific "Key" (the name) to a "Value" (the grade).

Initial List: I started with a few names like Yash and Harsh.

Step 2: Checking for Existing Names
I wrote an if-else block to handle the input. If the name is already in my catlogue, the script updates their grade. If the name is new, it just adds them as a new entry. This keeps my data organized without having the same person listed twice.

Output 1 : 
Initial catalogue: {'Yash': 'A', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C'}
Enter the name of the student 
Yash
Enter the grade of the student 
A+
Updated catalogue: {'Yash': 'A+', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C'}
{'Yash': 'A+', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C'}

Output 2 : 
Initial catalogue: {'Yash': 'A', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C'}
Enter the name of the student 
Vayu
Enter the grade of the student 
F
Catalogue with new entry: {'Yash': 'A', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C', 'Vayu': 'F'}
{'Yash': 'A', 'harsh': 'A+', 'Mansi': 'A+', 'Rohit': 'B', 'Rahul': 'C', 'Vayu': 'F'}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q 3. Write to a File
Step 1: Opening the file in Write mode
I used the open() function to create a new text file called 03_Zdata.txt. I added the 'w' flag, which tells Python I want to "write" to the file. This mode is useful because it creates the file automatically if it doesn't exist yet.

Code: f = open('03_Zdata.txt' , 'w')

Step 2: Adding content and closing
I used the f.write() method to save a string of text inside the file. After writing, I made sure to use f.close() to save my progress. Closing the file is a good habit because it prevents data loss and stops the program from using up extra memory.

Code: f.write("This is a new line.")

Code: f.close()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q 4. Read from a File
Step 1: Accessing the file
For this task, I used the open() function again, but this time I used the 'r' flag for "read" mode. I targeted the file 04_zdata.txt to pull the information I saved earlier.

Code: f = open('04_zdata.txt' , 'r')

Step 2: Displaying the content
I used the f.read() method to grab all the text inside the file and stored it in a variable called data. Finally, I used a print() statement to display that data in the terminal and closed the file to keep things clean.

Code: data = f.read()

Code: print(data)

Output : 
<--DevOpsChat-->

Firsguy : hii
Secondguy : hello

This is a new line added to the file.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
