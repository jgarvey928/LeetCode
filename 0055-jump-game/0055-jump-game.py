class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # print(len(nums))
        # print(nums[0])
        # print(nums[::-1])
        flipped = nums[::-1]
        flipped = flipped[1:]
        # print(flipped)
        reach = len(nums) - 1
        i = reach - 1
        for num in flipped:
            # print("reach: "+str(reach))
            # print("index: "+str(i) + " num: "+str(num))
            # print( str(i) +" " +str(num))
            if i + num >= reach:
                reach = i
                # print("reachNow: "+str(reach))
            i -=1
        if reach == 0:
            return True
        else:
            return False
