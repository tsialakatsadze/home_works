
class Calculator:

    def reverse_string(self,s):
        return s[::-1]

    def is_palindrome(self,s):
        if s == s[::-1]:
            return 'It is a palindrome'
        else:
            return 'It is not a palindrome'
    def capitalize_words(self,s):
        return ' '.join(word.capitalize() for word in s.split())

    def celsius_to_fahrenheit(self, c):
        return c * 9 / 5 + 32

    def fahrenheit_to_celsius(self,f):
        return (f - 32) * 5 / 9