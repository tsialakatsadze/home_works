
import unittest

from main import Calculator
class TestCalculator(unittest.TestCase):
    def test_celsius_to_fahrenheit_equal(self):
        calc = Calculator()
        self.assertEqual(calc.celsius_to_fahrenheit(5), 41)
        self.assertEqual(calc.celsius_to_fahrenheit(15), 59)
    def test_celsius_to_fahrenheit_not_equal(self):
        calc = Calculator()
        self.assertNotEqual(calc.celsius_to_fahrenheit(5), 40)
        self.assertNotEqual(calc.celsius_to_fahrenheit(15), 60)
    def test_fahrenheit_to_celsius_equal(self):
        calc = Calculator()
        self.assertEqual(calc.fahrenheit_to_celsius(41), 5)
        self.assertEqual(calc.fahrenheit_to_celsius(59), 15)
    def test_fahrenheit_to_celsius_not_equal(self):
        calc = Calculator()
        self.assertNotEqual(calc.fahrenheit_to_celsius(5), 40)
        self.assertNotEqual(calc.fahrenheit_to_celsius(15), 60)
    def test_reverse_string_equal(self):
        calc = Calculator()
        self.assertEqual(calc.reverse_string("1234"),"4321")
        self.assertEqual(calc.reverse_string("abcd"), "dcba")
    def test_reverse_string_not_equal(self):
        calc = Calculator()
        self.assertNotEqual(calc.reverse_string("267"),"763")
        self.assertNotEqual(calc.reverse_string("abc"), "bcb")
    def test_is_palindrome_equal(self):
        calc = Calculator()
        self.assertEqual(calc.is_palindrome("123454321"),'It is a palindrome')
        self.assertEqual(calc.is_palindrome("abcdcba"),'It is a palindrome')
    def test_is_palindrome_not_equal(self):
        calc = Calculator()
        self.assertNotEqual(calc.is_palindrome("456787654"),'It is not a palindrome')
        self.assertNotEqual(calc.is_palindrome("abccba"),'It is not a palindrome')
    def test_capitalize_words_equal(self):
        calc = Calculator()
        self.assertEqual(calc.capitalize_words("i"),'I')
        self.assertEqual(calc.capitalize_words("m"),'M')
    def test_capitalize_words_not_equal(self):
        calc = Calculator()
        self.assertNotEqual(calc.capitalize_words("i"),'J')
        self.assertNotEqual(calc.capitalize_words("k"),'k')
    
