'''
https://leetcode.com/problems/base-7/
'''

def convertToBase7(self, num: int) -> str:
        # bina if ke kiya, while main temp_num >= 0 dala toh TLE aaya tha
        ans = ''
        temp_num = abs(num)
        if num == 0:
            return "0"
        while temp_num:
            ans += str(temp_num%7)
            temp_num = temp_num//7
        ans = ans[::-1]
        if num < 0:
            ans = '-'+ans
        return ans