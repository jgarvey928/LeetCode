class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indxs = []
        size = len(nums)
        for i in range(size):
            if nums[i] != val:
                indxs.append(i)
        k = len(indxs)
        for i in range(k):
            nums[i] = nums[indxs[i]]
        return k
        