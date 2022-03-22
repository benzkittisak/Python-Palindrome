import unittest

class Palindrome():
    def check(self,n1):
        for char in n1:
            if char.isdigit():
                return True
        return False

    def palin(self,n1):
        n2 = reversed(n1)
        if list(n1) == list(n2):
            return True
        else : return False

class TestPalindrome(unittest.TestCase):
    def test_checkWord(self):
        myPalin = Palindrome()
        self.assertEqual(myPalin.check("asdqwd56"),True,"Should be True")

    def test_checkWord(self):
        myPalin = Palindrome()
        self.assertEqual(myPalin.check("aslkdqwoehdqiuwh"),False,"Should be False")

    def test_checkPalin(self):
        myPalin = Palindrome()
        self.assertEqual(myPalin.palin("aasswwssaa"),True,"Should be True")

    def test_checkPalin(self):
        myPalin = Palindrome()
        self.assertEqual(myPalin.palin("aslkdqwoehdqiuwh"),False,"Should be False")

if __name__ == '__main__':
    unittest.main()
