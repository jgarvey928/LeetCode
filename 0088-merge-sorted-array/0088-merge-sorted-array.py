class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1, nums2, and the placement position in nums1
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        # (If p1 < 0, elements in nums1 are already in their correct place)
        nums1[:p2 + 1] = nums2[:p2 + 1]