class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = 0
        j = 0
        while i < m:
            if j < n:
                if nums1[i] > nums2[j]:
                    temp.append(nums2[j])
                    j += 1
                else:
                    temp.append(nums1[i])
                    i += 1
            else:
                temp.append(nums1[i])
                i += 1
        if i == m:
            while j < n:
                temp.append(nums2[j])
                j += 1
        i = 0
        for num in temp:
            nums1[i] = num
            i += 1