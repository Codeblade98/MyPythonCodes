class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

    ''' The __iter__() function returns an iterator for the given object'''

    #It creates an object that can be accessed one element at a time using __next__() function, 
    # which generally comes in handy when dealing with loops

  def __next__(self): #The __next__() method must return the next item in the sequence
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration #for takes StopIteration error and causes an exception so we do not get an error

gen = MyGen(1,100)
for i in gen:
    print(i)

    