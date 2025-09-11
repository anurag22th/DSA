'''
https://leetcode.com/problems/power-of-three/
'''
def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n//3
        return (n == 1)
        return n>0 and (1162261467%n)==0
        #thats the largest 32 bit int divided by 3 and for 2 we did & since if it is even num then the odd & will give 0