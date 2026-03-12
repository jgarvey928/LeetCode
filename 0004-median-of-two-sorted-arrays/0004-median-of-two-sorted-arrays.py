class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        # Binary search on the smaller array
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases by assigning -infinity or infinity when the partition is at the ends
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total length is even, median is the average of the two middle elements
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # If the total length is odd, median is the maximum of the left half
                else:
                    return float(max(maxLeft1, maxLeft2))
            
            # If maxLeft1 is too large, we need to move the partition to the left
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            # Otherwise, move the partition to the right
            else:
                left = partition1 + 1