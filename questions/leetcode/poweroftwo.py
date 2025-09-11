'''
https://leetcode.com/problems/power-of-two/
'''
def isPowerOfTwo(self, n: int) -> bool:
        #if n< 2:
        #agar divisible by 2 hai toh uska count 1 hi hoga
        return n>0 and str(bin(n)).count('1')==1
        #
        return n and n&(n-1)==0