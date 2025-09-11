"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""

def findLucky(self, arr: List[int]) -> int:
        max_num = -1
        #count complexity badha deta hai
        ''' 
        for i in arr:
            if i == arr.count(i):
                temp_num = i
                max_num = max(temp_num, max_num)
        return max_num'''
        dct = {}
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        for i in dct:
            if dct[i] == i:
                val = i
                if val > max_num:
                    max_num = val
        return max_num