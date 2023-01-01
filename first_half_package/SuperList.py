class SuperList(list):
   def __len__(self):
        return 1000

sl1 = SuperList([1,2,3,4,5])
sl1.append(50)
print(len(sl1))
print(sl1)
