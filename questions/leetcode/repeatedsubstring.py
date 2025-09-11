'''
https://leetcode.com/problems/repeated-substring-pattern/
'''
def repeatedSubstringPattern(self, s: str) -> bool:
    '''if len(s)%2 != 0:
        return False
    return True'''
    return s in (s+s)[1:-1]
    '''n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return True
    return False'''
    #return s[:(len(s)//2)] == s[(len(s)//2):]
        