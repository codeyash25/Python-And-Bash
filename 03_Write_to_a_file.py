# 3.Write to a File
# Write a program to create a text file and write some content to it.

# Using file functions like write and open.

# Solution -->
f = open('03_Zdata.txt' , 'w')
f.write("This is a new lines.")
f.close()