class Solution(object):
    def isPalindrome(self, x):

        temp = x
        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        
        return temp == rev



        """
        :type x: int
        :rtype: bool
        """
        