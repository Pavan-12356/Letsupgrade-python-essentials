import sympy

def checkPrimeNumber(num):
    if sympy.isprime(num):
        return num
    else:
        return("No Prime")
%%writefile check_pri.py
import sympy
'''
Module to check prime Number
'''
def checkPrimeNumber(num):
    '''
    Function to Check Prime takes a Input
    '''
    if sympy.isprime(num):
        '''
        if statement
        '''
        return num
    else:
        return "No Prime"




%%writefile check_prime.py
import unittest 
import check_pri

class TestPrime(unittest.TestCase):
    def checkprimeNumber(self):
        num = 7
        result = chPrime.checkPrimeNumber(num)
        self.assertEqual(result,num)

    def checkNotPrimenumber(self):
        num= 8
        result = chPrime.checkPrimeNumber(num)
        self.assertEqual(result,"No Prime")

if __name__ == "__main__":
    unittest.main()
