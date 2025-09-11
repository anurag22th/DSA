'''
https://leetcode.com/problems/binary-search/
'''

def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        if target not in nums:
            return -1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return l