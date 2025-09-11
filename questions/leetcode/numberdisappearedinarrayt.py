'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    '''
    lst = []
    for i in range(1,len(nums)+1) :
        lst.append(i)
    return list(set(lst)-set(nums))'''

    set_num = set(nums)
    return [i for i in range(1,len(nums)+1) if i not in set_num]