'''
https://leetcode.com/problems/is-subsequence/
'''

def isSubsequence(self, s: str, t: str) -> bool:
        '''i,j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)'''
        point = 0
        for i in range(len(t)):
            if point < len(s) and s[point] == t[i]:
                point += 1
        return point == len(s)