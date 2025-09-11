'''
https://leetcode.com/problems/largest-3-same-digit-number-in-string/
'''
# main idhar 9,8,7 aise dekh raha hu kyun ki str main toh 0-9 hi number rahenge na
# yeh nahi toh string main jaake, max nikalke karna padta
def largestGoodInteger(self, num: str) -> str:
    for i in range(9,-1,-1):
        temp = (str(i)*3)
        if temp in num:
            return temp
    return ''