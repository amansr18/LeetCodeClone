import unittest
from solution import *
import random
import string



class TestNthFibonacci(unittest.TestCase):
    def test_zero(self):
        """Test for n = 0"""
        self.assertEqual(nth_fib(0), 0)

    def test_one(self):
        """Test for n = 1"""
        self.assertEqual(nth_fib(1), 1)

    def test_positive(self):
        """Test for positive values of n"""
        self.assertEqual(nth_fib(2), 1)
        self.assertEqual(nth_fib(3), 2)
        self.assertEqual(nth_fib(4), 3)
        self.assertEqual(nth_fib(5), 5)
        self.assertEqual(nth_fib(6), 8)
        # Add more test cases as needed

def correct_palindrome(string):
	new_str = ""
	for i in string:
		if i.isalnum():
			new_str += (i)
	return new_str.lower()[::-1] == new_str.lower()



class PalindromeChecker(unittest.TestCase):
    def test_1(self):
        """Test for palindrome when input is 'eye'"""
        self.assertTrue(palindrome("eye"))

    def test_2(self):
        """Test for palindrome when input is '_eye'"""
        self.assertTrue(palindrome("_eye"))

    def test_3(self):
        """Test for palindrome when input is 'race car'"""
        self.assertTrue(palindrome("race car"))

    def test_4(self):
        """Test for palindrome when input is 'not a palindrome'"""
        self.assertFalse(palindrome("not a palindrome"))

    def test_5(self):
        """Test for palindrome when input is 'A man, a plan, a canal. Panama'"""
        self.assertTrue(palindrome("A man, a plan, a canal. Panama"))

    def test_6(self):
        """Test for palindrome when input is 'never odd or even'"""
        self.assertTrue(palindrome("never odd or even"))

    def test_7(self):
        """Test for palindrome when input is 'nope'"""
        self.assertFalse(palindrome("nope"))

    def test_8(self):
        """Test for palindrome when input is 'almostomla'"""
        self.assertFalse(palindrome("almostomla"))

    def test_9(self):
        """Test for palindrome when input is 'My age is 0, 0 si ega ym.'"""
        self.assertTrue(palindrome("My age is 0, 0 si ega ym."))

class CountingTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.failures_count = 0

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failures_count += 1


if __name__ == "__main__":
    unittest.main()
    
    
