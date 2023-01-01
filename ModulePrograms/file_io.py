my_file = open('test.txt')
print(my_file) 
print(my_file.read()) #here we read what is in the file 
print(my_file.read()) #this time we read nothing due to cursor being at end
my_file.seek(0) #moves cursor to desired index. If we do print(my_file.seek(<index number>)), the index number is printed
print(my_file.read()) #now we again get the full text
my_file.seek(0)
print(my_file.readline()) #reads only one line from where the cursor is present
print(my_file.readline())
#if we do my_file.readline() again the 2nd line is printed

my_file.seek(0)
print(my_file.readlines()) #reads as a list, each line is a member of the list

# if we do enter it is printed as /n
# if in the file the cursor is moved to the next line we get a /n in the last line text

my_file.close() #closes the file