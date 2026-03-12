class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for ind1 in range(len(nums)):
            for ind2 in range(1,len(nums)):
                if nums[ind1] + nums[ind2] == target and ind1 != ind2:
                    return [ind1, ind2]