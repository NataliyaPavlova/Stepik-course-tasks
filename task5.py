'''
Write a recursive function that takes a string and returns True if that string is a palindrome and False othrwise. The function should be case sensitive. Spaces and other special symbols count as well.

'''

def isPalindrome(str):
    return str[0]==str[-1] and isPalindrome(str[1:-1]) if str else True

