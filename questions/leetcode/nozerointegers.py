'''
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
'''

def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            left = i
            right = n - i
            if '0' not in str(left) and '0' not in str(right):
                return [left, right]
        return []