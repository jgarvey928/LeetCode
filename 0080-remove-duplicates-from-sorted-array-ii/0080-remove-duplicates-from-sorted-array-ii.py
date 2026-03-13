class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # 'slow' points to the index where the next valid element should be placed
        slow = 2
        
        # 'fast' scans through the array starting from the third element
        for fast in range(2, len(nums)):
            # If the current element is different from the element 
            # two positions before the current 'slow' pointer, it's valid.
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
                
        return slow