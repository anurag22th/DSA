'''
https://leetcode.com/problems/valid-anagram/
'''
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(t):
            if t.count(i) != s.count(i):
                return False
        return True