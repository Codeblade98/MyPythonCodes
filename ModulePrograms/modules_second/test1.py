import unittest
import main1

class TestMain1(unittest.TestCase):
    
    def setUp(self):
        print('A function is being tested')

    #if we name a function setUp, it is executed before each unit test

    def test_main1(self):
        test_arr = []
        for case in range(4):
            test_num = input('Enter Test case for test1 ')
            test_arr.append(test_num)
        a,b,c,d = test_arr
        result = main1.fun_test(a,b,c,d)
        self.assertEqual(result,4)
        
        
    def test2_main1(self):
        test_arr = []
        for case in range(4):
            test_num = input('Enter Test case for test2 ')
            test_arr.append(test_num)
        a,b,c,d = test_arr
        result = main1.fun_test(a,b,c,d)
        self.assertIsInstance(result, ValueError)
    
    def tearDown(self):
        print('Cleaning everything up')



if __name__ == '__main__':
    unittest.main()