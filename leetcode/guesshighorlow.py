'''
https://leetcode.com/problems/guess-number-higher-or-lower/
'''
def guessNumber(self, n: int) -> int:
        l = 1
        r = n+1
        while l<r:
            mid = l+(r-l)//2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                r = mid
            else:
                l = mid+1
        return l
