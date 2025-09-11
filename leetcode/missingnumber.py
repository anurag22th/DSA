'''
https://leetcode.com/problems/missing-number/
'''

def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(1+n)//2 # sum of series ke 2 formulae hai n*(2a+(n-1)d)/2 and this
        return total_sum - sum(nums)