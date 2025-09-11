'''
https://leetcode.com/problems/find-closest-person/
'''

def findClosestPerson(x,y,z):
    if abs(z-x) > abs(z-y):
        return 2
    elif  abs(z-x) < abs(z-y):
        return 1
    return 0