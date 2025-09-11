'''
https://leetcode.com/problems/sqrtx/
'''
def mySqrt(self, x: int) -> int:
        l = 0
        r = x+1
        while l < r:
            mid = l + (r-l)//2
            if mid**2 == x:
                return mid
            if mid**2 > x:
                r = mid 
            else:
                l = mid + 1
        return l-1