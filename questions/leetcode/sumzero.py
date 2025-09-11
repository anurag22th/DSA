'''
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
'''

def sumZero(self, n: int) -> List[int]:   
    lst = [x for x in range(-n//2,n//2+1)]
    if n%2 == 0:
        lst.remove(0)
    return lst
