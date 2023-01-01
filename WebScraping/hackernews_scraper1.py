import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

# Response of 200 means that everything is ok(More reasearch required)
# we can get the HTML content using response.text

b1 = BeautifulSoup(response.text, 'html.parser')

# we can do b1.body to get the  first body tag that comes up
# similarly we can do b1.a to get the first a tag(for hyperlink) that comes up
# it can be also done by using .find()
# we can use .findall() to find something

print(b1.find('a'))
print(b1.find_all('head'))

# We can use .select to select on basis of css selectors(eg: tags, .classes, #ids etc.)

print(b1.select('.score'))
print(b1.select('#score_33395121'))

print(b1.select('.title'))
