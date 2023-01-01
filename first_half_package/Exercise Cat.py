class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def play(self):
        print(f'CAT PURR : \' I am of age {self.age}\' ') #this func was not in question but done as practice
    
        
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

def find_oldest(age_list = []):
    copy = age_list.copy()
    copy.sort()
    return copy[2]

name_list = []
age_list = []

for cat_number in range(1,4):
    name = input(f'Enter the name of cat number {cat_number} ')
    age = input(f'Enter the age of cat number {cat_number} ')
    name_list.append(name)
    age_list.append(age)

cat1 = Cat(name_list[0], age_list[0])
cat2 = Cat(name_list[1], age_list[1])
cat3 = Cat(name_list[2], age_list[2])

oldest_cat_age = find_oldest(age_list)
print(f'The oldest cat is {oldest_cat_age} years old')