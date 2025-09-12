'''
https://leetcode.com/problems/valid-perfect-square/
'''

def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low < high:
            mid = low + (high-low)//2
            if mid**2 == num:
                return True
            if mid**2 < num:
                low = mid + 1
            else:
                high = mid - 1
        return low**2 == num