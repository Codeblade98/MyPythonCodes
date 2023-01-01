import unittest
from random_game import num_checker

class Testing(unittest.TestCase):
   
    def test_num_checker1(self):
        start = 'Agnij'
        end = 1
        num = 'Python'
        result = num_checker(num,start,end)
        self.assertIsInstance(result,ValueError)

    def test_num_checker2(self):
        start = 10
        end = 1
        num = 2
        result = num_checker(num,start,end)
        self.assertIsInstance(result,ValueError) #empty range error is a type of ValueError

    def test_num_checker2(self):
        start = None
        end = 1
        num = 2
        result = num_checker(num,start,end)
        self.assertIsInstance(result,TypeError)

if __name__ == '__main__':
    unittest.main()