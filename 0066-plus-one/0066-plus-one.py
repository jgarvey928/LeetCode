class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        size = len(digits) - 1
        while True:
            if size == -1:
                digits = [1] + digits
                return digits
            num = digits[size]
            if num != 9 :
                digits[size] = num + 1
                return digits
            else :
                digits[size] = 0
            size = size - 1




