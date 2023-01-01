import sys

print('Run succesful')
print(sys.argv[0]) #argv[0] is always the file name
print(sys.argv[1]) #first word after file name
print(sys.argv[2]) #second word after file name(separated by spaces)

#if we had only one word then we would get an index error 
#if the code does not run, save the file and run again