import re
eg_string = 'I am Agnij Biswas. I am from Serampore West Bengal'
eg_str2 = 'I am Agnij Biswas. I am from IIT Kharagpur'

a = re.search('am', eg_string) # a stores a match object in it
print(a.span()) #prints the starting and ending indices of the searched string
print(a.end()) #prints the ending indice
# if the searched string occurs more than once, the first time it occurs is considered by span, end

b = re.compile(eg_str2)
print(b.fullmatch(eg_string))
print(b.match(eg_string))