# 4. Read from a File
# We used open in read mode and file.read to read and print to display.

# Solution -->
f = open('04_zdata.txt' , 'r')

data = f.read()
print(data)
f.close()