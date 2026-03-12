class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign
        sign = -1 if x < 0 else 1
        
        # Get the absolute value, convert to string, reverse it, and convert back to integer
        reversed_x = int(str(abs(x))[::-1]) * sign
        
        # Check if the reversed integer goes outside the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
            
        return reversed_x