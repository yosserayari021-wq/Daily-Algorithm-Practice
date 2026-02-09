class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        original_num = x
        reverse_digit = 0
        
        while x > 0:
            last_digit = x % 10
            reverse_digit = reverse_digit * 10 + last_digit
            x = x // 10
        
        return original_num == reverse_digit
        