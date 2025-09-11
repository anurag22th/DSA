"""
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
"""
# idhar agar do element ek saath aaye toh same wale ko ignore kar
def countHillValley(self, nums: List[int]) -> int:
    count = 0
    for i in range(1,len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i-1]
        if (nums[i-1]<nums[i] and nums[i+1]<nums[i]) or (nums[i-1]>nums[i] and nums[i+1]>nums[i]):
            count += 1
    return count